"""
Python Basics Exercise
----------------------
Complete the following functions according to their docstrings.
This exercise covers basic Python syntax, data types, and operations.
"""

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        float: The average of the numbers, or 0 if the list is empty
        
    Example:
        >>> calculate_average([10, 20, 30, 40])
        25.0
    """
    # YOUR CODE HERE
    pass

def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    # YOUR CODE HERE
    pass

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Args:
        sentence (str): The sentence to count words in
        
    Returns:
        int: The number of words in the sentence
        
    Example:
        >>> count_words("This is a test sentence")
        5
    """
    # YOUR CODE HERE
    pass

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    The formula is: F = C * 9/5 + 32
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
        
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    # YOUR CODE HERE
    pass

def is_palindrome(text):
    """
    Check if a string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward,
    ignoring case, spaces, and punctuation.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing calculate_average...")
    print(f"calculate_average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
    
    print("\nTesting reverse_string...")
    print(f"reverse_string('python') = {reverse_string('python')}")
    
    print("\nTesting count_words...")
    print(f"count_words('The quick brown fox jumps over the lazy dog') = {count_words('The quick brown fox jumps over the lazy dog')}")
    
    print("\nTesting celsius_to_fahrenheit...")
    print(f"celsius_to_fahrenheit(25) = {celsius_to_fahrenheit(25)}")
    
    print("\nTesting is_palindrome...")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"is_palindrome('hello') = {is_palindrome('hello')}")
    print(f"is_palindrome('A man, a plan, a canal: Panama') = {is_palindrome('A man, a plan, a canal: Panama')}")

if __name__ == "__main__":
    main()