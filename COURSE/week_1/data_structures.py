"""
Data Structures Practice: Soccer Analytics
-----------------------------------------
Complete the following functions according to their docstrings.
This exercise focuses on Python's built-in data structures: lists, dictionaries, sets, and tuples
while introducing you to soccer data analytics concepts.
"""

def unique_goal_scorers(match_report):
    """
    Extract a list of unique goal scorers from a match report while preserving the order.
    
    Args:
        match_report (list): A list of goal scorer names, which may contain duplicates
                           for players who scored multiple goals
        
    Returns:
        list: A list of unique goal scorers in the order they first scored
        
    Example:
        >>> unique_goal_scorers(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo'])
        ['Messi', 'Ronaldo', 'Neymar']
    """
    seen = set()
    unique_scorers = []
    for scorer in match_report:
        if scorer not in seen:
            seen.add(scorer)
            unique_scorers.append(scorer)
    return unique_scorers

def merge_player_stats(season1_stats, season2_stats):
    """
    Merge player statistics from two different seasons. 
    If a player appears in both seasons, use the most recent (season2) statistics.
    
    Args:
        season1_stats (dict): Player statistics from season 1
        season2_stats (dict): Player statistics from season 2
        
    Returns:
        dict: Merged player statistics with season2 taking precedence for players in both seasons
        
    Example:
        >>> merge_player_stats(
        ...     {'Messi': {'goals': 30, 'assists': 10}}, 
        ...     {'Messi': {'goals': 25, 'assists': 15}, 'Ronaldo': {'goals': 28, 'assists': 5}}
        ... )
        {'Messi': {'goals': 25, 'assists': 15}, 'Ronaldo': {'goals': 28, 'assists': 5}}
    """
    merged_stats = season1_stats.copy()
    merged_stats.update(season2_stats)
    return merged_stats

def find_top_scorer(match_goals):
    """
    Find the player who scored the most goals in a series of matches.
    If multiple players have the same highest number of goals, return any one of them.
    
    Args:
        match_goals (list): A list of goal scorers across multiple matches
        
    Returns:
        str: The name of the top goal scorer
        
    Example:
        >>> find_top_scorer(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo', 'Messi'])
        'Messi'
    """
    from collections import Counter
    goal_counts = Counter(match_goals)
    return max(goal_counts, key=goal_counts.get)

def group_players_by_position(players, position_key):
    """
    Group a list of player dictionaries by their position.
    
    Args:
        players (list): A list of player dictionaries
        position_key (str): The key in each dictionary that specifies the player's position
        
    Returns:
        dict: A dictionary where keys are positions and values are lists of players with that position
        
    Example:
        >>> players = [
        ...     {'name': 'Alisson', 'position': 'Goalkeeper'}, 
        ...     {'name': 'Van Dijk', 'position': 'Defender'},
        ...     {'name': 'Salah', 'position': 'Forward'},
        ...     {'name': 'Robertson', 'position': 'Defender'}
        ... ]
        >>> group_players_by_position(players, 'position')
        {
            'Goalkeeper': [{'name': 'Alisson', 'position': 'Goalkeeper'}],
            'Defender': [
                {'name': 'Van Dijk', 'position': 'Defender'}, 
                {'name': 'Robertson', 'position': 'Defender'}
            ],
            'Forward': [{'name': 'Salah', 'position': 'Forward'}]
        }
    """
    grouped = {}
    for player in players:
        position = player[position_key]
        if position not in grouped:
            grouped[position] = []
        grouped[position].append(player)
    return grouped

def total_tournament_goals(tournament_data):
    """
    Calculate the total number of goals across all divisions and matches in a tournament.
    The tournament data structure may contain nested lists and dictionaries.
    
    Args:
        tournament_data (list): A nested structure of tournament data
                              [division, [match, goals], ...]
        
    Returns:
        int: The total number of goals in the tournament
        
    Example:
        >>> tournament_data = [
        ...     'Division 1', 
        ...     [
        ...         ['Match 1', 3],
        ...         ['Match 2', 2]
        ...     ],
        ...     'Division 2',
        ...     [
        ...         ['Match 1', 1],
        ...         ['Match 2', 4],
        ...         ['Match 3', 2]
        ...     ]
        ... ]
        >>> total_tournament_goals(tournament_data)
        12
    """
    total_goals = 0
    for item in tournament_data:
        if isinstance(item, list):
            for match in item:
                total_goals += match[1]
    return total_goals

def main():
    """Run some examples to test your functions."""
    print("Testing unique_goal_scorers...")
    print(f"unique_goal_scorers(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo']) = {unique_goal_scorers(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo'])}")
    
    print("\nTesting merge_player_stats...")
    season1 = {'Messi': {'goals': 30, 'assists': 10}}
    season2 = {'Messi': {'goals': 25, 'assists': 15}, 'Ronaldo': {'goals': 28, 'assists': 5}}
    print(f"merge_player_stats(season1, season2) = {merge_player_stats(season1, season2)}")
    
    print("\nTesting find_top_scorer...")
    print(f"find_top_scorer(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo', 'Messi']) = {find_top_scorer(['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Ronaldo', 'Messi'])}")
    
    print("\nTesting group_players_by_position...")
    players = [
        {'name': 'Alisson', 'position': 'Goalkeeper'}, 
        {'name': 'Van Dijk', 'position': 'Defender'},
        {'name': 'Salah', 'position': 'Forward'},
        {'name': 'Robertson', 'position': 'Defender'}
    ]
    print(f"group_players_by_position(players, 'position') = {group_players_by_position(players, 'position')}")
    
    print("\nTesting total_tournament_goals...")
    tournament_data = [
        'Division 1', 
        [
            ['Match 1', 3],
            ['Match 2', 2]
        ],
        'Division 2',
        [
            ['Match 1', 1],
            ['Match 2', 4],
            ['Match 3', 2]
        ]
    ]
    print(f"total_tournament_goals(tournament_data) = {total_tournament_goals(tournament_data)}")

if __name__ == "__main__":
    main()