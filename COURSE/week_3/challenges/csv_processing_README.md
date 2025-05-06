# Challenge 2: Player Statistics Parser

This challenge focuses on working with CSV files containing soccer player statistics.

## Overview

CSV (Comma-Separated Values) files are commonly used in sports analytics to store structured data like player statistics. In this challenge, you'll implement functions to read, process, and analyze soccer player data from CSV files.

## Learning Focus

- Reading and parsing CSV files
- Data extraction and transformation
- Working with tabular data
- Filtering and aggregating statistics
- Error handling with CSV files

## Key Concepts Explained

### CSV Processing Basics

**CSV Format**:
CSV files store tabular data as text with values separated by commas. Each line is a row, and columns are separated by commas:
```
Name,Team,Position,Goals,Assists
Messi,Inter Miami,Forward,12,8
Ronaldo,Al-Nassr,Forward,15,5
```

**Reading CSV Using Python's Built-in csv Module**:
```python
import csv

# Reading CSV with csv module
with open('players.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    for row in reader:     # Read each data row
        name = row[0]
        team = row[1]
        # Process data...
```

**Reading CSV Using pandas Library**:
```python
import pandas as pd

# Reading CSV with pandas
df = pd.read_csv('players.csv')
# Access columns by name
names = df['Name']
goals = df['Goals']
# Filter data
forwards = df[df['Position'] == 'Forward']
```

## Functions to Implement

### 1. `read_player_stats_basic`

This function reads player statistics from a CSV file using the built-in csv module.

**Tips:**
- Use the csv module's reader function
- Handle potential file format errors
- Convert numeric values to the appropriate data types

**Pseudocode:**
```
function read_player_stats_basic(filepath):
    try:
        create an empty list for players
        
        open the file using a context manager
        create a csv reader object
        read the header row
        
        for each row in the reader:
            create a dictionary for the player
            map each header column to its corresponding value
            convert numeric values to appropriate types
            add the player dictionary to the players list
        
        return the list of players
    except FileNotFoundError:
        raise appropriate error
    except csv.Error:
        raise appropriate error
```

**Example Usage:**
```python
players = read_player_stats_basic("player_stats.csv")
for player in players[:3]:  # Print first 3 players
    print(f"{player['Name']} - {player['Team']} - {player['Goals']} goals")
```

### 2. `read_player_stats_pandas`

This function reads player statistics from a CSV file using the pandas library.

**Tips:**
- Use pandas' read_csv function
- Convert the DataFrame to a list of dictionaries for consistency
- Handle potential pandas-specific errors

**Pseudocode:**
```
function read_player_stats_pandas(filepath):
    try:
        import pandas as pd
        
        read the CSV file into a DataFrame
        convert the DataFrame to a list of dictionaries
        return the list of players
    except FileNotFoundError:
        raise appropriate error
    except pd.errors.EmptyDataError:
        raise appropriate error
    except pd.errors.ParserError:
        raise appropriate error
```

**Example Usage:**
```python
players = read_player_stats_pandas("player_stats.csv")
for player in players[:3]:  # Print first 3 players
    print(f"{player['Name']} - {player['Team']} - {player['Goals']} goals")
```

### 3. `find_top_scorer`

This function finds the player with the most goals from a list of players.

**Tips:**
- Iterate through the player list to find the maximum value
- Handle cases where multiple players have the same maximum
- Return the player's full record, not just their name

**Pseudocode:**
```
function find_top_scorer(players):
    if players is empty:
        return None
    
    set top_scorer to the first player
    set max_goals to the first player's goals
    
    for each player in players (starting from the second):
        if player's goals > max_goals:
            update max_goals
            update top_scorer to current player
    
    return top_scorer
```

**Example Usage:**
```python
players = read_player_stats_basic("player_stats.csv")
top_scorer = find_top_scorer(players)
print(f"Top scorer: {top_scorer['Name']} with {top_scorer['Goals']} goals")
```

### 4. `filter_by_team`

This function filters the player list to include only players from a specific team.

**Tips:**
- Create a new list with only the matching players
- Make the comparison case-insensitive for better usability
- Return an empty list if no players match

**Pseudocode:**
```
function filter_by_team(players, team_name):
    create an empty list for team_players
    
    for each player in players:
        if player's team equals team_name (case-insensitive comparison):
            add player to team_players
    
    return team_players
```

**Example Usage:**
```python
players = read_player_stats_basic("player_stats.csv")
barcelona_players = filter_by_team(players, "FC Barcelona")
print(f"Found {len(barcelona_players)} players from FC Barcelona")
```

### 5. `calculate_team_stats`

This function calculates aggregate statistics for each team.

**Tips:**
- Group players by team
- Calculate totals and averages for each statistic
- Return a dictionary with team names as keys

**Pseudocode:**
```
function calculate_team_stats(players):
    create an empty dictionary for team_stats
    
    for each player in players:
        get the player's team
        
        if the team is not in team_stats:
            initialize team entry with zero counts and empty player list
        
        increment team's total goals, assists, etc.
        add player to team's player list
    
    for each team in team_stats:
        calculate average goals per player
        calculate average assists per player
        calculate other aggregate statistics
    
    return team_stats
```

**Example Usage:**
```python
players = read_player_stats_basic("player_stats.csv")
team_stats = calculate_team_stats(players)
for team, stats in team_stats.items():
    print(f"{team}: {stats['total_goals']} goals, {stats['player_count']} players")
```

### 6. `export_team_stats`

This function exports team statistics to a new CSV file.

**Tips:**
- Create a new CSV with appropriate headers
- Format the data correctly for CSV output
- Use the csv module to handle escaping and formatting

**Pseudocode:**
```
function export_team_stats(team_stats, output_filepath):
    try:
        open the output file in write mode
        create a csv writer object
        
        write header row with column names
        
        for each team, stats in team_stats.items():
            create a row with team name and statistics
            write the row to the CSV
        
        return True on success
    except IOError:
        raise appropriate error
```

**Example Usage:**
```python
players = read_player_stats_basic("player_stats.csv")
team_stats = calculate_team_stats(players)
export_team_stats(team_stats, "team_summary.csv")
```

## Testing Your Implementation

Run the file with:

```python
python csv_processing.py
```

The provided `main()` function will test your implementations with sample data. Make sure all test cases pass without errors.

## Further Exploration

After completing the challenge, consider:

1. How would you extend the player statistics to include more advanced metrics like expected goals or pass completion rate?

2. Could you implement a function to perform positional analysis, comparing players by position?

3. How might you create a visualization of team performance based on the CSV data?

## Connect to Capstone

For your NCAA soccer analysis capstone, CSV processing will be crucial for:

- Importing player and team statistics from NCAA data sources
- Transforming raw data into analysis-ready formats
- Calculating derived metrics and key performance indicators
- Exporting processed data for visualization and reporting

These skills will form the core of your data pipeline, allowing you to transform raw NCAA soccer data into valuable insights for your analysis system.