# Challenge 4: Basic API Authentication

This challenge focuses on implementing simple authentication mechanisms for your soccer API.

## Overview

Securing API endpoints is essential for protecting sensitive data and operations. In this challenge, you'll implement basic authentication mechanisms for a soccer API, focusing on understanding the key concepts rather than creating a production-ready system.

## Learning Focus

- API key authentication
- Basic password security
- JSON Web Tokens (JWT) concepts
- Protecting API endpoints
- Authentication vs. Authorization

## Key Concepts Explained

### Authentication vs. Authorization

- **Authentication**: Verifying who the user is (identity)
- **Authorization**: Determining what the user is allowed to do (permissions)

### API Key Authentication

API keys are simple strings that clients include in their requests:

```
┌──────────────┐                              ┌────────────┐
│              │    Request with API Key      │            │
│   Client     │ ─────────────────────────────> API Server │
│              │  (Header: X-API-Key: abc123) │            │
└──────────────┘                              └────────────┘
                                                     │
                                                     ▼
                                              ┌────────────┐
                                              │ Verify Key │
                                              │ is valid   │
                                              └────────────┘
```

### JWT (JSON Web Token) Authentication

JWTs provide a way to securely transmit information between parties:

```
┌──────────────┐                               ┌────────────┐
│              │  1. Login (username/password) │            │
│   Client     │ ─────────────────────────────>│  Server    │
│              │                               │            │
│              │  2. JWT Token                 │            │
│              │ <─────────────────────────────│            │
└──────────────┘                               └────────────┘

┌──────────────┐                               ┌────────────┐
│              │  3. Request with JWT Token    │            │
│   Client     │ ─────────────────────────────>│  Server    │
│              │                               │            │
│              │  4. Protected Resource        │            │
│              │ <─────────────────────────────│            │
└──────────────┘                               └────────────┘
```

A JWT consists of three parts:
1. **Header**: Specifies the token type and algorithm
2. **Payload**: Contains claims about the user and token
3. **Signature**: Verifies the token hasn't been tampered with

## Functions to Implement

In this challenge, you'll implement several authentication methods in the AuthManager class. This class manages API keys and user credentials.

### 1. `generate_api_key`

This function generates a new API key for a user.

**Tips:**
- Create a secure, random API key
- Store the key with metadata like owner and permissions
- Return the generated key

**Pseudocode:**
```
function generate_api_key(owner_name, permissions=None):
    # Generate a secure random API key
    api_key = generate a random string of letters and numbers
    
    # Set default permissions if none provided
    if permissions is None:
        permissions = ["read"]
    
    # Create API key metadata
    key_data = {
        "owner": owner_name,
        "permissions": permissions,
        "created_at": current timestamp,
        "last_used": None
    }
    
    # Store the API key
    self.api_keys[api_key] = key_data
    self._save_api_keys()
    
    return api_key
```

**Example Usage:**
```python
auth_manager = AuthManager()
api_key = auth_manager.generate_api_key("Coach Smith", ["read", "write"])
print(f"Your API key: {api_key}")
```

### 2. `validate_api_key`

This function validates an API key and checks if it has the required permissions.

**Tips:**
- Check if the key exists in your store
- Verify if the key has the required permissions
- Return information about the key's validity

**Pseudocode:**
```
function validate_api_key(api_key, required_permissions=None):
    # Check if API key exists
    if api_key not in self.api_keys:
        return False, None, None
    
    # Get key data
    key_data = self.api_keys[api_key]
    owner_name = key_data["owner"]
    permissions = key_data["permissions"]
    
    # If permissions are required, check them
    if required_permissions:
        has_permissions = True
        for permission in required_permissions:
            if permission not in permissions:
                has_permissions = False
                break
        
        if not has_permissions:
            return False, owner_name, permissions
    
    # Update last used timestamp
    key_data["last_used"] = current timestamp
    self._save_api_keys()
    
    return True, owner_name, permissions
```

**Example Usage:**
```python
is_valid, owner, permissions = auth_manager.validate_api_key(api_key, ["read"])
if is_valid:
    print(f"Valid API key from {owner}")
    print(f"Permissions: {permissions}")
else:
    print("Invalid API key or insufficient permissions")
```

### 3. `register_user`

This function registers a new user with a username and password.

