# Challenge 3: Soccer Team API Server

This challenge focuses on creating a simple Flask API server for soccer team data.

## Overview

Web APIs are crucial for modern applications to share and access data. In this challenge, you'll implement a basic RESTful API for soccer team data using Flask. The focus is on understanding API design concepts rather than building a complex system.

## Learning Focus

- Creating basic Flask API endpoints
- Implementing RESTful API patterns
- Handling different HTTP methods (GET, POST, PUT, DELETE)
- Managing API responses and status codes
- Implementing basic data validation

## Key Concepts Explained

### Flask API Basics

Flask is a lightweight web framework that makes it easy to create APIs:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/teams', methods=['GET'])
def get_teams():
    # This function handles GET requests to /api/teams
    teams = [{"id": 1, "name": "Liverpool"}, {"id": 2, "name": "Chelsea"}]
    return jsonify(teams)  # Convert Python data to JSON response

@app.route('/api/teams/<team_id>', methods=['GET'])
def get_team(team_id):
    # This function handles GET requests to /api/teams/1, /api/teams/2, etc.
    # team_id is a URL parameter
    team = {"id": team_id, "name": f"Team {team_id}"}
    return jsonify(team)

if __name__ == '__main__':
    app.run(debug=True)  # Start the development server
```

### RESTful API Structure

RESTful APIs organize endpoints around resources (like teams or players):

| HTTP Method | URL | Action | Response Code |
|-------------|-----|--------|---------------|
| GET | /api/teams | List all teams | 200 OK |
| GET | /api/teams/123 | Get details for team 123 | 200 OK |
| POST | /api/teams | Create a new team | 201 Created |
| PUT | /api/teams/123 | Update team 123 | 200 OK |
| DELETE | /api/teams/123 | Delete team 123 | 204 No Content |

## Functions to Implement

In this challenge, you'll implement several API endpoints for a soccer team management system. The starter code already includes route definitions - you just need to implement the functions.

### 1. `get_teams`

This function handles GET requests to retrieve all teams or filter teams by query parameters.

**Tips:**
- Return a JSON array of team objects
- Support filtering with request query parameters
- Handle empty results appropriately

**Pseudocode:**
```
function get_teams():
    # Load teams data from file
    teams = load_teams()
    
    # Get query parameters
    country = request.args.get('country')
    league = request.args.get('league')
    
    # Filter teams if query parameters are provided
    if country:
        teams = filter teams where team['country'] matches country
    
    if league:
        teams = filter teams where team['league'] matches league
    
    # Return the teams as JSON
    return jsonify(teams)
```

**Example Request:**
```
GET /api/v1/teams
GET /api/v1/teams?country=England
GET /api/v1/teams?country=Spain&league=La%20Liga
```

### 2. `get_team`

This function handles GET requests to retrieve a specific team by ID.

**Tips:**
- Use the team_id parameter from the URL
- Return 404 if the team doesn't exist
- Return a JSON object with team details

**Pseudocode:**
```
function get_team(team_id):
    # Load teams data from file
    teams = load_teams()
    
    # Find the team with the given ID
    team = find team in teams where team['id'] equals team_id
    
    if team is found:
        return jsonify(team)
    else:
        # Return 404 Not Found if team doesn't exist
        return jsonify({"error": "Team not found"}), 404
```

**Example Request:**
```
GET /api/v1/teams/123
```

### 3. `create_team`

This function handles POST requests to create a new team.

**Tips:**
- Parse JSON data from the request body
- Validate required fields
- Add the new team to the data store
- Return the created team with a 201 status code

**Pseudocode:**
```
function create_team():
    # Get JSON data from request
    team_data = request.get_json()
    
    # Validate required fields
    if 'name' not in team_data:
        return jsonify({"error": "Team name is required"}), 400
    
    if 'country' not in team_data:
        return jsonify({"error": "Team country is required"}), 400
    
    # Load existing teams
    teams = load_teams()
    
    # Generate a new ID for the team
    new_id = generate a unique ID
    
    # Create the new team
    new_team = {
        "id": new_id,
        "name": team_data["name"],
        "country": team_data["country"],
        "league": team_data.get("league", ""),
        "founded": team_data.get("founded", 0),
        "coach": team_data.get("coach", ""),
        "stadium": team_data.get("stadium", "")
    }
    
    # Add the new team to the list
    teams.append(new_team)
    
    # Save the updated teams list
    save_teams(teams)
    
    # Return the new team with 201 Created status
    return jsonify(new_team), 201
```

**Example Request:**
```
POST /api/v1/teams
Content-Type: application/json

