# Challenge 2: Soccer Data Integration

This challenge focuses on combining and transforming data from multiple soccer API sources.

## Overview

In real-world soccer analytics, valuable insights often come from combining data from multiple sources. This challenge will teach you how to integrate data from different APIs and transform it into unified, useful information.

## Learning Focus

- Making requests to multiple API endpoints
- Combining related data from different sources
- Transforming and normalizing data structures
- Handling different API response formats
- Creating composite data views

## Key Concepts Explained

### Multi-API Integration

```
┌─────────────┐
│ Team API    │
│  Response   │──┐
└─────────────┘  │   ┌──────────────┐      ┌────────────┐
                 ├──>│  Your Code   │─────>│ Integrated │
┌─────────────┐  │   │  (Combine &  │      │    Data    │
│ Player API  │──┘   │  Transform)  │      └────────────┘
│  Response   │      └──────────────┘
└─────────────┘
```

### Data Transformation Process

```
1. Fetch data from multiple APIs
2. Extract relevant fields from each response
3. Transform to consistent format (field names, types)
4. Merge related data (e.g., add player info to teams)
5. Create new derived data (e.g., statistics)
```

## Functions to Implement

For this challenge, we'll use TheSportsDB for team data and player information, but will need to combine and transform the data in useful ways.

### 1. `get_team_with_players`

This function gets comprehensive team data including all players with detailed information.

**Tips:**
- Make requests to both team and player endpoints
- Combine the data into a unified team object
- Handle cases where either request fails

**Pseudocode:**
```
function get_team_with_players(team_name):
    # Get basic team information
    team_endpoint = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    team_data = make API request to team_endpoint with params={"t": team_name}
    
    if team_data contains error or no team found:
        return the error
    
    team_id = extract team ID from team_data
    basic_team_info = extract and format basic team info
    
    # Get players for this team
    players_endpoint = "https://www.thesportsdb.com/api/v1/json/3/lookup_all_players.php"
    players_data = make API request to players_endpoint with params={"id": team_id}
    
    if players_data contains error:
        set players to empty list
    else:
        extract and format player information
    
    # Combine team and players data
    create a comprehensive team object with:
        - All team information
        - Array of player objects
        - Summary statistics (roster size, positions count, etc.)
    
    return the comprehensive team object
```

**Example Usage:**
```python
team = get_team_with_players("Arsenal")
if "error" not in team:
    print(f"Team: {team['name']}")
    print(f"Number of players: {len(team['players'])}")
    print(f"Forwards: {team['positions_count']['Forward']}")
```

### 2. `combine_player_stats`

This function combines stats for a specific player from multiple sources.

**Tips:**
- Create a complete profile by merging player data from multiple endpoints
- Handle missing data gracefully
- Create a normalized structure for the combined data

**Pseudocode:**
```
function combine_player_stats(player_name):
    # Search for the player
    search_endpoint = "https://www.thesportsdb.com/api/v1/json/3/searchplayers.php"
    search_results = make API request to search_endpoint with params={"p": player_name}
    
    if search_results contains error or no player found:
        return the error
    
    player_id = extract player ID from first search result
    basic_player_info = extract basic player information
    
    # Get detailed player information
    player_details_endpoint = "https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php"
    player_details = make API request to player_details_endpoint with params={"id": player_id}
    
    if player_details contains error:
        use only basic information
    else:
        extract detailed player information
    
    # Combine all information into a comprehensive player profile
    create player profile with:
        - Basic information (name, team, position)
        - Detailed information (height, weight, birth date, etc.)
        - Team information
        - Any available statistics
    
    return the player profile
```

**Example Usage:**
```python
player = combine_player_stats("Kevin De Bruyne")
if "error" not in player:
    print(f"Player: {player['name']}")
    print(f"Team: {player['team']}")
    print(f"Position: {player['position']}")
    print(f"Nationality: {player['nationality']}")
```

### 3. `search_across_leagues`

This function searches for teams across multiple leagues and combines the results.

**Tips:**
- Make multiple requests to search in different leagues
- Combine and deduplicate the results
- Format the results consistently

**Pseudocode:**
```
function search_across_leagues(search_term, leagues=["English Premier League", "La Liga", "Bundesliga"]):
    all_results = []
    
    for each league in leagues:
        league_endpoint = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php"
        league_results = make API request to league_endpoint with params={"l": league, "s": search_term}
        
        if league_results doesn't contain error and has teams:
            extract and format team information
            add teams to all_results
    
    # Deduplicate results (teams might appear in multiple searches)
    create a dictionary to uniquely identify teams by ID
    
    combine_results = []
    for each team in all_results:
        if team ID is not already in our results:
            add team to combined_results
    
    return combined_results
```