**Tips:**
- Hash the password securely (don't store plaintext)
- Check for duplicate usernames
- Store user information securely

**Pseudocode:**
```
function register_user(username, password, email, role='user'):
    # Check if username already exists
    if username in self.users:
        raise ValueError("Username already exists")
    
    # Hash the password
    password_hash, salt = self._hash_password(password)
    
    # Create user data
    user_data = {
        "username": username,
        "email": email,
        "role": role,
        "password_hash": password_hash,
        "salt": salt,
        "created_at": current timestamp
    }
    
    # Store the user
    self.users[username] = user_data
    self._save_users()
    
    # Return user data without password
    user_info = user_data.copy()
    del user_info["password_hash"]
    del user_info["salt"]
    
    return user_info
```

**Example Usage:**
```python
try:
    user = auth_manager.register_user("coach_smith", "secure_password", "coach@team.com", "admin")
    print(f"User registered: {user['username']}")
except ValueError as e:
    print(f"Error: {e}")
```

### 4. `authenticate_user`

This function authenticates a user with a username and password.

**Tips:**
- Hash the provided password using the same method as registration
- Compare the hash with the stored hash
- Return authentication status and user info

**Pseudocode:**
```
function authenticate_user(username, password):
    # Check if username exists
    if username not in self.users:
        return False, None
    
    # Get user data
    user_data = self.users[username]
    stored_hash = user_data["password_hash"]
    salt = user_data["salt"]
    
    # Hash the provided password with the stored salt
    password_hash, _ = self._hash_password(password, salt)
    
    # Compare the hashes
    if password_hash == stored_hash:
        # Return user data without password
        user_info = user_data.copy()
        del user_info["password_hash"]
        del user_info["salt"]
        
        return True, user_info
    else:
        return False, None
```

**Example Usage:**
```python
is_authenticated, user_data = auth_manager.authenticate_user("coach_smith", "secure_password")
if is_authenticated:
    print(f"Authentication successful for {user_data['username']}")
else:
    print("Authentication failed")
```

### 5. `generate_jwt_token`

This function generates a JWT token for an authenticated user.

**Tips:**
- Create a token payload with user information and expiration
- Sign the token with a secret key
- Return the complete JWT token

**Pseudocode:**
```
function generate_jwt_token(user_data):
    # Import JWT library
    import jwt
    from datetime import datetime, timedelta
    
    # Create token payload
    payload = {
        "sub": user_data["username"],
        "email": user_data["email"],
        "role": user_data["role"],
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    
    # Sign the token
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return token
```

**Example Usage:**
```python
if is_authenticated:
    token = auth_manager.generate_jwt_token(user_data)
    print(f"JWT Token: {token}")
```

### 6. `validate_jwt_token`

This function validates a JWT token and extracts its payload.

**Tips:**
- Verify the token's signature using the secret key
- Check that the token hasn't expired
- Return validation status and payload

**Pseudocode:**
```
function validate_jwt_token(token):
    # Import JWT library
    import jwt
    
    try:
        # Decode and verify the token
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        
        # Check if token has expired
        if "exp" in payload and payload["exp"] < current timestamp:
            return False, {"error": "Token has expired"}
        
        return True, payload
    except jwt.InvalidTokenError:
        return False, {"error": "Invalid token"}
```

**Example Usage:**
```python
is_valid, payload = auth_manager.validate_jwt_token(token)
if is_valid:
    print(f"Valid token for user: {payload['sub']}")
    print(f"Role: {payload['role']}")
else:
    print(f"Invalid token: {payload.get('error')}")
```

## Password Security

Proper password security is essential. The `_hash_password` method should:

1. Generate a random salt if none is provided
2. Combine the password with the salt
3. Apply a strong hashing algorithm (like PBKDF2, bcrypt, or Argon2)
4. Return the hash and salt

**Pseudocode:**
```
function _hash_password(password, salt=None):
    # Generate salt if not provided
    if salt is None:
        salt = generate random bytes
    
    # Hash the password with the salt using PBKDF2
    password_hash = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    
    # Convert to hex strings for storage
    password_hash_hex = password_hash.hex()
    salt_hex = salt.hex()
    
    return password_hash_hex, salt_hex
```

## Testing Your Implementation

Run the file with:

```python
python auth_system.py
```

The provided `main()` function will test your implementations with example usage. You should see output showing successful API key generation, user registration, authentication, and JWT token generation/validation.

## Further Exploration

After completing the challenge, consider:

1. How would you implement role-based authorization for different API endpoints?

2. Could you add token refresh capability to extend token lifetimes securely?

3. How might you implement more advanced security features like rate limiting?

## Connect to Capstone

For your NCAA soccer analysis capstone, secure authentication will be important for:

- Protecting access to sensitive data and analytics
- Providing different access levels for coaches, players, and administrators
- Securing API endpoints that modify data
- Creating a safe multi-user environment

These authentication concepts will help you build a secure foundation for your capstone project, ensuring that your NCAA soccer data is properly protected.