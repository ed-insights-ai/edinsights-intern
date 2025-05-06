# Week 5: Web Development & Web Scraping

## Overview
This week focuses on web development fundamentals and web scraping techniques, essential skills for collecting and presenting soccer analytics data. You'll learn to create web pages, extract data from sports websites, and build interactive web applications to display your findings.

## Skills & Difficulty Chart

| Challenge | Main Skills | Difficulty | Application to Capstone |
|-----------|-------------|------------|-------------------------|
| 1. Web Page Creation | HTML, CSS, Responsive Design | ⭐⭐☆☆☆ | Create appealing UI for player stats |
| 2. Web Scraper Development | Beautiful Soup, HTML Parsing | ⭐⭐⭐☆☆ | Collect player data from NCAA sites |
| 3. Flask Web Application | Flask, Templates, Routing | ⭐⭐⭐☆☆ | Build interactive dashboard for data |
| 4. Dynamic Content Scraping | Selenium, JavaScript Content | ⭐⭐⭐⭐☆ | Handle complex NCAA stats pages |

## Learning Objectives
- Understand HTML, CSS, and basic web structure
- Build interactive web applications with Flask
- Extract data from websites using web scraping techniques
- Navigate and parse HTML documents
- Handle dynamic websites and AJAX content

## Required Course Videos
Complete the following course videos before starting this week's assignments:

1. **Day 41: Web Foundation - Introduction to HTML** (58min)
   - HTML syntax and structure
   - Basic tags and elements
   - Document structure

2. **Day 42: Web Foundation - Intermediate HTML** (1hr 1min)
   - Forms and inputs
   - Tables and lists
   - Semantic HTML

3. **Day 43: Web Foundation - Introduction to CSS** (56min)
   - CSS syntax and selectors
   - Styling HTML elements
   - Box model and layout

4. **Day 45: Web Scraping with Beautiful Soup** (1hr 4min)
   - Introduction to web scraping
   - Using Beautiful Soup
   - Extracting and parsing data

5. **Day 55: HTML & URL Parsing in Flask** (33min)
   - Integrating HTML with Flask
   - URL routing and parameters
   - Processing form data

## Assignments

### 1. Web Page Creation 🎯
- Create a simple soccer analytics web page in `webpage.html`
- Apply CSS styling in `styles.css`
- Implement responsive design principles
- See [detailed challenge README](challenges/webpage_README.md)

### 2. Web Scraper Development ⚽
- Create a web scraper in `web_scraper.py` 
- Target a soccer statistics website (demo site provided)
- Extract player and team information
- See [detailed challenge README](challenges/web_scraper_README.md)

### 3. Flask Web Application 🏟️
- Build a Flask web application in `flask_app.py`
- Create routes for displaying and managing soccer data
- Implement templates and form handling
- See [detailed challenge README](challenges/flask_app_README.md)

### 4. Dynamic Content Scraping 🔄
- Implement advanced scraping in `dynamic_scraper.py`
- Handle JavaScript-rendered soccer stats content
- Extract data from interactive elements
- See [detailed challenge README](challenges/dynamic_scraper_README.md)

## Project Milestone: Web Scraper Implementation

In the `PROJECT/` directory:
1. Implement a working web scraper for NCAA soccer statistics
2. Store the scraped data in an appropriate format
3. Add error handling and retry mechanisms
4. Create a simple visualization of the scraped data

Focus on implementing this in the `PROJECT/src/scraping/` directory, building on the existing scraper scaffolding.

> **🌟 CAPSTONE TIP:** The web scraper you build this week will be a critical component of your capstone project's data collection pipeline. Your capstone will need to gather real NCAA soccer data, so create a robust scraper that can handle different page structures and potential site changes. Consider implementing a scheduling system that can regularly update your dataset during your capstone implementation.

## Resources
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [HTML & CSS Tutorial](https://www.w3schools.com/html/)
- [Flask Template Documentation](https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/)
- [Web Scraping Ethics & Best Practices](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)
- [HTTP Request Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [NCAA Soccer Statistics](https://stats.ncaa.org/rankings/DIV2) (Reference for actual data)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)

## Submission
Submit your completed work following the standard pull request process described in the Getting Started guide.