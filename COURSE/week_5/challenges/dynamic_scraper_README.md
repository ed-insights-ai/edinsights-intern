# Challenge 4: Dynamic Soccer Content Scraper

**Difficulty: ⭐⭐⭐⭐☆**

## Challenge Overview

In this challenge, you'll build an advanced web scraper that can handle dynamic, JavaScript-rendered content on NCAA soccer statistics websites. Many modern web applications load data dynamically after the initial page load, which requires special handling beyond basic HTML parsing.

## Learning Objectives

- Understand how to scrape dynamically-loaded web content
- Use Selenium to automate browser interactions
- Implement waiting strategies for JavaScript-rendered elements
- Navigate through multi-page data sources
- Handle complex web scenarios like logins and popups
- Extract data from interactive elements and tables

## Real-World Context

Modern sports statistics websites often use JavaScript frameworks to render data dynamically. NCAA websites and other soccer statistics platforms may load player and team data after the initial page load, require user interaction to display additional data, or implement pagination for large datasets. An effective scraper for your capstone project must be able to handle these scenarios to collect comprehensive player and team statistics.

## Challenge Details

### The Task

Create an advanced web scraper using Selenium that:
1. Launches a browser to handle JavaScript-rendered content
2. Navigates to a demo NCAA soccer statistics page
3. Waits for dynamic content to load
4. Extracts player statistics from tables that load dynamically
5. Navigates through pagination to collect all available data
6. Handles any login requirements or popup dialogs
7. Saves the collected data in a structured format

### Dynamic Scraping Workflow

```
    +------------------------+
    | Initialize WebDriver   |
    +------------------------+
              |
              v
    +------------------------+
    | Navigate to URL        |
    +------------------------+
              |
              v
    +------------------------+
    | Wait for Content Load  |
    +------------------------+
              |
              v
    +------------------------+
    | Extract Player Stats   |
    +------------------------+
              |
              v
    +------------------------+
    | Extract Team Stats     |
    +------------------------+
              |
              v
    +-----------+  No  +------------------------+
    | More Pages?  |----→| Save Data & Clean Up  |
    +-----------+       +------------------------+
              |
              | Yes
              v
    +------------------------+
    | Navigate to Next Page  |
    +------------------------+
              |
              +----------------→ (back to Wait for Content Load)
```

## Tips and Hints

### Setting Up Selenium WebDriver

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    """Initialize and configure the Selenium WebDriver."""
    options = Options()
    
    # Uncomment for headless operation
    # options.add_argument("--headless")
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Set page load timeout
    driver.set_page_load_timeout(30)
    
    return driver
```

### Waiting for Elements to Load

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, selector, by=By.CSS_SELECTOR, timeout=10):
    """Wait for an element to be visible on the page."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        return element
    except TimeoutException:
        print(f"Timed out waiting for element: {selector}")
        return None
```

### Extracting Data from Dynamic Tables

```python
def extract_player_stats(driver):
    """Extract player statistics from a dynamic page."""
    players = []
    
    # Wait for the table to be visible
    player_table = wait_for_element(driver, "table.player-stats")
    if not player_table:
        return players
    
    # Get table headers
    header_elements = driver.find_elements(By.CSS_SELECTOR, "table.player-stats thead th")
    headers = [header.text.strip() for header in header_elements]
    
    # Extract data from each row
    rows = driver.find_elements(By.CSS_SELECTOR, "table.player-stats tbody tr")
    for row in rows:
        player_data = {}
        cells = row.find_elements(By.TAG_NAME, "td")
        
        for i, cell in enumerate(cells):
            if i < len(headers):
                # Convert numeric values to appropriate types
                value = cell.text.strip()
                if headers[i] in ["Goals", "Assists", "Shots"]:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                player_data[headers[i]] = value
                
        players.append(player_data)
    
    return players
```

### Handling Pagination

```python
def handle_pagination(driver, next_button_selector="button.pagination-next"):
    """Navigate to the next page of results."""
    try:
        # Check if there's a next page button and it's enabled
        next_button = driver.find_element(By.CSS_SELECTOR, next_button_selector)
        
        if "disabled" in next_button.get_attribute("class"):
            return False  # No more pages
            
        # Click the next button
        next_button.click()
        
        # Wait for the new page to load (for example, wait for a table to be visible again)
        wait_for_element(driver, "table.player-stats")
        
        # Add a small delay to ensure everything is loaded
        time.sleep(1)
        
        return True  # Successfully navigated to next page
        
    except NoSuchElementException:
        print("No pagination button found")
        return False
    except Exception as e:
        print(f"Error during pagination: {e}")
        return False
```

## Testing Your Solution

Your solution should:
1. Successfully load pages with dynamic content
2. Extract player statistics from JavaScript-rendered tables
3. Navigate through all available pages of data
4. Handle any interactive elements or login requirements
5. Save the extracted data in a structured format
6. Handle errors gracefully

Test with these scenarios:
1. Pages that load data after initial HTML load
2. Tables with pagination
3. Dropdown menus or filters that need interaction
4. Forms that need to be submitted
5. Content that changes based on user interaction

## Application to Capstone

For your capstone project, you'll need to collect comprehensive NCAA Division II soccer data, which may be spread across multiple interactive pages. This advanced scraper will allow you to:

1. Access player and team statistics that load dynamically
2. Collect data from interactive dashboards and statistics portals
3. Navigate through season archives and game reports
4. Handle login-protected resources (if applicable)
5. Build a more robust data collection system for your analytics platform

The ability to scrape dynamic content will significantly expand the range and depth of data available for your analysis, leading to more comprehensive insights for NCAA soccer programs.

## Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [WebDriverManager for Python](https://github.com/SergeyPirogov/webdriver_manager)
- [Selenium Expected Conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html)
- [Working with Dynamic Web Content](https://towardsdatascience.com/web-scraping-dynamic-websites-with-python-using-selenium-f6dc1e2588bb)
- [XPath and CSS Selectors Tutorial](https://www.lambdatest.com/blog/complete-guide-for-using-xpath-in-selenium-with-examples/)
- [Handling Waits in Selenium](https://www.selenium.dev/documentation/en/webdriver/waits/)