# Challenge 4: Soccer Data API Client

This challenge focuses on accessing and processing soccer data from external APIs.

## Overview

Professional soccer data is often available through API services. In this challenge, you'll implement functions to connect to soccer APIs, retrieve data, and handle different response scenarios. The focus is on understanding API concepts rather than implementing complex functionality.

## Learning Focus

- Making API requests
- Handling API responses
- Managing request parameters and authentication
- Error handling for API interactions
- Organizing and processing returned data

## Key Concepts Explained

### API Basics

**What is an API?**

An API (Application Programming Interface) allows different software systems to communicate. In our context, it lets your Python code request soccer data from online services.

**HTTP Methods**:
- **GET**: Retrieve data (most common for data fetching)
- **POST**: Send data to create or update resources
- **PUT**: Update existing resources
- **DELETE**: Remove resources

**API Request Diagram**:
```
┌─────────────┐         HTTP Request         ┌─────────────┐
│             │ ──────────────────────────→  │             │
│  Your Code  │     (URL, parameters,        │   API       │
│             │      headers, etc.)          │   Server    │
│             │ ←────────────────────────────│             │
└─────────────┘      HTTP Response           └─────────────┘
                 (JSON/XML data, status code)
```

**Using the Requests Library**:
```python
import requests

# Basic GET request
response = requests.get("https://api.example.com/players")

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response to Python dict
    print(data)
else:
    print(f"Error: {response.status_code}")
```

## Functions to Implement

### 1. `make_api_request`

This function makes a generic API request with error handling.

**Tips:**
- Use the requests library
- Support different HTTP methods (GET, POST, etc.)
- Handle common request errors
- Return both the data and status code

**Pseudocode:**
```
function make_api_request(url, method="GET", headers=None, params=None, data=None, timeout=10):
    try:
        if method is "GET":
            make a GET request with the provided parameters
        else if method is "POST":
            make a POST request with the provided parameters
        else if method is "PUT":
            make a PUT request with the provided parameters
        else if method is "DELETE":
            make a DELETE request with the provided parameters
        else:
            raise ValueError for unsupported method
        
        check if response status code indicates success (200-299)
        if successful:
            try to parse the response as JSON
            return (parsed_data, status_code)
        else:
            return (error_message, status_code)
            
    except requests.exceptions.Timeout:
        raise appropriate timeout error
    except requests.exceptions.ConnectionError:
        raise appropriate connection error
    except requests.exceptions.RequestException:
        raise generic request error
```

**Example Usage:**
```python
try:
    data, status = make_api_request("https://jsonplaceholder.typicode.com/posts/1")
    if status == 200:
        print(f"Retrieved post: {data['title']}")
    else:
        print(f"Error: Status code {status}")
except Exception as e:
    print(f"Request failed: {e}")
```

### 2. `get_soccer_team_info`

This function retrieves information about a soccer team from a public API.

**Tips:**
- Build on your `make_api_request` function
- Handle team-not-found scenarios
- Extract and return relevant team data

**Pseudocode:**
```
function get_soccer_team_info(team_name, api_key=None):
    # For this example, we'll use a free API that doesn't require authentication
    base_url = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    
    params = {"t": team_name}
    
    data, status = make_api_request(base_url, params=params)
    
    if status != 200:
        raise ValueError with message about API error
    
    if "teams" not in data or not data["teams"]:
        raise ValueError with message about team not found
    
    team_data = data["teams"][0]  # Get the first matching team
    
    # Extract relevant information
    team_info = {
        "name": team_data["strTeam"],
        "country": team_data["strCountry"],
        "league": team_data["strLeague"],
        "year_formed": team_data["intFormedYear"],
        "stadium": team_data["strStadium"],
        "description": team_data["strDescriptionEN"]
    }
    
    return team_info
```

**Example Usage:**
```python
try:
    team_info = get_soccer_team_info("Arsenal")
    print(f"Team: {team_info['name']}")
    print(f"League: {team_info['league']}")
    print(f"Stadium: {team_info['stadium']}")
except ValueError as e:
    print(e)
```

### 3. `search_players`

This function searches for soccer players by name.

**Tips:**
- Structure your API request with appropriate parameters
- Format the returned data for easier use
- Handle empty search results gracefully

