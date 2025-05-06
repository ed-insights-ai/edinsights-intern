"""
Function Workshop
---------------
Complete the following functions according to their docstrings.
This exercise focuses on creating and using functions in Python.
Be sure to add appropriate docstrings to document your functions.
"""

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (number): First number
        b (number): Second number
        
    Returns:
        number: The product of a and b
        
    Example:
        >>> multiply(3, 4)
        12
    """
    # YOUR CODE HERE
    pass

def greet_user(name, greeting="Hello"):
    """
    Generate a greeting message for a user.
    
    Args:
        name (str): The name of the user
        greeting (str, optional): The greeting to use. Defaults to "Hello"
        
    Returns:
        str: The complete greeting message
        
    Example:
        >>> greet_user("Alice")
        'Hello, Alice!'
        >>> greet_user("Bob", "Hi")
        'Hi, Bob!'
    """
    # YOUR CODE HERE
    pass

def calculate_area(shape, **kwargs):
    """
    Calculate the area of different shapes based on the provided parameters.
    
    Supported shapes:
    - "rectangle": requires 'width' and 'height' parameters
    - "circle": requires 'radius' parameter
    - "triangle": requires 'base' and 'height' parameters
    
    Args:
        shape (str): The type of shape ("rectangle", "circle", or "triangle")
        **kwargs: Keyword arguments for shape dimensions
            - For rectangle: width, height
            - For circle: radius
            - For triangle: base, height
            
    Returns:
        float: The calculated area or None if invalid parameters
        
    Example:
        >>> calculate_area("rectangle", width=5, height=3)
        15.0
        >>> calculate_area("circle", radius=2)
        12.566370614359172
        >>> calculate_area("triangle", base=4, height=6)
        12.0
    """
    # YOUR CODE HERE
    pass

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence.
    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The Fibonacci number at position n
        
    Example:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(6)
        8
    """
    # YOUR CODE HERE
    pass

def validate_email(email):
    """
    Validate if the provided string is a proper email address.
    
    A simple validation that checks:
    1. Contains exactly one '@' character
    2. Has at least one character before the '@'
    3. Has at least one '.' after the '@'
    4. Has at least one character between '@' and '.'
    5. Has at least one character after the last '.'
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if the email is valid, False otherwise
        
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid@")
        False
        >>> validate_email("user@.com")
        False
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing multiply...")
    print(f"multiply(3, 4) = {multiply(3, 4)}")
    
    print("\nTesting greet_user...")
    print(f"greet_user('Alice') = {greet_user('Alice')}")
    print(f"greet_user('Bob', 'Hi') = {greet_user('Bob', 'Hi')}")
    
    print("\nTesting calculate_area...")
    print(f"calculate_area('rectangle', width=5, height=3) = {calculate_area('rectangle', width=5, height=3)}")
    print(f"calculate_area('circle', radius=2) = {calculate_area('circle', radius=2)}")
    print(f"calculate_area('triangle', base=4, height=6) = {calculate_area('triangle', base=4, height=6)}")
    
    print("\nTesting fibonacci...")
    print(f"fibonacci(0) = {fibonacci(0)}")
    print(f"fibonacci(1) = {fibonacci(1)}")
    print(f"fibonacci(6) = {fibonacci(6)}")
    
    print("\nTesting validate_email...")
    print(f"validate_email('user@example.com') = {validate_email('user@example.com')}")
    print(f"validate_email('invalid@') = {validate_email('invalid@')}")
    print(f"validate_email('user@.com') = {validate_email('user@.com')}")

if __name__ == "__main__":
    main()