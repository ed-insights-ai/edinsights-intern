"""
Data Structures Practice
-----------------------
Complete the following functions according to their docstrings.
This exercise focuses on Python's built-in data structures: lists, dictionaries, sets, and tuples.
"""

def unique_elements(input_list):
    """
    Return a list of unique elements from the input list while preserving order.
    
    Args:
        input_list (list): A list of elements that may contain duplicates
        
    Returns:
        list: A list of unique elements in the order they first appeared
        
    Example:
        >>> unique_elements([1, 2, 3, 1, 2, 4])
        [1, 2, 3, 4]
    """
    # YOUR CODE HERE
    pass

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If there are duplicate keys, use the value from dict2.
    
    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary
        
    Returns:
        dict: Merged dictionary with values from dict2 taking precedence for duplicate keys
        
    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    # YOUR CODE HERE
    pass

def find_most_frequent(items):
    """
    Find the most frequently occurring item in a list.
    If there are multiple items with the same highest frequency, return any one of them.
    
    Args:
        items (list): A list of items
        
    Returns:
        The item that appears most frequently in the list
        
    Example:
        >>> find_most_frequent([1, 2, 3, 2, 1, 2, 4, 5])
        2
    """
    # YOUR CODE HERE
    pass

def group_by_key(records, key):
    """
    Group a list of dictionaries by a specified key.
    
    Args:
        records (list): A list of dictionaries
        key (str): The key to group by
        
    Returns:
        dict: A dictionary where keys are the unique values of the specified key,
              and values are lists of records with that key value
        
    Example:
        >>> records = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, 
                       {'name': 'Charlie', 'age': 25}]
        >>> group_by_key(records, 'age')
        {25: [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}], 
         30: [{'name': 'Bob', 'age': 30}]}
    """
    # YOUR CODE HERE
    pass

def nested_sum(nested_list):
    """
    Calculate the sum of all numbers in a nested list structure.
    The list may contain non-numeric elements that should be skipped.
    
    Args:
        nested_list (list): A list that may contain nested lists, numbers, and other elements
        
    Returns:
        float: The sum of all numbers in the nested structure
        
    Example:
        >>> nested_sum([1, [2, 3], [4, [5, 6]], 'a', {'b': 7}])
        21
    """
    # YOUR CODE HERE
    pass

def main():
    """Run some examples to test your functions."""
    print("Testing unique_elements...")
    print(f"unique_elements([1, 2, 3, 1, 2, 4]) = {unique_elements([1, 2, 3, 1, 2, 4])}")
    
    print("\nTesting merge_dictionaries...")
    print(f"merge_dictionaries({{'a': 1, 'b': 2}}, {{'b': 3, 'c': 4}}) = {merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}")
    
    print("\nTesting find_most_frequent...")
    print(f"find_most_frequent([1, 2, 3, 2, 1, 2, 4, 5]) = {find_most_frequent([1, 2, 3, 2, 1, 2, 4, 5])}")
    
    print("\nTesting group_by_key...")
    records = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 25}]
    print(f"group_by_key(records, 'age') = {group_by_key(records, 'age')}")
    
    print("\nTesting nested_sum...")
    print(f"nested_sum([1, [2, 3], [4, [5, 6]], 'a', {{'b': 7}}]) = {nested_sum([1, [2, 3], [4, [5, 6]], 'a', {'b': 7}])}")

if __name__ == "__main__":
    main()