"""
Control Flow Challenge
---------------------
Complete the following functions according to their docstrings.
This exercise focuses on conditional statements and loops in Python.
"""

def fizzbuzz(n):
    """
    Implement the classic FizzBuzz problem.
    
    For numbers 1 to n:
    - If the number is divisible by 3, print "Fizz"
    - If the number is divisible by 5, print "Buzz"
    - If the number is divisible by both 3 and 5, print "FizzBuzz"
    - Otherwise, print the number itself
    
    Args:
        n (int): Upper limit of numbers to process
        
    Returns:
        list: A list of strings with the FizzBuzz results
        
    Example:
        >>> fizzbuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    # YOUR CODE HERE
    pass

def is_prime(number):
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that is not a product
    of two smaller natural numbers.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
    """
    # YOUR CODE HERE
    pass

def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list without using built-in max/min functions.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        tuple: A tuple containing (max_value, min_value)
        
    Example:
        >>> find_max_min([5, 3, 9, 1, 7])
        (9, 1)
    """
    # YOUR CODE HERE
    pass

def calculate_grade(score):
    """
    Convert a numerical score to a letter grade.
    
    Grade scale:
    - 90-100: 'A'
    - 80-89: 'B'
    - 70-79: 'C'
    - 60-69: 'D'
    - Below 60: 'F'
    
    Args:
        score (float): Numerical score (0-100)
        
    Returns:
        str: Letter grade
        
    Example:
        >>> calculate_grade(85)
        'B'
    """
    # YOUR CODE HERE
    pass

def sum_of_squares(n):
    """
    Calculate the sum of squares from 1 to n.
    
    Args:
        n (int): Upper limit of the sequence
        
    Returns:
        int: The sum of squares from 1 to n
        
    Example:
        >>> sum_of_squares(4)
        30  # 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing fizzbuzz...")
    print(f"fizzbuzz(15) = {fizzbuzz(15)}")
    
    print("\nTesting is_prime...")
    print(f"is_prime(7) = {is_prime(7)}")
    print(f"is_prime(4) = {is_prime(4)}")
    
    print("\nTesting find_max_min...")
    print(f"find_max_min([5, 3, 9, 1, 7]) = {find_max_min([5, 3, 9, 1, 7])}")
    
    print("\nTesting calculate_grade...")
    print(f"calculate_grade(85) = {calculate_grade(85)}")
    
    print("\nTesting sum_of_squares...")
    print(f"sum_of_squares(4) = {sum_of_squares(4)}")

if __name__ == "__main__":
    main()