{
  "name": "Liverpool FC",
  "country": "England",
  "league": "Premier League",
  "founded": 1892,
  "coach": "Jürgen Klopp",
  "stadium": "Anfield"
}
```

### 4. `update_team`

This function handles PUT requests to update an existing team.

**Tips:**
- Parse JSON data from the request body
- Check if the team exists
- Update the team data
- Return the updated team

**Pseudocode:**
```
function update_team(team_id):
    # Get JSON data from request
    team_data = request.get_json()
    
    # Load existing teams
    teams = load_teams()
    
    # Find the team with the given ID
    team_index = find index in teams where team['id'] equals team_id
    
    if team_index is found:
        # Update the team with new data
        teams[team_index]["name"] = team_data.get("name", teams[team_index]["name"])
        teams[team_index]["country"] = team_data.get("country", teams[team_index]["country"])
        teams[team_index]["league"] = team_data.get("league", teams[team_index]["league"])
        # Update other fields similarly
        
        # Save the updated teams list
        save_teams(teams)
        
        # Return the updated team
        return jsonify(teams[team_index])
    else:
        # Return 404 Not Found if team doesn't exist
        return jsonify({"error": "Team not found"}), 404
```

**Example Request:**
```
PUT /api/v1/teams/123
Content-Type: application/json

{
  "name": "Liverpool FC",
  "coach": "Jürgen Klopp"
}
```

### 5. `delete_team`

This function handles DELETE requests to remove a team.

**Tips:**
- Check if the team exists
- Remove the team from the data store
- Return a success message with 204 No Content status

**Pseudocode:**
```
function delete_team(team_id):
    # Load existing teams
    teams = load_teams()
    
    # Find the team with the given ID
    team_index = find index in teams where team['id'] equals team_id
    
    if team_index is found:
        # Remove the team
        teams.pop(team_index)
        
        # Save the updated teams list
        save_teams(teams)
        
        # Return 204 No Content
        return "", 204
    else:
        # Return 404 Not Found if team doesn't exist
        return jsonify({"error": "Team not found"}), 404
```

**Example Request:**
```
DELETE /api/v1/teams/123
```

### 6. `search_teams`

This function handles GET requests to search for teams by name, league, or other criteria.

**Tips:**
- Parse search criteria from query parameters
- Implement a flexible search mechanism
- Return an array of matching teams

**Pseudocode:**
```
function search_teams():
    # Get query parameters
    name = request.args.get('name', '')
    league = request.args.get('league', '')
    country = request.args.get('country', '')
    
    # Load teams data from file
    teams = load_teams()
    
    # Filter teams based on search criteria
    results = []
    for team in teams:
        # Check if team matches all provided criteria
        if (name and name.lower() not in team['name'].lower()):
            continue
        
        if (league and league.lower() not in team['league'].lower()):
            continue
            
        if (country and country.lower() not in team['country'].lower()):
            continue
        
        # If we get here, the team matches all criteria
        results.append(team)
    
    # Return the results
    return jsonify(results)
```

**Example Request:**
```
GET /api/v1/teams/search?name=united&country=england
```

## Data Storage

For simplicity, this challenge uses a JSON file to store team data. In a real application, you would use a database like PostgreSQL, MongoDB, or SQLite.

The starter code includes helper functions to load and save data:

```python
def load_teams():
    """Load teams from JSON file or create empty list if file doesn't exist."""
    try:
        if os.path.exists(TEAMS_FILE):
            with open(TEAMS_FILE, 'r') as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print(f"Error loading teams: {e}")
        return []

def save_teams(teams):
    """Save teams to JSON file."""
    try:
        with open(TEAMS_FILE, 'w') as f:
            json.dump(teams, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving teams: {e}")
        return False
```

## Testing Your API

Run the Flask server:

```python
python flask_api.py
```

The server will start running at http://127.0.0.1:5000/. You can test the API endpoints using:

1. **Web Browser**: Visit http://127.0.0.1:5000/api/v1/teams for GET requests
2. **curl**: Use command-line requests:
   ```bash
   curl -X GET http://127.0.0.1:5000/api/v1/teams
   curl -X POST -H "Content-Type: application/json" -d '{"name":"Manchester United","country":"England"}' http://127.0.0.1:5000/api/v1/teams
   ```
3. **Postman**: A graphical tool for API testing

## Further Exploration

After completing the challenge, consider:

1. How would you implement pagination for the GET /teams endpoint?

2. Could you add a players resource with its own endpoints and link it to teams?

3. How might you implement filtering, sorting, and searching capabilities?

## Connect to Capstone

For your NCAA soccer analysis capstone, building API endpoints will be essential for:

- Exposing player and team data to web dashboards
- Creating services that other applications can consume
- Providing a clean interface for your analysis tools
- Supporting multiple frontend applications with a common backend

This API design pattern will form the foundation of your capstone's data access layer, allowing different components to communicate efficiently.