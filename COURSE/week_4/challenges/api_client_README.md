# Challenge 1: Soccer Data API Client

This challenge focuses on creating a client to fetch and process soccer data from public APIs.

## Overview

Modern sports applications rely on data from external APIs. In this challenge, you'll implement functions to request soccer team and player data from public APIs, with an emphasis on understanding how API clients work rather than complex implementations.

## Learning Focus

- Making HTTP requests to external APIs
- Working with query parameters and headers
- Handling and processing API responses
- Error handling for API requests
- Creating a reusable API client

## Key Concepts Explained

### API Request/Response Cycle

```
┌──────────────┐       1. HTTP Request        ┌────────────┐
│              │ ─────────────────────────────>            │
│  Your Code   │      (URL, headers, etc)     │  API       │
│  (Client)    │                              │  Server    │
│              │ <─────────────────────────────            │
└──────────────┘      2. HTTP Response        └────────────┘
                    (JSON data, status code)
```

### Making API Requests with Python

The Python `requests` library is the standard way to make HTTP requests:

```python
import requests

# Basic GET request
response = requests.get("https://api.example.com/teams")

# GET request with query parameters
response = requests.get(
    "https://api.example.com/teams",
    params={"country": "England"}
)

# GET request with headers (like API keys)
response = requests.get(
    "https://api.example.com/teams",
    headers={"X-API-Key": "your_api_key"}
)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dict
else:
    print(f"Error: {response.status_code}")
```

### Common HTTP Status Codes

- **200 OK**: The request succeeded
- **201 Created**: The request succeeded and created a new resource
- **400 Bad Request**: The server couldn't understand the request
- **401 Unauthorized**: Authentication is required and has failed
- **403 Forbidden**: The server understood but refuses to authorize
- **404 Not Found**: The requested resource doesn't exist
- **500 Internal Server Error**: The server encountered an unexpected error

## Functions to Implement

### 1. `make_request`

This function makes a generic HTTP request to an API endpoint.

**Tips:**
- Use the `requests` library
- Handle different HTTP methods (GET, POST, etc.)
- Process the response to return useful data

**Pseudocode:**
```
function make_request(url, method="GET", params=None, headers=None, data=None):
    try:
        if method is "GET":
            send a GET request with the provided params and headers
        else if method is "POST":
            send a POST request with the provided params, headers, and data
        # Add support for other methods if needed
        
        check if response status code is in the 200s (success)
        
        if successful and response contains JSON:
            return the parsed JSON data
        else:
            return an error message with the status code
            
    except requests.exceptions.RequestException as e:
        handle network errors, timeouts, etc.
        return an error message
```

**Example Usage:**
```python
# Get data from a soccer API
data = make_request(
    "https://www.thesportsdb.com/api/v1/json/3/searchteams.php",
    params={"t": "Arsenal"}
)
print(data)
```

### 2. `get_team_info`

This function gets information about a specific soccer team.

**Tips:**
- Build on your `make_request` function
- Use appropriate API endpoint and parameters
- Extract and format only the relevant team data

**Pseudocode:**
```
function get_team_info(team_name):
    endpoint = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    
    response_data = make_request(endpoint, params={"t": team_name})
    
    if response_data contains error:
        return the error
    
    if "teams" in response_data and response_data["teams"] is not empty:
        extract the first team from the results
        
        create a simplified team_info dictionary with:
            - name
            - country
            - league
            - year_formed
            - stadium
            - description
            
        return team_info
    else:
        return an error indicating team not found
```

**Example Usage:**
```python
team = get_team_info("Barcelona")
if "error" not in team:
    print(f"Team: {team['name']}")
    print(f"League: {team['league']}")
    print(f"Stadium: {team['stadium']}")
```

### 3. `get_team_players`

This function gets the roster of players for a soccer team.

**Tips:**
- First fetch the team ID, then get the players for that team
- Filter and format the player data for easier use
- Handle cases where the team or players aren't found

