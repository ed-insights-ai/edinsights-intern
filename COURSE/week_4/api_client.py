"""
RESTful API Client
---------------
Implement a complete API client according to the specified requirements.
This exercise focuses on creating a robust client for interacting with RESTful APIs.
"""

import requests
import json
import os
import time
import logging
from urllib.parse import urljoin

class APIClient:
    """
    A class for interacting with RESTful APIs.
    
    Attributes:
        base_url (str): The base URL of the API
        headers (dict): Default headers to send with requests
        timeout (int): Default timeout for requests in seconds
        logger (logging.Logger): Logger for the client
        
    Methods:
        get: Send a GET request
        post: Send a POST request
        put: Send a PUT request
        delete: Send a DELETE request
        handle_response: Process API responses
        set_auth_token: Set an authentication token
    """
    
    def __init__(self, base_url, auth_token=None, timeout=10):
        """
        Initialize the API client.
        
        Args:
            base_url (str): The base URL of the API
            auth_token (str, optional): Authentication token. Defaults to None.
            timeout (int, optional): Default timeout in seconds. Defaults to 10.
        """
        # YOUR CODE HERE
        pass
    
    def get(self, endpoint, params=None):
        """
        Send a GET request to the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            params (dict, optional): Query parameters. Defaults to None.
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            ValueError: If the API returns an error response
        """
        # YOUR CODE HERE
        pass
    
    def post(self, endpoint, data=None, json_data=None):
        """
        Send a POST request to the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            data (dict, optional): Form data. Defaults to None.
            json_data (dict, optional): JSON data. Defaults to None.
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            ValueError: If the API returns an error response
        """
        # YOUR CODE HERE
        pass
    
    def put(self, endpoint, data=None, json_data=None):
        """
        Send a PUT request to the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            data (dict, optional): Form data. Defaults to None.
            json_data (dict, optional): JSON data. Defaults to None.
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            ValueError: If the API returns an error response
        """
        # YOUR CODE HERE
        pass
    
    def delete(self, endpoint, params=None):
        """
        Send a DELETE request to the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            params (dict, optional): Query parameters. Defaults to None.
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            ValueError: If the API returns an error response
        """
        # YOUR CODE HERE
        pass
    
    def handle_response(self, response):
        """
        Process the API response.
        
        Args:
            response (requests.Response): The HTTP response
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            ValueError: If the response contains an error
        """
        # YOUR CODE HERE
        pass
    
    def set_auth_token(self, token, token_type="Bearer"):
        """
        Set an authentication token for the client.
        
        Args:
            token (str): The authentication token
            token_type (str, optional): The token type. Defaults to "Bearer".
            
        Returns:
            None
        """
        # YOUR CODE HERE
        pass
    
    def set_basic_auth(self, username, password):
        """
        Set basic authentication for the client.
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            None
        """
        # YOUR CODE HERE
        pass
    
    def set_custom_header(self, key, value):
        """
        Set a custom header for requests.
        
        Args:
            key (str): Header name
            value (str): Header value
            
        Returns:
            None
        """
        # YOUR CODE HERE
        pass
    
    def upload_file(self, endpoint, filepath, file_param_name='file', additional_data=None):
        """
        Upload a file to the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            filepath (str): Path to the file to upload
            file_param_name (str, optional): Name of the file parameter. Defaults to 'file'.
            additional_data (dict, optional): Additional form data. Defaults to None.
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            requests.exceptions.RequestException: If the request fails
            ValueError: If the API returns an error response
        """
        # YOUR CODE HERE
        pass
    
    def download_file(self, endpoint, save_path, params=None):
        """
        Download a file from the API.
        
        Args:
            endpoint (str): API endpoint (relative to base_url)
            save_path (str): Path where to save the file
            params (dict, optional): Query parameters. Defaults to None.
            
        Returns:
            bool: True if download was successful
            
        Raises:
            requests.exceptions.RequestException: If the request fails
            IOError: If writing to the file fails
        """
        # YOUR CODE HERE
        pass
    
    def retry_request(self, method, endpoint, max_retries=3, retry_delay=1, **kwargs):
        """
        Send a request with automatic retry logic.
        
        Args:
            method (str): HTTP method ('get', 'post', 'put', 'delete')
            endpoint (str): API endpoint (relative to base_url)
            max_retries (int, optional): Maximum number of retries. Defaults to 3.
            retry_delay (int, optional): Delay between retries in seconds. Defaults to 1.
            **kwargs: Additional arguments to pass to the request method
            
        Returns:
            dict or list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: If all retries fail
            ValueError: If the API returns an error response on all retries
        """
        # YOUR CODE HERE
        pass


class APIClientExample:
    """Examples of how to use the APIClient class."""
    
    def run_examples(self):
        """Run some example API requests."""
        # Initialize client with JSONPlaceholder API
        client = APIClient('https://jsonplaceholder.typicode.com/')
        
        # Example 1: GET request
        print("Example 1: GET request")
        try:
            posts = client.get('posts')
            print(f"Retrieved {len(posts)} posts")
            print(f"First post title: {posts[0]['title']}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Example 2: GET request with parameters
        print("\nExample 2: GET request with parameters")
        try:
            posts = client.get('posts', params={'userId': 1})
            print(f"Retrieved {len(posts)} posts for user 1")
        except Exception as e:
            print(f"Error: {e}")
        
        # Example 3: POST request
        print("\nExample 3: POST request")
        try:
            new_post = {
                'title': 'New Post',
                'body': 'This is a new post',
                'userId': 1
            }
            response = client.post('posts', json_data=new_post)
            print(f"Created new post with ID: {response.get('id')}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Example 4: PUT request
        print("\nExample 4: PUT request")
        try:
            updated_post = {
                'id': 1,
                'title': 'Updated Post',
                'body': 'This post has been updated',
                'userId': 1
            }
            response = client.put('posts/1', json_data=updated_post)
            print(f"Updated post: {response.get('title')}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Example 5: DELETE request
        print("\nExample 5: DELETE request")
        try:
            response = client.delete('posts/1')
            print(f"Deleted post. Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
        
        print("\nNote: These examples use JSONPlaceholder, a fake REST API for testing")


def main():
    """Run the API client examples."""
    example = APIClientExample()
    example.run_examples()

if __name__ == "__main__":
    main()