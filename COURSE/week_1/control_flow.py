"""
Control Flow Challenge: Soccer Edition
-------------------------------------
Complete the following functions according to their docstrings.
This exercise focuses on conditional statements and loops in Python
while introducing you to soccer match concepts.
"""

def goal_commentary(n):
    """
    Implement a soccer commentary generator based on goal patterns.
    
    For numbers 1 to n:
    - If the number is divisible by 3, print "Goal!"
    - If the number is divisible by 5, print "Save!"
    - If the number is divisible by both 3 and 5, print "Spectacular Play!"
    - Otherwise, print "Minute X" where X is the number itself
    
    Args:
        n (int): Number of minutes to commentate
        
    Returns:
        list: A list of commentary strings
        
    Example:
        >>> goal_commentary(15)
        ['Minute 1', 'Minute 2', 'Goal!', 'Minute 4', 'Save!', 'Goal!', 'Minute 7', 'Minute 8', 'Goal!', 'Save!', 'Minute 11', 'Goal!', 'Minute 13', 'Minute 14', 'Spectacular Play!']
    """
    # YOUR CODE HERE
    pass

def is_prime_jersey_number(number):
    """
    Check if a jersey number is prime. This is often used to identify
    'special' jersey numbers in soccer.
    
    A prime number is a natural number greater than 1 that is not a product
    of two smaller natural numbers.
    
    Args:
        number (int): The jersey number to check
        
    Returns:
        bool: True if the jersey number is prime, False otherwise
        
    Example:
        >>> is_prime_jersey_number(7)  # Many famous players wear 7
        True
        >>> is_prime_jersey_number(10)  # Classic number 10 is not prime
        False
    """
    # YOUR CODE HERE
    pass

def find_season_extremes(match_scores):
    """
    Find the highest and lowest scoring matches in a season without using built-in max/min functions.
    
    Args:
        match_scores (list): A list of match scores (total goals scored in each match)
        
    Returns:
        tuple: A tuple containing (highest_score, lowest_score)
        
    Example:
        >>> find_season_extremes([2, 0, 5, 1, 3])
        (5, 0)
    """
    # YOUR CODE HERE
    pass

def calculate_performance_tier(player_rating):
    """
    Convert a player's numerical rating to a performance tier.
    
    Rating scale:
    - 90-100: 'World Class'
    - 80-89: 'Elite'
    - 70-79: 'Quality'
    - 60-69: 'Average'
    - Below 60: 'Development Prospect'
    
    Args:
        player_rating (float): Numerical rating (0-100)
        
    Returns:
        str: Performance tier
        
    Example:
        >>> calculate_performance_tier(85)
        'Elite'
    """
    # YOUR CODE HERE
    pass

def cumulative_goal_difference(goal_differences):
    """
    Calculate the cumulative goal difference over a season.
    
    This helps track a team's performance trajectory throughout the season.
    
    Args:
        goal_differences (list): List of goal differences for each match
                                (positive for wins, negative for losses, 0 for draws)
        
    Returns:
        list: Cumulative goal difference after each match
        
    Example:
        >>> cumulative_goal_difference([1, -1, 2, 0, -2])
        [1, 0, 2, 2, 0]  # Running total after each match
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing goal_commentary...")
    print(f"goal_commentary(15) = {goal_commentary(15)}")
    
    print("\nTesting is_prime_jersey_number...")
    print(f"is_prime_jersey_number(7) = {is_prime_jersey_number(7)}")
    print(f"is_prime_jersey_number(10) = {is_prime_jersey_number(10)}")
    
    print("\nTesting find_season_extremes...")
    print(f"find_season_extremes([2, 0, 5, 1, 3]) = {find_season_extremes([2, 0, 5, 1, 3])}")
    
    print("\nTesting calculate_performance_tier...")
    print(f"calculate_performance_tier(85) = {calculate_performance_tier(85)}")
    
    print("\nTesting cumulative_goal_difference...")
    print(f"cumulative_goal_difference([1, -1, 2, 0, -2]) = {cumulative_goal_difference([1, -1, 2, 0, -2])}")

if __name__ == "__main__":
    main()