# Challenge 1: Soccer Team Management System

This challenge introduces you to Object-Oriented Programming by creating a system to manage soccer teams, players, and match details.

## Overview

Object-Oriented Programming is the perfect paradigm for modeling real-world entities like soccer teams and players. In this challenge, you'll implement three fundamental classes that form the basis of a soccer team management system.

## Learning Focus

- Creating classes with attributes and methods
- Implementing constructors (`__init__` methods)
- Data validation and encapsulation
- Class interactions and relationships
- Special methods like `__str__`

## Classes to Implement

### 1. `SoccerTeam` Class

This class represents a soccer team with financial and performance tracking.

**Tips:**
- Store the team name, coach, and financial information as attributes
- Implement methods to update the financial state
- Validate inputs (e.g., budget can't be negative)
- Track team statistics like matches played, won, and lost

**Pseudocode:**
```
class SoccerTeam:
    # Constructor
    function __init__(team_name, coach_name, initial_budget=0):
        store team_name as an attribute
        store coach_name as an attribute
        store initial_budget as an attribute (ensure it's not negative)
        initialize matches_played, wins, draws, losses to 0
        initialize goals_scored, goals_conceded to 0
    
    # Method to add funds to budget
    function add_funds(amount):
        if amount is negative:
            raise ValueError
        add amount to current budget
        return the new budget
    
    # Method to spend from budget
    function spend_funds(amount):
        if amount is negative:
            raise ValueError
        if amount is greater than current budget:
            raise ValueError("Insufficient funds")
        subtract amount from current budget
        return the new budget
    
    # Method to get current balance
    function get_balance():
        return the current budget
    
    # Method to update match results
    function record_match_result(goals_for, goals_against):
        increment matches_played
        add goals_for to goals_scored
        add goals_against to goals_conceded
        
        if goals_for > goals_against:
            increment wins
        else if goals_for == goals_against:
            increment draws
        else:
            increment losses
        
        return a dictionary with updated stats
```

**Real-world application:** Soccer teams need to track both financial information (transfer budgets, player salaries) and performance data. This class provides the foundation for a team management system used by coaches and administrators.

### 2. `SoccerField` Class

This class represents a soccer field with specific dimensions and conditions.

**Tips:**
- Store field dimensions and surface type as attributes
- Include methods to assess field conditions
- Calculate areas for different parts of the field
- Include validation for sensible field dimensions

**Pseudocode:**
```
class SoccerField:
    # Constructor
    function __init__(length, width, surface_type="grass"):
        if length or width are not positive:
            raise ValueError
        store length as an attribute
        store width as an attribute
        store surface_type as an attribute
        initialize condition_rating to 100 (perfect condition)
    
    # Method to calculate field area
    function area():
        return length * width
    
    # Method to calculate penalty box area
    function penalty_box_area():
        # Standard penalty box is 16.5m x 40.3m
        penalty_box_width = 40.3
        penalty_box_length = 16.5
        return penalty_box_length * penalty_box_width
    
    # Method to assess if field dimensions are regulation
    function is_regulation_size():
        # FIFA regulation field is between 90-120m length and 45-90m width
        if length is between 90 and 120 AND width is between 45 and 90:
            return True
        return False
    
    # Method to update field condition after weather or use
    function update_condition(weather_impact=-5):
        condition_rating = condition_rating + weather_impact
        if condition_rating < 0:
            condition_rating = 0
        if condition_rating > 100:
            condition_rating = 100
        return condition_rating
```

**Real-world application:** Field conditions impact game strategy and player performance. This class could be used by groundskeepers, match officials, and coaches to assess field playability and plan tactics accordingly.

### 3. `SoccerMatch` Class

This class represents a soccer match with teams, score tracking, and match events.

**Tips:**
- Store home and away teams, the match date, and venue
- Track goals, scorers, cards, and other match events
- Include methods to update the score and record events
- Implement special `__str__` method to display match result

**Pseudocode:**
```
class SoccerMatch:
    # Constructor
    function __init__(home_team, away_team, match_date, venue):
        store home_team as an attribute
        store away_team as an attribute
        store match_date as an attribute
        store venue as an attribute
        initialize home_goals, away_goals to 0
        initialize match_events to an empty list
        initialize is_completed to False
    
    # Method to add a goal
    function add_goal(team, player_name, minute):
        create a goal event dictionary with team, player_name, minute, event_type="goal"
        add this dictionary to match_events
        
        if team is home_team:
            increment home_goals
        else if team is away_team:
            increment away_goals
        
        return current score as tuple (home_goals, away_goals)
    
    # Method to record a card
    function add_card(team, player_name, card_type, minute):
        if card_type is not "yellow" or "red":
            raise ValueError
        
        create a card event dictionary with team, player_name, card_type, minute, event_type="card"
        add this dictionary to match_events
        
        return the updated match_events list
    
    # Method to complete the match and update team stats
    function complete_match():
        if is_completed:
            raise ValueError("Match already completed")
        
        set is_completed to True
        
        # Update home team's stats
        call home_team.record_match_result(home_goals, away_goals)
        
        # Update away team's stats
        call away_team.record_match_result(away_goals, home_goals)
        
        return a dictionary with the match result
    
    # String representation of the match
    function __str__():
        if is_completed:
            return formatted string with teams and score
        else:
            return formatted string indicating match is scheduled
```

**Real-world application:** Match tracking systems are essential for sports leagues, providing historical data, statistics for analysis, and information for fans. This class could be part of a match management system used by league officials and media.

## Testing Your Implementation

The provided `main()` function tests your implementation with sample usage. Run the file to see if your classes behave as expected:

```python
python oop_basics.py
```

Make sure all the tests in the main function pass without errors.

## Further Exploration

After completing the challenge, consider:

1. How would you extend `SoccerTeam` to include a roster of players?

2. Could you add methods to `SoccerField` to track field wear patterns based on player movement?

3. How might you enhance `SoccerMatch` to include a time-based simulation of a match?

## Connect to Capstone

These classes represent fundamental entities you'll need in your NCAA soccer analysis capstone. As you work through this challenge, think about:

- What additional attributes and methods would make these classes more useful for analytics?
- How might you structure the relationships between teams, players, and matches?
- What kinds of statistics would be most important to track for NCAA soccer analysis?

Understanding how to model soccer entities as objects is the first step toward building your comprehensive NCAA soccer analysis system!