**Pseudocode:**
```
function get_team_players(team_name):
    # First get the team ID
    endpoint = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    
    response_data = make_request(endpoint, params={"t": team_name})
    
    if response_data contains error or team not found:
        return the error
    
    team_id = extract team ID from the response
    
    # Now get the players for this team
    players_endpoint = "https://www.thesportsdb.com/api/v1/json/3/lookup_all_players.php"
    
    response_data = make_request(players_endpoint, params={"id": team_id})
    
    if response_data contains error or no players found:
        return the error or an empty list
    
    create an empty list for formatted_players
    
    for each player in response_data["player"]:
        create a simplified player dictionary with:
            - name
            - position
            - nationality
            - birth_date
        add the player to formatted_players
    
    return formatted_players
```

**Example Usage:**
```python
players = get_team_players("Manchester United")
if isinstance(players, list):
    for player in players:
        print(f"{player['name']} - {player['position']}")
```

### 4. `search_players`

This function searches for soccer players by name.

**Tips:**
- Use the appropriate API endpoint for player searches
- Format the results for easier consumption
- Handle cases where no players are found

**Pseudocode:**
```
function search_players(player_name):
    endpoint = "https://www.thesportsdb.com/api/v1/json/3/searchplayers.php"
    
    response_data = make_request(endpoint, params={"p": player_name})
    
    if response_data contains error:
        return the error
    
    if "player" in response_data and response_data["player"] is not empty:
        create an empty list for formatted_players
        
        for each player in response_data["player"]:
            create a simplified player dictionary with:
                - name
                - team
                - position
                - nationality
            add the player to formatted_players
        
        return formatted_players
    else:
        return an empty list
```

**Example Usage:**
```python
players = search_players("Messi")
if players:
    for player in players:
        print(f"{player['name']} - {player['team']}")
else:
    print("No players found")
```

### 5. `create_soccer_api_client`

This function creates a reusable soccer API client with multiple methods.

**Tips:**
- Create a dictionary of functions that can be called
- Encapsulate the API base URL and any common headers
- Return a client object that can make various requests

**Pseudocode:**
```
function create_soccer_api_client():
    base_url = "https://www.thesportsdb.com/api/v1/json/3"
    
    # Define client methods within this function
    def get_team(team_name):
        return get_team_info(team_name)  # Reuse your existing function
    
    def get_players(team_name):
        return get_team_players(team_name)  # Reuse your existing function
    
    def search_player(player_name):
        return search_players(player_name)  # Reuse your existing function
    
    def get_league(league_name):
        endpoint = f"{base_url}/search_all_leagues.php"
        return make_request(endpoint, params={"l": league_name})
    
    # Create and return the client object
    return {
        "get_team": get_team,
        "get_players": get_players,
        "search_player": search_player,
        "get_league": get_league
    }
```

**Example Usage:**
```python
# Create a soccer API client
soccer_api = create_soccer_api_client()

# Use the client to make various requests
team = soccer_api["get_team"]("Liverpool")
players = soccer_api["get_players"]("Liverpool")
search_results = soccer_api["search_player"]("Salah")
```

## API Rate Limits and Error Handling

Most public APIs have rate limits (maximum number of requests per time period). Your code should handle these gracefully:

```python
# Example rate limit handling
if response.status_code == 429:  # Too Many Requests
    print("Rate limit exceeded. Please wait before making more requests.")
    retry_after = response.headers.get("Retry-After", "60")
    print(f"Try again in {retry_after} seconds")
```

## Testing Your Implementation

Run the file with:

```python
python api_client.py
```

The provided `main()` function will test your implementations with sample API calls. If the APIs are functioning correctly, you should see team and player data printed to the console.

## Using Alternative APIs

If the TheSportsDB API is unavailable or rate-limited, you can modify your functions to use these alternatives:

1. **Football-Data.org**: Offers a free tier with limited access
2. **API-Football**: Requires registration but has a free tier
3. **OpenFootball JSON datasets**: Static data that doesn't require API calls

The concepts remain the same regardless of which API you use.

## Further Exploration

After completing the challenge, consider:

1. How would you implement caching to reduce duplicate API calls?

2. Could you add error retry logic to automatically retry failed requests?

3. How might you handle authentication for APIs that require it?

## Connect to Capstone

For your NCAA soccer analysis capstone, the ability to create API clients will be valuable for:

- Retrieving data from NCAA statistics services
- Integrating with third-party sports data providers
- Creating a consistent interface for accessing different data sources
- Building a data pipeline that can adapt to different API structures

These skills form the foundation for your data collection system, allowing you to access and process soccer data from various sources.