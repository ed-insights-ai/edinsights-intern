#!/usr/bin/env -S uv run --script
# /// script
# dependencies = []
# ///

"""
Function Workshop: Soccer Analytics
----------------------------------
Complete the following functions according to their docstrings.
This exercise focuses on creating and using functions in Python
while introducing you to soccer analytics concepts.
"""

def calculate_win_percentage(wins, draws, losses):
    """
    Calculate the win percentage for a soccer team.
    
    The formula is: (wins + draws * 0.5) / total_matches * 100
    
    Args:
        wins (int): Number of wins
        draws (int): Number of draws
        losses (int): Number of losses
        
    Returns:
        float: The win percentage (0-100)
        
    Example:
        >>> calculate_win_percentage(10, 5, 5)
        62.5  # (10 + 5*0.5) / 20 * 100
    """
    return (wins + draws * 0.5) / (wins + draws + losses) * 100
    

def format_player_info(first_name, last_name, position, team=None, jersey_number=None):
    """
    Format player information into a standard string representation.
    
    Args:
        first_name (str): Player's first name
        last_name (str): Player's last name
        position (str): Player's position
        team (str, optional): Player's team. Defaults to None.
        jersey_number (int, optional): Player's jersey number. Defaults to None.
        
    Returns:
        str: Formatted player information
        
    Example:
        >>> format_player_info("Lionel", "Messi", "Forward", "Inter Miami", 10)
        "Lionel Messi (Forward, #10) - Inter Miami"
        >>> format_player_info("Cristiano", "Ronaldo", "Forward")
        "Cristiano Ronaldo (Forward)"
    """
    info = f"{first_name} {last_name} ({position}"
    if jersey_number:
        info += f", #{jersey_number}"
    info += ")"
    if team:
        info += f" - {team}"
    return info
    

def calculate_points(*match_results):
    """
    Calculate total points earned from a series of match results.

    In soccer, a win is worth 3 points, a draw is worth 1 point,
    and a loss is worth 0 points.

    Args:
        *match_results: Variable number of match results ('W', 'D', or 'L')

    Returns:
        int: Total points earned

    Example:
        >>> calculate_points('W', 'D', 'W', 'L', 'D')
        8  # 3 + 1 + 3 + 0 + 1
    """
    points = 0
    for result in match_results:
        if result == 'W':
            points += 3
        elif result == 'D':
            points += 1
        # Loss ('L') adds 0 points, so no need to handle explicitly
    return points

def analyze_match_stats(team_stats, opponent_stats):
    """
    Analyze match statistics and determine areas of strength and weakness.
    
    Args:
        team_stats (dict): Dictionary containing team statistics
        opponent_stats (dict): Dictionary containing opponent statistics
        
    Returns:
        dict: Dictionary containing analysis results with the following keys:
            - 'possession_difference': Difference in possession percentage
            - 'shots_accuracy': Team's shots on target as a percentage of total shots
            - 'passing_accuracy': Team's completed passes as a percentage of total passes
            - 'strengths': List of areas where team outperformed opponent
            - 'weaknesses': List of areas where opponent outperformed team
    """
    possession_difference = team_stats['possession'] - opponent_stats['possession']
    shots_accuracy = round((team_stats['shots_on_target'] / team_stats['shots']) * 100, 2)
    passing_accuracy = round((team_stats['passes_completed'] / team_stats['passes']) * 100, 2)

    strengths = []
    weaknesses = []

    for key in team_stats:
        if key in opponent_stats and key != 'fouls':  # Exclude 'fouls' from strengths/weaknesses
            if team_stats[key] > opponent_stats[key]:
                strengths.append(key)
            elif team_stats[key] < opponent_stats[key]:
                weaknesses.append(key)

    if team_stats['fouls'] < opponent_stats['fouls']:
        strengths.append('fouls')
    elif team_stats['fouls'] > opponent_stats['fouls']:
        weaknesses.append('fouls')

    return {
        'possession_difference': possession_difference,
        'shots_accuracy': shots_accuracy,
        'passing_accuracy': passing_accuracy,
        'strengths': strengths,
        'weaknesses': weaknesses
    }

def generate_league_table(team_results):
    """
    Generate a league table (standings) from team results.
    
    Args:
        team_results (dict): Dictionary where keys are team names and values are lists
                             of match results ('W', 'D', or 'L')
        
    Returns:
        list: List of dictionaries, each containing the following keys:
            - 'team': Team name
            - 'played': Number of matches played
            - 'won': Number of matches won
            - 'drawn': Number of matches drawn
            - 'lost': Number of matches lost
            - 'points': Total points earned
        The list should be sorted by points in descending order.
        
    Example:
        >>> team_results = {
        ...     'Team A': ['W', 'W', 'D', 'L', 'W'],
        ...     'Team B': ['L', 'W', 'D', 'W', 'D'],
        ...     'Team C': ['D', 'L', 'L', 'D', 'L']
        ... }
        >>> generate_league_table(team_results)
        [
            {'team': 'Team A', 'played': 5, 'won': 3, 'drawn': 1, 'lost': 1, 'points': 10},
            {'team': 'Team B', 'played': 5, 'won': 2, 'drawn': 2, 'lost': 1, 'points': 8},
            {'team': 'Team C', 'played': 5, 'won': 0, 'drawn': 2, 'lost': 3, 'points': 2}
        ]
    """
    league_table = []

    for team, results in team_results.items():
        played = len(results)
        won = results.count('W')
        drawn = results.count('D')
        lost = results.count('L')
        points = won * 3 + drawn * 1

        league_table.append({
            'team': team,
            'played': played,
            'won': won,
            'drawn': drawn,
            'lost': lost,
            'points': points
        })

    league_table.sort(key=lambda x: x['points'], reverse=True)
    return league_table

def main():
    """Run some examples to test your functions."""
    print("Testing calculate_win_percentage...")
    print(f"calculate_win_percentage(10, 5, 5) = {calculate_win_percentage(10, 5, 5)}")
    
    print("\nTesting format_player_info...")
    print(f"format_player_info('Lionel', 'Messi', 'Forward', 'Inter Miami', 10) = {format_player_info('Lionel', 'Messi', 'Forward', 'Inter Miami', 10)}")
    print(f"format_player_info('Cristiano', 'Ronaldo', 'Forward') = {format_player_info('Cristiano', 'Ronaldo', 'Forward')}")
    
    print("\nTesting calculate_points...")
    print(f"calculate_points('W', 'D', 'W', 'L', 'D') = {calculate_points('W', 'D', 'W', 'L', 'D')}")
    
    print("\nTesting analyze_match_stats...")
    team_stats = {
        'possession': 60,
        'shots': 15,
        'shots_on_target': 7,
        'passes': 500,
        'passes_completed': 450,
        'corners': 7,
        'fouls': 10
    }
    opponent_stats = {
        'possession': 40,
        'shots': 10,
        'shots_on_target': 3,
        'passes': 300,
        'passes_completed': 250,
        'corners': 3,
        'fouls': 15
    }
    print(f"analyze_match_stats(team_stats, opponent_stats) = {analyze_match_stats(team_stats, opponent_stats)}")
    
    print("\nTesting generate_league_table...")
    team_results = {
        'Team A': ['W', 'W', 'D', 'L', 'W'],
        'Team B': ['L', 'W', 'D', 'W', 'D'],
        'Team C': ['D', 'L', 'L', 'D', 'L']
    }
    print(f"generate_league_table(team_results) = {generate_league_table(team_results)}")

if __name__ == "__main__":
    main()