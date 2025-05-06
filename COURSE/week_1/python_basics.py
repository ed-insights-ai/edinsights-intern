"""
Python Basics Exercise: Soccer Statistics
--------------------------------------
Complete the following functions according to their docstrings.
This exercise covers basic Python syntax, data types, and operations
while introducing you to soccer data concepts.
"""

def calculate_goals_per_game(goals, games_played):
    """
    Calculate the average goals per game for a soccer player.
    
    Args:
        goals (list): A list of goals scored in each game
        games_played (int): Number of games played
        
    Returns:
        float: The average goals per game, or 0 if no games were played
        
    Example:
        >>> calculate_goals_per_game([1, 0, 2, 1], 4)
        1.0
    """
    # YOUR CODE HERE
    pass

def reverse_team_name(team_name):
    """
    Reverse a soccer team name (useful for creating scrambled team names for quizzes).
    
    Args:
        team_name (str): The team name to reverse
        
    Returns:
        str: The reversed team name
        
    Example:
        >>> reverse_team_name("Manchester United")
        "detinU retsehcnaM"
    """
    # YOUR CODE HERE
    pass

def count_words_in_chant(chant):
    """
    Count the number of words in a soccer chant or team motto.
    
    Args:
        chant (str): The soccer chant or team motto
        
    Returns:
        int: The number of words in the chant
        
    Example:
        >>> count_words_in_chant("You'll Never Walk Alone")
        4
    """
    # YOUR CODE HERE
    pass

def km_to_miles(kilometers):
    """
    Convert distance from kilometers to miles (useful for comparing European
    and American soccer statistics).
    
    The formula is: miles = kilometers * 0.621371
    
    Args:
        kilometers (float): Distance in kilometers
        
    Returns:
        float: Distance in miles
        
    Example:
        >>> km_to_miles(5)
        3.10686
        >>> km_to_miles(10)
        6.21371
    """
    # YOUR CODE HERE
    pass

def is_palindrome_formation(formation):
    """
    Check if a soccer formation is a palindrome when spaces are removed.
    
    This can identify symmetrical formations, which may have balanced tactical properties.
    
    Args:
        formation (str): The formation to check (e.g., "4-4-2", "4-3-2-1")
        
    Returns:
        bool: True if the formation is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome_formation("4-4-2")
        False
        >>> is_palindrome_formation("4-2-2-4")
        True
        >>> is_palindrome_formation("1-2-3-2-1")
        True
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing calculate_goals_per_game...")
    print(f"calculate_goals_per_game([1, 0, 2, 1], 4) = {calculate_goals_per_game([1, 0, 2, 1], 4)}")
    
    print("\nTesting reverse_team_name...")
    print(f"reverse_team_name('Manchester United') = {reverse_team_name('Manchester United')}")
    
    print("\nTesting count_words_in_chant...")
    print(f"count_words_in_chant('You\'ll Never Walk Alone') = {count_words_in_chant('You\'ll Never Walk Alone')}")
    
    print("\nTesting km_to_miles...")
    print(f"km_to_miles(10) = {km_to_miles(10)}")
    
    print("\nTesting is_palindrome_formation...")
    print(f"is_palindrome_formation('4-4-2') = {is_palindrome_formation('4-4-2')}")
    print(f"is_palindrome_formation('4-2-2-4') = {is_palindrome_formation('4-2-2-4')}")
    print(f"is_palindrome_formation('1-2-3-2-1') = {is_palindrome_formation('1-2-3-2-1')}")

if __name__ == "__main__":
    main()