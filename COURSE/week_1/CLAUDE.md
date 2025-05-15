# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains materials for the ED-Insights.AI 10-week internship program focused on NCAA Division II Soccer Player Analysis. The program combines structured Python programming education with the incremental development of a comprehensive player analysis system, culminating in a capstone project.

## Project Structure

The repository is organized into three main sections:

1. **COURSE/** - Weekly programming course materials and assignments that follow a 10-week curriculum
2. **PROJECT/** - Soccer analysis project source code and resources
3. **SUBMISSIONS/** - Templates for weekly submissions
4. **TEMPLATES/** - Documentation and workflow templates

## Week 1 Specific Information

Week 1 focuses on Python fundamentals for soccer analytics, covering:
- Basic Python syntax and data types
- Control structures (if/else, loops)
- Functions and modules
- Python's built-in data structures (lists, dictionaries, tuples, sets)

The week includes four coding challenges:
1. `python_basics.py` - Basic calculations and string operations
2. `control_flow.py` - Conditionals and loops for match scenarios
3. `data_structures.py` - Working with lists, dictionaries, and nested structures
4. `functions.py` - Creating analytics functions

## Common Commands

### Running Week 1 Assignments

```bash
# Run any of the week 1 assignment files
python python_basics.py
python control_flow.py
python data_structures.py
python functions.py
```

### Running the Dashboard Application

```bash
# Navigate to the dashboard directory
cd PROJECT/src/dashboard

# Run the Flask application
python app.py
```

### Running Tests

```bash
# Run all tests
pytest PROJECT/tests/

# Run specific test file
pytest PROJECT/tests/test_player_metrics.py

# Run with verbose output
pytest -v PROJECT/tests/
```

### Running the Player Metrics Module

```bash
# Navigate to the analysis directory
cd PROJECT/src/analysis

# Run the player metrics module
python player_metrics.py
```

### Running the NCAA Scraper

```bash
# Navigate to the scraping directory
cd PROJECT/src/scraping

# Run the scraper
python ncaa_scraper.py
```

## Testing Week 1 Assignments

The week 1 assignments include their own testing functionality:
- Each Python file has a `main()` function that will test the implemented functions
- Running the file directly (e.g., `python python_basics.py`) will execute these tests
- Each function's docstring includes examples showing expected outputs

## Code Architecture

### Main Components

1. **Data Collection** (`PROJECT/src/scraping/`)
   - Web scraping of NCAA Division II soccer statistics
   - API integration with sports data sources

2. **Data Analysis** (`PROJECT/src/analysis/`)
   - Player performance metrics calculation
   - Statistical analysis of player and team data
   - Predictive models for performance evaluation

3. **Data Visualization** (`PROJECT/src/dashboard/`)
   - Flask-based web dashboard
   - Interactive data visualizations
   - Player and team comparison tools

### Data Flow

1. Data is collected through web scraping and API calls
2. Raw data is processed and stored in a database
3. Analysis modules calculate metrics and generate insights
4. Visualization components present data through a web interface

## Weekly Workflow

For each week of the course:
1. Watch the required course videos listed in the README
2. Read the README files for each challenge
3. Implement the required functions in the Python files
4. Run the files to test your implementations
5. Create a pull request with your completed assignments

## Code Style Guidelines

The project follows PEP 8 style guidelines:
- Use Black for code formatting
- Use flake8 for linting
- Use isort for import sorting