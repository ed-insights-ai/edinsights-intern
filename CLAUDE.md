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

## Development Environment

### Setup

1. **Python Environment**:
   - Python 3.12+ required
   - Create a virtual environment: `uv create venv`
   - Activate the environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

2. **Install Dependencies**:
   ```
   pip install -r PROJECT/requirements.txt
   ```

## Common Commands

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

## Testing Approach

- Tests are located in `PROJECT/tests/`
- Uses pytest for unit and integration testing
- Test fixtures provide sample player data
- Tests verify metric calculations and data processing functions

## Code Style Guidelines

The project follows PEP 8 style guidelines:
- Use Black for code formatting
- Use flake8 for linting
- Use isort for import sorting