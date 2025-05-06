# Challenge 2: NCAA Soccer Web Scraper

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll build a web scraper that extracts soccer player and team statistics from a demo NCAA stats website. This is a crucial skill for your capstone project, as you'll need to collect real NCAA Division II soccer data from official sources.

## Learning Objectives

- Understand the basics of web scraping and HTML parsing
- Use the BeautifulSoup library to extract data from web pages
- Implement error handling for HTTP requests
- Process and structure extracted data
- Write data to CSV files for later analysis

## Real-World Context

Data collection is the foundation of any sports analytics system. NCAA soccer programs don't always have convenient APIs for accessing player and team statistics, so web scraping becomes a necessary skill. Analysts use scraped data to build performance metrics, identify trends, and generate insights for coaches and players.

## Challenge Details

### The Task

Create a web scraper using Python that:
1. Fetches the HTML content of a demo NCAA soccer statistics website
2. Parses the HTML using BeautifulSoup
3. Extracts player statistics (name, position, goals, assists, etc.)
4. Extracts team statistics (wins, losses, etc.)
5. Stores the data in appropriate Python data structures
6. Saves the extracted data to CSV files

### Web Scraping Workflow

```
         +----------------+
         | Fetch Web Page |
         +----------------+
                 |
                 v
         +----------------+
         |   Parse HTML   |
         +----------------+
                 |
                 v
         +----------------+
         | Extract Player |
         |  Statistics    |
         +----------------+
                 |
                 v
         +----------------+
         | Extract Team   |
         |  Statistics    |
         +----------------+
                 |
                 v
         +----------------+
         |  Save Data to  |
         |  CSV Files     |
         +----------------+
```

### HTML Structure of Demo Page

The demo page you'll scrape has this general structure:

```html
<html>
  <head>...</head>
  <body>
    <header>...</header>
    
    <section id="player-stats">
      <h2>Player Statistics</h2>
      <table class="stats-table">
        <thead>
          <tr>
            <th>Player Name</th>
            <th>Position</th>
            <th>Goals</th>
            <th>Assists</th>
            <!-- More headers -->
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Player 1</td>
            <td>Forward</td>
            <td>10</td>
            <td>5</td>
            <!-- More data -->
          </tr>
          <!-- More players -->
        </tbody>
      </table>
    </section>
    
    <section id="team-stats">
      <h2>Team Statistics</h2>
      <div class="team-record">
        <h3>Season Record</h3>
        <p>Wins: <span class="wins">15</span></p>
        <p>Losses: <span class="losses">3</span></p>
        <p>Ties: <span class="ties">2</span></p>
      </div>
      <!-- More team stats -->
    </section>
  </body>
</html>
```

## Tips and Hints

### Setting Up Requests

When making HTTP requests, always:
1. Set appropriate headers (especially User-Agent)
2. Implement error handling
3. Add delays between requests to be respectful

```python
def fetch_webpage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
```

### Parsing with BeautifulSoup

```python
def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')
```

### Extracting Data from Tables

```python
def extract_player_stats(soup):
    players = []
    player_table = soup.select_one('table.stats-table')
    
    if not player_table:
        return players
        
    headers = [header.text.strip() for header in player_table.select('thead th')]
    
    for row in player_table.select('tbody tr'):
        player_data = {}
        for i, cell in enumerate(row.select('td')):
            if i < len(headers):
                player_data[headers[i]] = cell.text.strip()
        players.append(player_data)
        
    return players
```

### Saving Data to CSV

```python
def save_to_csv(data, filename):
    if not data:
        print(f"No data to save to {filename}")
        return
        
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Get all possible keys from all dictionaries
    fieldnames = set()
    for item in data:
        fieldnames.update(item.keys())
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Data saved to {filename}")
```

## Testing Your Solution

Your solution should:
1. Successfully fetch web content with proper error handling
2. Correctly extract player statistics from tables
3. Correctly extract team statistics from relevant sections
4. Save the data to properly formatted CSV files
5. Include proper documentation and comments
6. Handle potential errors gracefully

## Application to Capstone

For your capstone project, you'll need to collect real NCAA Division II soccer data, which might be spread across multiple pages and have complex HTML structures. The scraper you build in this challenge will be the foundation for your data collection pipeline. You'll later enhance it to handle pagination, more complex data structures, and to be more robust against website changes.

## Ethical Considerations

Web scraping comes with ethical and legal considerations:
1. Always respect robots.txt files
2. Add delays between requests to avoid overwhelming servers
3. Identify your scraper with appropriate User-Agent headers
4. Only scrape publicly available data
5. Use the data for personal analysis, not commercial redistribution

## Resources

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [Web Scraping Ethics](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
- [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- [Mozilla Developer Network: HTML Tables](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
- [Demo URL for Practice](https://web-scraping-demo.onrender.com/ncaa-soccer-stats)