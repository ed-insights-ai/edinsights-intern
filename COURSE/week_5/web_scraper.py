"""
CHALLENGE: NCAA Soccer Web Scraper

Your task is to build a web scraper that extracts soccer player and team statistics 
from a demo NCAA soccer statistics website.

The scraper should:
1. Fetch the web page content
2. Parse the HTML structure
3. Extract player statistics (name, position, goals, assists, etc.)
4. Extract team statistics (wins, losses, etc.)
5. Store the data in appropriate Python data structures
6. Save the extracted data as CSV files

REQUIREMENTS:
- Use the requests library to fetch web content
- Use Beautiful Soup to parse HTML and extract data
- Implement error handling for HTTP requests
- Create functions to extract different types of data
- Store extracted data in CSV format
- Add proper documentation and comments
"""

import requests
from bs4 import BeautifulSoup
import csv
import os
from typing import List, Dict, Any, Optional


def fetch_webpage(url: str) -> Optional[str]:
    """
    Fetch the content of a web page.
    
    Args:
        url: The URL of the webpage to fetch
        
    Returns:
        The HTML content of the page as a string, or None if the request failed
    """
    # TODO: Implement this function to fetch the webpage content
    # Remember to:
    # - Add proper user-agent headers
    # - Implement error handling
    # - Add appropriate delays to be respectful to the website
    pass


def parse_html(html_content: str) -> BeautifulSoup:
    """
    Parse HTML content using Beautiful Soup.
    
    Args:
        html_content: The HTML content to parse
        
    Returns:
        A BeautifulSoup object representing the parsed HTML
    """
    # TODO: Implement this function to parse the HTML content
    pass


def extract_player_stats(soup: BeautifulSoup) -> List[Dict[str, Any]]:
    """
    Extract player statistics from the parsed HTML.
    
    Args:
        soup: The BeautifulSoup object containing the parsed HTML
        
    Returns:
        A list of dictionaries containing player statistics
    """
    # TODO: Implement this function to extract player statistics
    # Each player should be represented as a dictionary with keys such as:
    # - player_name
    # - position
    # - goals
    # - assists
    # - shots
    # - shots_on_goal
    # - etc.
    pass


def extract_team_stats(soup: BeautifulSoup) -> Dict[str, Any]:
    """
    Extract team statistics from the parsed HTML.
    
    Args:
        soup: The BeautifulSoup object containing the parsed HTML
        
    Returns:
        A dictionary containing team statistics
    """
    # TODO: Implement this function to extract team statistics
    # The team statistics should be represented as a dictionary with keys such as:
    # - team_name
    # - wins
    # - losses
    # - ties
    # - goals_for
    # - goals_against
    # - etc.
    pass


def save_to_csv(data: List[Dict[str, Any]], filename: str) -> None:
    """
    Save data to a CSV file.
    
    Args:
        data: The data to save (list of dictionaries)
        filename: The name of the CSV file to save to
    """
    # TODO: Implement this function to save the data to a CSV file
    # Make sure to:
    # - Create the file with appropriate headers
    # - Handle cases where the dictionaries might have different keys
    # - Create the directory if it doesn't exist
    pass


def main():
    """
    Main function to run the web scraper.
    """
    # TODO: Implement the main function to orchestrate the web scraping process
    # Use the demo URL: "https://web-scraping-demo.onrender.com/ncaa-soccer-stats"
    # This is a fictional demo site for educational purposes
    
    # Example workflow:
    # 1. Fetch the webpage
    # 2. Parse the HTML
    # 3. Extract player statistics
    # 4. Extract team statistics
    # 5. Save the data to CSV files
    pass


if __name__ == "__main__":
    main()