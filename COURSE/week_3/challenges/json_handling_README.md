# Challenge 3: Team Roster Management

This challenge focuses on working with JSON data to manage soccer team rosters and player information.

## Overview

JSON (JavaScript Object Notation) is widely used in sports analytics for exchanging structured data between systems. In this challenge, you'll implement functions to read, modify, and analyze soccer team rosters stored in JSON format.

## Learning Focus

- Reading and writing JSON files
- Manipulating JSON data structures
- Converting between data formats
- Handling nested JSON objects
- Error management with JSON operations

## Key Concepts Explained

### JSON Basics

**JSON Format**:
JSON stores data as structured text using objects (dictionaries) and arrays (lists):
```json
{
  "team_name": "FC Barcelona",
  "players": [
    {
      "name": "Marc-André ter Stegen",
      "position": "Goalkeeper",
      "number": 1
    },
    {
      "name": "Robert Lewandowski",
      "position": "Forward",
      "number": 9
    }
  ]
}
```

**Working with JSON in Python**:
```python
import json

# Reading JSON from a file
with open('team.json', 'r') as file:
    team_data = json.load(file)  # Converts JSON to Python dict/list

# Writing Python data as JSON to a file
with open('updated_team.json', 'w') as file:
    json.dump(team_data, file, indent=2)  # Pretty formatting with indent

# Converting between JSON string and Python objects
json_string = json.dumps(team_data)  # Python dict to JSON string
team_data = json.loads(json_string)  # JSON string to Python dict
```

## Functions to Implement

### 1. `load_team_roster`

This function loads a team roster from a JSON file.

**Tips:**
- Use the `json.load()` function with a file object
- Handle potential JSON parsing errors
- Validate that the loaded data has the expected structure

**Pseudocode:**
```
function load_team_roster(filepath):
    try:
        open the file using a context manager
        load JSON data using json.load()
        
        if the loaded data doesn't have the expected keys (e.g., "team_name", "players"):
            raise ValueError with appropriate message
        
        return the loaded data
    except FileNotFoundError:
        raise appropriate error
    except json.JSONDecodeError:
        raise ValueError indicating invalid JSON format
```

**Example Usage:**
```python
try:
    team = load_team_roster("barcelona_roster.json")
    print(f"Loaded roster for {team['team_name']}")
    print(f"Number of players: {len(team['players'])}")
except Exception as e:
    print(f"Error: {e}")
```

### 2. `save_team_roster`

This function saves a team roster to a JSON file.

**Tips:**
- Use the `json.dump()` function with a file object
- Include proper formatting for readability (indentation)
- Handle file writing errors

**Pseudocode:**
```
function save_team_roster(team_data, filepath):
    try:
        open the file in write mode using a context manager
        write the JSON data using json.dump() with indent=2 for formatting
        return True on success
    except IOError:
        raise appropriate error
```

**Example Usage:**
```python
team_data = {
    "team_name": "Liverpool FC",
    "players": [
        {"name": "Mohamed Salah", "position": "Forward", "number": 11},
        {"name": "Virgil van Dijk", "position": "Defender", "number": 4}
    ]
}
save_team_roster(team_data, "liverpool_roster.json")
```

### 3. `add_player`

This function adds a new player to a team roster.

**Tips:**
- Validate the input player data
- Check for duplicate players
- Add the player to the roster and return the updated roster

**Pseudocode:**
```
function add_player(team_data, player):
    if player doesn't have required fields (name, position):
        raise ValueError indicating missing required fields
    
    for each existing_player in team_data["players"]:
        if existing_player's name matches the new player's name:
            raise ValueError indicating player already exists
    
    add player to team_data["players"] list
    return the updated team_data
```

**Example Usage:**
```python
team = load_team_roster("liverpool_roster.json")
new_player = {"name": "Alisson Becker", "position": "Goalkeeper", "number": 1}
updated_team = add_player(team, new_player)
save_team_roster(updated_team, "liverpool_roster.json")
```

### 4. `find_players_by_position`

This function finds all players in a specific position.

**Tips:**
- Filter the player list based on the position field
- Handle case-insensitive matching for better usability
- Return a list of matching players

**Pseudocode:**
```
function find_players_by_position(team_data, position):
    create an empty list for matching_players
    
    for each player in team_data["players"]:
        if player's position matches the target position (case-insensitive):
            add player to matching_players
    
    return matching_players
```

**Example Usage:**
```python
team = load_team_roster("barcelona_roster.json")
forwards = find_players_by_position(team, "Forward")
print(f"Found {len(forwards)} forwards")
for player in forwards:
    print(f"{player['name']} - #{player.get('number', 'N/A')}")
```

### 5. `convert_to_csv_format`

This function converts a team roster from JSON to CSV format.

**Tips:**
- Determine the headers based on player data fields
- Handle missing fields gracefully
- Return a string in CSV format, including a header row

**Pseudocode:**
```
function convert_to_csv_format(team_data):
    get all possible fields from players (some players might have different fields)
    create a header row with field names
    
    create a list of CSV rows starting with the header
    
    for each player in team_data["players"]:
        create a new row with values for each field
        handle missing fields by using empty strings
        add the row to the list of rows
    
    join the rows with newlines to create a CSV string
    return the CSV string
```

**Example Usage:**
```python
team = load_team_roster("barcelona_roster.json")
csv_data = convert_to_csv_format(team)
with open("barcelona_roster.csv", "w") as file:
    file.write(csv_data)
```

### 6. `merge_team_rosters`

This function merges two team rosters into a single roster.

**Tips:**
- Create a new roster with a combined name
- Add players from both teams, avoiding duplicates
- Handle conflicts (e.g., players with the same name but different details)

**Pseudocode:**
```
function merge_team_rosters(team1_data, team2_data):
    create a new team data structure with:
        team_name: "team1_name + team2_name Combined Roster"
        players: empty list
    
    add all players from team1_data to the new team
    
    for each player in team2_data["players"]:
        check if a player with the same name already exists in the new team
        if not exists:
            add the player to the new team
        else:
            handle the conflict (perhaps by appending team name to player name)
    
    return the merged team data
```

**Example Usage:**
```python
team1 = load_team_roster("barcelona_roster.json")
team2 = load_team_roster("liverpool_roster.json")
merged_team = merge_team_rosters(team1, team2)
save_team_roster(merged_team, "combined_roster.json")
```

## Testing Your Implementation

Run the file with:

```python
python json_handling.py
```

The provided `main()` function will test your implementations with sample data. Make sure all test cases pass without errors.

## Further Exploration

After completing the challenge, consider:

1. How would you extend the player data structure to include statistics like goals, assists, and playing time?

2. Could you implement a function to track roster changes over time, storing a history of additions and removals?

3. How might you convert the team roster to other formats like XML or a database structure?

## Connect to Capstone

For your NCAA soccer analysis capstone, JSON handling will be valuable for:

- Storing and managing complex, nested data structures
- Exchanging data between different components of your system
- Creating configurable systems with JSON-based settings
- Building data APIs that return structured results

These skills will allow you to create flexible data structures that can model the complex relationships in NCAA soccer teams and competitions.