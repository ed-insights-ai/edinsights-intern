# Challenge 4: Soccer Player Analytics System

This challenge focuses on designing a comprehensive object-oriented system for tracking and analyzing soccer player performance.

## Overview

Professional soccer teams rely on sophisticated analytics systems to evaluate player performance, identify strengths and weaknesses, and make data-driven decisions. In this challenge, you'll implement a soccer player analytics system that tracks various statistics and calculates performance metrics.

## Learning Focus

- Designing complete class structures for real-world applications
- Implementing multiple interacting classes
- Working with complex data and calculations
- Creating reusable and extensible OOP code
- Applying domain-specific knowledge to software design

## Classes to Implement

### 1. `SoccerPlayer` Class

This class is the core of the analytics system, representing an individual player and their statistics.

**Tips:**
- Store player identification information and basic attributes
- Maintain various statistical categories for performance tracking
- Implement methods for updating statistics
- Calculate derived metrics from the raw statistics

**Pseudocode:**
```
class SoccerPlayer:
    # Constructor
    function __init__(player_id, first_name, last_name, position, team):
        store player_id, first_name, last_name, position, team as attributes
        
        # Initialize all statistics to zero
        initialize games_played, minutes, goals, assists to 0
        initialize shots, shots_on_goal to 0
        initialize yellow_cards, red_cards to 0
        initialize fouls_committed, fouls_suffered to 0
    
    # Return the player's full name
    function full_name():
        return first_name + " " + last_name
    
    # Update player statistics with new game data
    function update_stats(games=0, minutes=0, goals=0, assists=0, shots=0, 
                         shots_on_goal=0, yellow_cards=0, red_cards=0, 
                         fouls_committed=0, fouls_suffered=0):
        add each parameter value to the corresponding attribute
        
        return dictionary containing all updated statistics
    
    # Calculate goals per 90 minutes played
    function goals_per_90():
        if minutes equals 0:
            return 0
        
        return (goals / minutes) * 90
    
    # Calculate assists per 90 minutes played
    function assists_per_90():
        if minutes equals 0:
            return 0
        
        return (assists / minutes) * 90
    
    # Calculate total goal contributions (goals + assists)
    function goal_contributions():
        return goals + assists
    
    # Calculate shot accuracy percentage
    function shot_accuracy():
        if shots equals 0:
            return 0
        
        return (shots_on_goal / shots) * 100
    
    # Calculate goal conversion rate percentage
    function conversion_rate():
        if shots equals 0:
            return 0
        
        return (goals / shots) * 100
    
    # Calculate cards per game ratio
    function card_ratio():
        if games_played equals 0:
            return 0
        
        total_cards = yellow_cards + red_cards
        return total_cards / games_played
    
    # Calculate ratio of fouls committed to fouls suffered
    function fouls_ratio():
        if fouls_suffered equals 0:
            return 0
        
        return fouls_committed / fouls_suffered
    
    # Calculate an overall efficiency score based on position
    function efficiency_score():
        if games_played equals 0:
            return 0
        
        if position equals "F" (Forward):
            # Forwards prioritize goals, conversion rate, shot accuracy
            return calculate forward efficiency
        else if position equals "MF" (Midfielder):
            # Midfielders prioritize assists, goals, fouls ratio
            return calculate midfielder efficiency
        else if position equals "D" (Defender):
            # Defenders prioritize fouls ratio, card ratio
            return calculate defender efficiency
        else if position equals "GK" (Goalkeeper):
            # Goalkeepers have a different rating system entirely
            return minutes / (games_played * 90) * 100
    
    # String representation of the player
    function __str__():
        return formatted string with name, position, team, and key stats
```

### 2. `Team` Class

This class represents a soccer team composed of multiple players and provides team-level analytics.

**Tips:**
- Manage a collection of SoccerPlayer objects
- Implement methods for team-level analytics
- Support adding and removing players from the roster
- Find top performers in different statistical categories

**Pseudocode:**
```
class Team:
    # Constructor
    function __init__(name):
        store name as attribute
        initialize players as empty list
    
    # Add a player to the team
    function add_player(player):
        if player's team name doesn't match this team's name:
            raise ValueError
        
        if player already exists in players (check by ID):
            raise ValueError
        
        add player to players list
        return count of players
    
    # Remove a player from the team
    function remove_player(player_id):
        find player with matching player_id
        
        if player not found:
            raise ValueError
        
        remove player from players list
        return the removed player
    
    # Get a specific player by ID
    function get_player(player_id):
        find player with matching player_id
        
        if player found:
            return player
        else:
            return None
    
    # Calculate team-level statistics
    function team_stats():
        create a dictionary for team statistics
        
        calculate total goals, assists, shots, etc. across all players
        calculate averages per player
        calculate team-level derived metrics
        
        return the statistics dictionary
    
    # Find the best goal scorer on the team
    function best_scorer():
        if no players:
            return None
        
        find player with maximum goals
        return that player
    
    # Find the best assistant on the team
    function best_assistant():
        if no players:
            return None
        
        find player with maximum assists
        return that player
    
    # Find the most efficient player on the team
    function most_efficient_player():
        if no players:
            return None
        
        find player with maximum efficiency_score()
        return that player
```

## Testing Your Implementation

The provided `main()` function in the starter code tests your implementation with sample data. Run the file to check your classes:

```python
python soccer_player.py
```

The output should display player statistics and team analytics that match the expected values.

## Extending Your Implementation

After completing the basic requirements, consider adding these enhancements:

1. **Position-Specific Classes**: Create subclasses for each position (Forward, Midfielder, Defender, Goalkeeper) with specialized metrics.

2. **Historical Tracking**: Add functionality to track statistics over time or by game.

3. **Comparison Methods**: Implement methods to compare players directly, possibly with a `PlayerComparison` class.

4. **Advanced Metrics**: Add more sophisticated analytics like expected goals (xG), progressive passes, or defensive actions.

## Connect to Capstone

This challenge directly relates to your NCAA soccer analysis capstone. Consider:

- How can this analytics system be adapted for college soccer data?
- What NCAA-specific metrics would you add?
- How might this player tracking feed into a larger system for team and league analysis?
- What visualizations could be generated from these analytics?

The player analytics system you build here forms the foundation for the statistical analysis components of your capstone project!