"""
API Integration
------------
Complete the following functions according to their docstrings.
This exercise focuses on working with APIs in Python.
"""

import requests
import json
import time
from datetime import datetime

def make_api_request(url, method="GET", headers=None, params=None, data=None, timeout=10):
    """
    Make an API request.
    
    Args:
        url (str): The API endpoint URL
        method (str, optional): HTTP method ('GET', 'POST', 'PUT', 'DELETE'). Defaults to "GET".
        headers (dict, optional): HTTP headers. Defaults to None.
        params (dict, optional): Query parameters. Defaults to None.
        data (dict, optional): Request body for POST/PUT. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
        
    Returns:
        tuple: (response_data, status_code)
        
    Raises:
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def get_weather_data(api_key, city):
    """
    Get current weather data for a city using OpenWeatherMap API.
    
    Args:
        api_key (str): OpenWeatherMap API key
        city (str): City name
        
    Returns:
        dict: Weather data
        
    Raises:
        ValueError: If the city is not found
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def get_github_user_repos(username):
    """
    Get the public repositories for a GitHub user.
    
    Args:
        username (str): GitHub username
        
    Returns:
        list: List of repository dictionaries
        
    Raises:
        ValueError: If the user is not found
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def post_data_to_api(url, data, headers=None):
    """
    Send data to an API using a POST request.
    
    Args:
        url (str): The API endpoint URL
        data (dict): Data to send
        headers (dict, optional): HTTP headers. Defaults to None.
        
    Returns:
        tuple: (response_data, status_code)
        
    Raises:
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def fetch_paginated_data(url, params=None, page_param="page", limit=None):
    """
    Fetch data from a paginated API endpoint.
    
    Args:
        url (str): The API endpoint URL
        params (dict, optional): Query parameters. Defaults to None.
        page_param (str, optional): Name of the page parameter. Defaults to "page".
        limit (int, optional): Maximum number of items to fetch. Defaults to None (fetch all).
        
    Returns:
        list: Combined results from all pages
        
    Raises:
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def handle_rate_limits(func, max_retries=3, delay=1):
    """
    Decorator function to handle API rate limits.
    
    Args:
        func (function): Function to decorate
        max_retries (int, optional): Maximum number of retries. Defaults to 3.
        delay (int, optional): Delay between retries in seconds. Defaults to 1.
        
    Returns:
        function: Decorated function
    """
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < max_retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.HTTPError as e:
                # Check if rate limited (usually 429 Too Many Requests)
                if e.response.status_code == 429:
                    attempts += 1
                    if attempts < max_retries:
                        retry_after = int(e.response.headers.get('Retry-After', delay))
                        print(f"Rate limited. Retrying in {retry_after} seconds...")
                        time.sleep(retry_after)
                    else:
                        raise ValueError("Max retries exceeded due to rate limiting")
                else:
                    raise
    return wrapper

def download_file_from_url(url, save_path):
    """
    Download a file from a URL and save it to the specified path.
    
    Args:
        url (str): URL of the file to download
        save_path (str): Path where the file should be saved
        
    Returns:
        bool: True if download was successful
        
    Raises:
        requests.exceptions.RequestException: If the request fails
    """
    # YOUR CODE HERE
    pass

def create_api_client(base_url, auth_token=None):
    """
    Create a simple API client with preset base URL and auth token.
    
    Args:
        base_url (str): Base URL for API requests
        auth_token (str, optional): Authentication token. Defaults to None.
        
    Returns:
        dict: Dictionary containing API client functions:
            - get(endpoint, params): Make GET request
            - post(endpoint, data): Make POST request
            - put(endpoint, data): Make PUT request
            - delete(endpoint): Make DELETE request
    """
    # YOUR CODE HERE
    pass

def main():
    """Run examples to test your functions."""
    print("API Integration Examples")
    
    # Note: In a real assignment, students would use their own API keys
    # For this template, we'll use placeholders
    
    # Example 1: Get GitHub user repositories
    try:
        print("\nFetching public repositories for 'octocat':")
        repos = get_github_user_repos("octocat")
        print(f"Found {len(repos)} repositories")
        # Print the first 3 repo names
        if repos:
            print("Repository names:")
            for repo in repos[:3]:
                print(f"- {repo['name']}")
    except Exception as e:
        print(f"Error fetching GitHub repos: {e}")
    
    # Example 2: Make a simple API request
    try:
        print("\nMaking request to JSONPlaceholder API:")
        url = "https://jsonplaceholder.typicode.com/posts/1"
        data, status = make_api_request(url)
        print(f"Status code: {status}")
        print(f"Data: {json.dumps(data, indent=2)}")
    except Exception as e:
        print(f"Error making API request: {e}")
    
    # Example 3: Fetch paginated data
    try:
        print("\nFetching paginated data (first 5 items):")
        url = "https://jsonplaceholder.typicode.com/posts"
        data = fetch_paginated_data(url, limit=5)
        print(f"Fetched {len(data)} items")
    except Exception as e:
        print(f"Error fetching paginated data: {e}")
    
    print("\nNote: In a real assignment, you would implement and test all functions")

if __name__ == "__main__":
    main()