**Example Usage:**
```python
teams = search_across_leagues("United")
print(f"Found {len(teams)} teams with 'United' in their name")
for team in teams:
    print(f"{team['name']} - {team['league']}")
```

### 4. `create_team_comparison`

This function creates a side-by-side comparison of two soccer teams.

**Tips:**
- Get comprehensive data for both teams
- Structure the data to highlight similarities and differences
- Include statistical comparisons where possible

**Pseudocode:**
```
function create_team_comparison(team1_name, team2_name):
    # Get data for both teams with players
    team1_data = get_team_with_players(team1_name)
    team2_data = get_team_with_players(team2_name)
    
    if either team1_data or team2_data contains error:
        return the error
    
    # Create comparison object
    comparison = {
        "teams": [
            {
                "name": team1_data["name"],
                "country": team1_data["country"],
                "league": team1_data["league"],
                "founded": team1_data["year_formed"],
                "players_count": len(team1_data["players"])
            },
            {
                "name": team2_data["name"],
                "country": team2_data["country"],
                "league": team2_data["league"],
                "founded": team2_data["year_formed"],
                "players_count": len(team2_data["players"])
            }
        ],
        "positions_comparison": {
            # Count players by position for each team
            "team1": count of players by position for team1,
            "team2": count of players by position for team2
        },
        "common_players": find players who have played for both teams (if any)
    }
    
    return comparison
```

**Example Usage:**
```python
comparison = create_team_comparison("Barcelona", "Real Madrid")
if "error" not in comparison:
    print("Team Comparison:")
    print(f"{comparison['teams'][0]['name']} vs {comparison['teams'][1]['name']}")
    print(f"Players: {comparison['teams'][0]['players_count']} vs {comparison['teams'][1]['players_count']}")
    
    print("\nPositions Comparison:")
    for position in comparison['positions_comparison']['team1']:
        count1 = comparison['positions_comparison']['team1'][position]
        count2 = comparison['positions_comparison']['team2'].get(position, 0)
        print(f"{position}: {count1} vs {count2}")
```

### 5. `get_league_standings`

This function gets the current standings for a soccer league.

**Tips:**
- Make a request to get league teams
- For each team, fetch additional statistics if available
- Create a sorted standings table

**Pseudocode:**
```
function get_league_standings(league_name):
    # Find the league ID
    league_endpoint = "https://www.thesportsdb.com/api/v1/json/3/search_all_leagues.php"
    league_data = make API request to league_endpoint with params={"l": league_name}
    
    if league_data contains error or no league found:
        return the error
    
    league_id = extract league ID from league_data
    
    # Get teams in this league
    teams_endpoint = "https://www.thesportsdb.com/api/v1/json/3/lookup_all_teams.php"
    teams_data = make API request to teams_endpoint with params={"id": league_id}
    
    if teams_data contains error or no teams found:
        return the error
    
    # For a true standings table, we'd need more data than is available in the free API
    # So we'll create a simulated standings table for this example
    teams = extract teams from teams_data
    
    # Create a simulated standings table
    standings = []
    for each team in teams:
        create a team entry with:
            - name: team name
            - position: (index + 1)
            - played: random number between 30-38 (for example)
            - won: random number less than played
            - drawn: random number less than (played - won)
            - lost: played - won - drawn
            - points: won * 3 + drawn
        
        add team entry to standings
    
    # Sort by points (descending)
    sort standings by points in descending order
    
    return standings
```

**Example Usage:**
```python
standings = get_league_standings("English Premier League")
if isinstance(standings, list):
    print("League Standings:")
    for team in standings[:5]:  # Top 5 teams
        print(f"{team['position']}. {team['name']} - {team['points']} pts")
```

## API Limitations

The free tier of TheSportsDB API has limitations on the data available. For a real-world application, you might:

1. Use a paid sports data API with more comprehensive data
2. Combine data from multiple providers
3. Create a database to store and combine data over time
4. Implement web scraping for data not available via APIs

For this challenge, focus on understanding the concept of data integration rather than building a complete system.

## Testing Your Implementation

Run the file with:

```python
python api_integration_advanced.py
```

The provided `main()` function will test your implementations with sample API calls. Due to API limitations, not all features may work perfectly, but you should be able to demonstrate the core integration concepts.

## Further Exploration

After completing the challenge, consider:

1. How would you implement persistent storage to avoid redundant API calls?

2. Could you create a more sophisticated player comparison that includes statistical analysis?

3. How might you visualize the team comparison data?

## Connect to Capstone

For your NCAA soccer analysis capstone, data integration will be essential for:

- Combining player statistics from different sources
- Creating comprehensive team profiles
- Generating match previews with combined historical data
- Building comparison tools for teams and players

These skills will allow you to create a richer, more valuable NCAA soccer analysis system by leveraging multiple data sources.