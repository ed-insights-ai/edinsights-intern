# Challenge 3: Soccer Analytics Flask Web Application

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll build a Flask web application that displays soccer player and team statistics. This will serve as a prototype for your capstone project's interactive dashboard, allowing users to view, search, and filter NCAA soccer data.

## Learning Objectives

- Set up a Flask application with proper structure
- Create HTML templates with Jinja2
- Implement route handling and URL parameters
- Build form handling and data filtering
- Create a simple REST API endpoint
- Understand the basics of web application architecture

## Real-World Context

Sports analytics platforms need interactive web interfaces to make data accessible to coaches, players, and analysts. Flask is a lightweight web framework that allows you to quickly build such interfaces. NCAA Division II soccer programs could use an application like this to analyze player performance, compare statistics, and make data-driven decisions about training and game strategies.

## Challenge Details

### The Task

Create a Flask web application that:
1. Displays a home page with summary statistics
2. Shows detailed player statistics with filtering options
3. Displays team statistics and comparisons
4. Includes a basic REST API endpoint for accessing player data programmatically
5. Provides a simple visualization of key metrics

### Application Structure

```
flask_app.py
/templates
    /base.html         # Base template with navigation and structure
    /home.html         # Home page template
    /players.html      # Player statistics page
    /teams.html        # Team statistics page
    /player_detail.html # Individual player details
/static
    /css
        /style.css     # CSS styles for your application
    /js
        /app.js        # JavaScript for interactive elements
    /images
        /logo.png      # Sample logo
```

### Flask Application Routes

```
/ (home)
    - Displays welcome message and summary statistics
    - Links to other pages

/players
    - Shows a table of player statistics
    - Includes filter/search functionality
    - Links to individual player detail pages

/teams
    - Displays team statistics
    - Allows comparisons between teams

/player/<player_id>
    - Shows detailed stats for a specific player
    - Links back to the players list

/api/players
    - REST API endpoint returning player data as JSON
    - Accepts filter parameters
```

## Tips and Hints

### Basic Flask Application Structure

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Soccer Analytics Dashboard')

if __name__ == '__main__':
    app.run(debug=True)
```

### Template Inheritance with Jinja2

**base.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>NCAA Soccer Analytics</h1>
        <nav>
            <ul>
                <li><a href="{{ url_for('home') }}">Home</a></li>
                <li><a href="{{ url_for('players') }}">Players</a></li>
                <li><a href="{{ url_for('teams') }}">Teams</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>NCAA Soccer Analytics Dashboard</p>
    </footer>
    
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
</body>
</html>
```

**players.html**:
```html
{% extends "base.html" %}

{% block content %}
<h2>Player Statistics</h2>

<form method="GET" action="{{ url_for('players') }}">
    <input type="text" name="search" placeholder="Search players..." value="{{ request.args.get('search', '') }}">
    <select name="position">
        <option value="">All Positions</option>
        <option value="Forward" {% if request.args.get('position') == 'Forward' %}selected{% endif %}>Forward</option>
        <option value="Midfielder" {% if request.args.get('position') == 'Midfielder' %}selected{% endif %}>Midfielder</option>
        <option value="Defender" {% if request.args.get('position') == 'Defender' %}selected{% endif %}>Defender</option>
        <option value="Goalkeeper" {% if request.args.get('position') == 'Goalkeeper' %}selected{% endif %}>Goalkeeper</option>
    </select>
    <button type="submit">Filter</button>
</form>

<table class="stats-table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Position</th>
            <th>Goals</th>
            <th>Assists</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for player in players %}
        <tr>
            <td>{{ player.name }}</td>
            <td>{{ player.position }}</td>
            <td>{{ player.goals }}</td>
            <td>{{ player.assists }}</td>
            <td>
                <a href="{{ url_for('player_detail', player_id=player.id) }}">Details</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

### Handling Query Parameters for Filtering

```python
@app.route('/players')
def players():
    search = request.args.get('search', '')
    position = request.args.get('position', '')
    
    # Filter players based on search and position
    filtered_players = []
    for player in SAMPLE_PLAYERS:
        if (not search or search.lower() in player['name'].lower()) and \
           (not position or player['position'] == position):
            filtered_players.append(player)
    
    return render_template('players.html', players=filtered_players, title='Player Statistics')
```

### Creating a Simple API Endpoint

```python
@app.route('/api/players')
def api_players():
    search = request.args.get('search', '')
    position = request.args.get('position', '')
    
    # Filter players based on search and position
    filtered_players = []
    for player in SAMPLE_PLAYERS:
        if (not search or search.lower() in player['name'].lower()) and \
           (not position or player['position'] == position):
            filtered_players.append(player)
    
    return jsonify(players=filtered_players)
```

## Testing Your Solution

Your solution should:
1. Start a web server that displays the home page
2. Allow navigation between different pages
3. Display player and team statistics
4. Filter players based on search terms and position
5. Show detailed information for individual players
6. Return JSON data through the API endpoint

Try these test cases:
1. Visit the home page and navigate to the players page
2. Search for a player by name
3. Filter players by position
4. View details for a specific player
5. Access the API endpoint with different filter parameters

## Application to Capstone

For your capstone project, you'll expand this Flask application to:
1. Connect to a database with real NCAA soccer data
2. Implement more sophisticated filtering and search
3. Add advanced data visualizations
4. Include more detailed player and team analysis
5. Add authentication for private data

This challenge establishes the foundation for your capstone project's web interface, letting you focus on the features that make your analytics platform unique and valuable to NCAA soccer programs.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/en/3.0.x/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [HTML Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
- [RESTful API Design](https://restfulapi.net/)