**Pseudocode:**
```
function search_players(player_name, api_key=None):
    base_url = "https://www.thesportsdb.com/api/v1/json/3/searchplayers.php"
    
    params = {"p": player_name}
    
    data, status = make_api_request(base_url, params=params)
    
    if status != 200:
        raise ValueError with message about API error
    
    if "player" not in data or not data["player"]:
        return []  # No players found
    
    players = []
    for player_data in data["player"]:
        player = {
            "name": player_data["strPlayer"],
            "team": player_data["strTeam"],
            "position": player_data["strPosition"],
            "nationality": player_data["strNationality"],
            "birth_date": player_data["dateBorn"]
        }
        players.append(player)
    
    return players
```

**Example Usage:**
```python
players = search_players("Messi")
if players:
    for player in players:
        print(f"{player['name']} - {player['team']} - {player['position']}")
else:
    print("No players found")
```

### 4. `get_team_players`

This function retrieves all players for a specific team.

**Tips:**
- Use the team ID or name to query the API
- Process the response to extract player information
- Organize players by position for easier analysis

**Pseudocode:**
```
function get_team_players(team_name, api_key=None):
    # First get the team ID
    base_url = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    
    params = {"t": team_name}
    
    data, status = make_api_request(base_url, params=params)
    
    if status != 200 or "teams" not in data or not data["teams"]:
        raise ValueError with message about team not found
    
    team_id = data["teams"][0]["idTeam"]
    
    # Now get the players for this team
    players_url = "https://www.thesportsdb.com/api/v1/json/3/lookup_all_players.php"
    
    params = {"id": team_id}
    
    data, status = make_api_request(players_url, params=params)
    
    if status != 200:
        raise ValueError with message about API error
    
    if "player" not in data or not data["player"]:
        return []  # No players found
    
    players = []
    for player_data in data["player"]:
        player = {
            "name": player_data["strPlayer"],
            "position": player_data["strPosition"],
            "nationality": player_data["strNationality"],
            "birth_date": player_data["dateBorn"],
            "height": player_data["strHeight"],
            "weight": player_data["strWeight"]
        }
        players.append(player)
    
    return players
```

**Example Usage:**
```python
try:
    players = get_team_players("Manchester United")
    positions = {}
    for player in players:
        pos = player["position"]
        if pos not in positions:
            positions[pos] = []
        positions[pos].append(player["name"])
    
    for pos, player_list in positions.items():
        print(f"{pos}: {', '.join(player_list)}")
except ValueError as e:
    print(e)
```

### 5. `save_api_data_to_json`

This function saves API response data to a JSON file.

**Tips:**
- Ensure the data is in the right format
- Create a proper file structure
- Add error handling for file operations

**Pseudocode:**
```
function save_api_data_to_json(data, filepath):
    try:
        import json
        
        open the file in write mode using a context manager
        write the data using json.dump() with indent=2 for formatting
        return True on success
    except IOError:
        raise appropriate file error
    except TypeError:
        raise error about data not being JSON serializable
```

**Example Usage:**
```python
try:
    team_info = get_soccer_team_info("Liverpool")
    save_api_data_to_json(team_info, "liverpool_info.json")
    print("Team information saved successfully")
except Exception as e:
    print(f"Error: {e}")
```

## API Limitations and Alternatives

**Note on API Limitations**:
Most comprehensive soccer APIs require registration and may have usage limits. The examples in this challenge use free public APIs that may have limited data. In a real-world scenario, you might:

1. Use a paid API service with more complete data
2. Register for a free account to get an API key with higher limits
3. Implement caching to reduce API calls
4. Have fallback options when APIs are unavailable

For this challenge, focus on understanding the concepts rather than accessing comprehensive data.

## Testing Your Implementation

Run the file with:

```python
python api_integration.py
```

The provided `main()` function will test your implementations with sample API calls. Be aware that public APIs may have rate limits or may change over time.

## Further Exploration

After completing the challenge, consider:

1. How would you implement caching to avoid repeated API calls for the same data?

2. Could you create a more comprehensive client that combines data from multiple APIs?

3. How might you handle authentication for APIs that require it?

## Connect to Capstone

For your NCAA soccer analysis capstone, API integration will be crucial for:

- Accessing real-time NCAA soccer data where available
- Retrieving historical match results and statistics
- Collecting player information from various sources
- Keeping your analysis system updated with the latest data

These skills will allow you to create a dynamic analysis system that can adapt to new data as it becomes available throughout the NCAA soccer season.