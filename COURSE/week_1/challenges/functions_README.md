# Challenge 4: Soccer Analytics Functions

This challenge focuses on creating powerful, reusable functions for soccer data analysis that form the foundation of your analytics toolkit.

## Overview

Well-designed functions are the building blocks of any soccer analytics system. In this challenge, you'll implement five functions that perform common soccer analytics tasks with different levels of complexity.

## Learning Focus

- Function definition and parameters
- Default parameter values
- Variable-length arguments
- Return values
- Complex data transformations
- Function composition

## Tips for Each Function

### 1. `calculate_win_percentage`

This function calculates a team's win percentage based on match results.

**Tips:**
- Calculate the total number of matches first (wins + draws + losses)
- Check for division by zero (if no matches have been played)
- Remember that draws count as half a win in the formula
- Multiply by 100 to convert to a percentage
- Return the result as a float

**Pseudocode:**
```
function calculate_win_percentage(wins, draws, losses):
    total_matches = wins + draws + losses
    
    if total_matches equals 0:
        return 0.0
    
    win_percentage = (wins + (0.5 * draws)) / total_matches * 100
    
    return win_percentage
```

**Real-world application:** Win percentage is a fundamental metric for evaluating team performance, allowing for fair comparison between teams that have played different numbers of matches.

### 2. `format_player_info`

This function creates a standardized string representation for player information.

**Tips:**
- Use string formatting or f-strings (Python 3.6+)
- Handle the optional parameters (team and jersey_number) correctly
- Test with different combinations of provided and omitted optional parameters
- Make sure your output matches the expected format exactly

**Pseudocode:**
```
function format_player_info(first_name, last_name, position, team=None, jersey_number=None):
    set full_name to first_name + " " + last_name
    
    if jersey_number is provided:
        set position_info to "(position, #jersey_number)"
    else:
        set position_info to "(position)"
    
    if team is provided:
        set result to full_name + " " + position_info + " - " + team
    else:
        set result to full_name + " " + position_info
    
    return result
```

**Real-world application:** Standardized player information formatting is essential for creating consistent player profiles in reports, dashboards, and databases.

### 3. `calculate_points`

This function uses variable-length arguments to calculate total points from a series of match results.

**Tips:**
- The `*match_results` parameter allows accepting any number of arguments
- Create a points dictionary mapping result codes to points values
- Use a loop or sum with a generator expression to calculate the total
- Handle invalid result codes gracefully

**Pseudocode:**
```
function calculate_points(*match_results):
    create a dictionary mapping:
        'W' to 3 points
        'D' to 1 point
        'L' to 0 points
    
    set total_points to 0
    
    for each result in match_results:
        if result is in the points dictionary:
            add the points for that result to total_points
    
    return total_points
```

**Real-world application:** Points calculation is central to league standings and performance evaluation throughout a season.

### 4. `analyze_match_stats`

This function performs a comprehensive comparison of team and opponent statistics.

**Tips:**
- Create a dictionary to store the analysis results
- Calculate each metric as specified in the requirements
- Use list comprehensions for identifying strengths and weaknesses
- Round percentage values appropriately for readability
- Make sure to compare all relevant statistics between the teams

**Pseudocode:**
```
function analyze_match_stats(team_stats, opponent_stats):
    create an empty dictionary called analysis
    
    # Calculate possession difference
    analysis['possession_difference'] = team_stats['possession'] - opponent_stats['possession']
    
    # Calculate shots accuracy
    if team_stats['shots'] > 0:
        analysis['shots_accuracy'] = (team_stats['shots_on_target'] / team_stats['shots']) * 100
    else:
        analysis['shots_accuracy'] = 0
    
    # Calculate passing accuracy
    if team_stats['passes'] > 0:
        analysis['passing_accuracy'] = (team_stats['passes_completed'] / team_stats['passes']) * 100
    else:
        analysis['passing_accuracy'] = 0
    
    # Identify strengths and weaknesses
    set analysis['strengths'] to an empty list
    set analysis['weaknesses'] to an empty list
    
    for each stat in team_stats:
        if stat is in opponent_stats:
            if team_stats[stat] > opponent_stats[stat]:
                add stat to analysis['strengths']
            elif team_stats[stat] < opponent_stats[stat]:
                add stat to analysis['weaknesses']
    
    # Special handling for fouls (lower is better)
    if 'fouls' in team_stats and 'fouls' in opponent_stats:
        if team_stats['fouls'] < opponent_stats['fouls']:
            if 'fouls' not in analysis['strengths']:
                add 'fouls' to analysis['strengths']
        else if team_stats['fouls'] > opponent_stats['fouls']:
            if 'fouls' not in analysis['weaknesses']:
                add 'fouls' to analysis['weaknesses']
    
    return analysis
```

**Real-world application:** Post-match analysis helps coaches identify areas of strength and weakness to inform training focus and tactical adjustments.

### 5. `generate_league_table`

This function creates a fully-formed league standings table from match results.

**Tips:**
- Create a dictionary to store each team's accumulating statistics
- Initialize all stats for each team (played, won, drawn, lost, points)
- Process each team's results to update their statistics
- Convert the dictionary to a list of dictionaries for the final output
- Sort the list by points in descending order
- Use the `sorted()` function with a key function or `itemgetter`

**Pseudocode:**
```
function generate_league_table(team_results):
    create an empty dictionary called table
    
    # Initialize stats for each team
    for each team in team_results:
        table[team] = {
            'team': team,
            'played': length of team_results[team],
            'won': count of 'W' in team_results[team],
            'drawn': count of 'D' in team_results[team],
            'lost': count of 'L' in team_results[team],
            'points': 0
        }
        
        # Calculate points
        for each result in team_results[team]:
            if result equals 'W':
                add 3 to table[team]['points']
            else if result equals 'D':
                add 1 to table[team]['points']
    
    # Convert to a list
    convert table dictionary to a list of values (each value is a team's stats dictionary)
    
    # Sort by points in descending order
    sort the list by the 'points' key in descending order
    
    return the sorted list
```

**Real-world application:** League tables are the primary way to visualize team performance in soccer leagues and are essential for understanding competitive standing.

## Testing Your Code

Run the file by executing:

```python
python functions.py
```

If your implementations are correct, you should see output that matches the expected results in the docstrings.

## Further Exploration

After completing the challenge, consider:

1. How could you enhance `analyze_match_stats` to provide specific tactical recommendations based on the analysis?

2. Could you extend `generate_league_table` to include additional tie-breaking criteria like goal difference or head-to-head results?

3. What other soccer analytics functions would complement this set to provide a more complete analytical toolkit?

## Connect to Capstone

These functions represent core analytical capabilities you'll need for your NCAA soccer analysis capstone. As you work through this challenge, think about:

- What are the key statistics and calculations you'll need to implement?
- How will you structure your functions to be modular and reusable?
- What output formats will be most useful for your analysis and visualization?

Developing robust, well-structured functions now will give you a strong foundation for your capstone project!