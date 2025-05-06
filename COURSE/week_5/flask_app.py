"""
Flask Web Application
-----------------
Build a Flask web application for displaying and managing soccer statistics.
This exercise focuses on creating a web interface with Flask.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("flask_app.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'development-key')  # In production, use an environment variable

# Sample data path
DATA_DIR = 'data'
PLAYERS_FILE = os.path.join(DATA_DIR, 'players.json')
TEAMS_FILE = os.path.join(DATA_DIR, 'teams.json')

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

def load_data(filepath, default=None):
    """Load data from a JSON file or return default if file doesn't exist."""
    if default is None:
        default = []
    
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        else:
            return default
    except Exception as e:
        logger.error(f"Error loading data from {filepath}: {e}")
        return default

def save_data(filepath, data):
    """Save data to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving data to {filepath}: {e}")
        return False

# Initialize with sample data if files don't exist
def init_sample_data():
    """Initialize sample data if files don't exist."""
    # Sample teams
    if not os.path.exists(TEAMS_FILE):
        teams = [
            {"id": "t1", "name": "Western State", "location": "Gunnison, CO", "conference": "RMAC"},
            {"id": "t2", "name": "Eastern College", "location": "Boston, MA", "conference": "NE-10"},
            {"id": "t3", "name": "Northern University", "location": "Minneapolis, MN", "conference": "NSIC"}
        ]
        save_data(TEAMS_FILE, teams)
    
    # Sample players
    if not os.path.exists(PLAYERS_FILE):
        players = [
            {"id": "p1", "first_name": "John", "last_name": "Smith", "team_id": "t1", "position": "F", 
             "stats": {"games_played": 20, "goals": 12, "assists": 8}},
            {"id": "p2", "first_name": "Maria", "last_name": "Garcia", "team_id": "t2", "position": "MF", 
             "stats": {"games_played": 18, "goals": 5, "assists": 10}},
            {"id": "p3", "first_name": "David", "last_name": "Johnson", "team_id": "t3", "position": "D", 
             "stats": {"games_played": 19, "goals": 1, "assists": 3}}
        ]
        save_data(PLAYERS_FILE, players)

# Initialize sample data
init_sample_data()

@app.route('/')
def index():
    """Render the home page."""
    # YOUR CODE HERE
    pass

@app.route('/players')
def list_players():
    """Render the players list page."""
    # YOUR CODE HERE
    pass

@app.route('/players/<player_id>')
def player_detail(player_id):
    """Render the player detail page."""
    # YOUR CODE HERE
    pass

@app.route('/players/new', methods=['GET', 'POST'])
def new_player():
    """Render the new player form and handle form submission."""
    # YOUR CODE HERE
    pass

@app.route('/players/<player_id>/edit', methods=['GET', 'POST'])
def edit_player(player_id):
    """Render the edit player form and handle form submission."""
    # YOUR CODE HERE
    pass

@app.route('/players/<player_id>/delete', methods=['POST'])
def delete_player(player_id):
    """Handle player deletion."""
    # YOUR CODE HERE
    pass

@app.route('/teams')
def list_teams():
    """Render the teams list page."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<team_id>')
def team_detail(team_id):
    """Render the team detail page."""
    # YOUR CODE HERE
    pass

@app.route('/teams/new', methods=['GET', 'POST'])
def new_team():
    """Render the new team form and handle form submission."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<team_id>/edit', methods=['GET', 'POST'])
def edit_team(team_id):
    """Render the edit team form and handle form submission."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<team_id>/delete', methods=['POST'])
def delete_team(team_id):
    """Handle team deletion."""
    # YOUR CODE HERE
    pass

@app.route('/search')
def search():
    """Handle search functionality."""
    # YOUR CODE HERE
    pass

@app.route('/api/players')
def api_players():
    """API endpoint to get players as JSON."""
    # YOUR CODE HERE
    pass

@app.route('/api/teams')
def api_teams():
    """API endpoint to get teams as JSON."""
    # YOUR CODE HERE
    pass

@app.route('/api/players/<player_id>')
def api_player_detail(player_id):
    """API endpoint to get player details as JSON."""
    # YOUR CODE HERE
    pass

@app.route('/api/teams/<team_id>')
def api_team_detail(team_id):
    """API endpoint to get team details as JSON."""
    # YOUR CODE HERE
    pass

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('error.html', error=e), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return render_template('error.html', error=e), 500

def create_templates():
    """Create basic template files if they don't exist."""
    templates_dir = os.path.join(app.root_path, 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # Create a basic layout template
    layout_path = os.path.join(templates_dir, 'layout.html')
    if not os.path.exists(layout_path):
        with open(layout_path, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Soccer Stats{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('list_players') }}">Players</a></li>
                <li><a href="{{ url_for('list_teams') }}">Teams</a></li>
                <li><a href="{{ url_for('search') }}">Search</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="flashes">
                    {% for message in messages %}
                        <div class="flash">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; {{ now.year }} Soccer Stats App</p>
    </footer>
    
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
""")
    
    # Create basic index template
    index_path = os.path.join(templates_dir, 'index.html')
    if not os.path.exists(index_path):
        with open(index_path, 'w') as f:
            f.write("""{% extends "layout.html" %}

{% block title %}Home - Soccer Stats{% endblock %}

{% block content %}
    <h1>NCAA Soccer Statistics</h1>
    <p>Welcome to the Soccer Statistics Dashboard.</p>
    
    <div class="dashboard">
        <div class="widget">
            <h2>Player Statistics</h2>
            <p>View and manage player statistics.</p>
            <a href="{{ url_for('list_players') }}" class="button">View Players</a>
        </div>
        
        <div class="widget">
            <h2>Team Statistics</h2>
            <p>View and manage team statistics.</p>
            <a href="{{ url_for('list_teams') }}" class="button">View Teams</a>
        </div>
        
        <div class="widget">
            <h2>Search</h2>
            <p>Search for players and teams.</p>
            <a href="{{ url_for('search') }}" class="button">Search</a>
        </div>
    </div>
{% endblock %}
""")
    
    # Create error template
    error_path = os.path.join(templates_dir, 'error.html')
    if not os.path.exists(error_path):
        with open(error_path, 'w') as f:
            f.write("""{% extends "layout.html" %}

{% block title %}Error{% endblock %}

{% block content %}
    <h1>Error</h1>
    <p>{{ error }}</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
{% endblock %}
""")
    
    # Create static directory and basic CSS
    static_dir = os.path.join(app.root_path, 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    css_path = os.path.join(static_dir, 'style.css')
    if not os.path.exists(css_path):
        with open(css_path, 'w') as f:
            f.write("""/* Basic styles for the Soccer Stats app */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem;
}

nav ul {
    list-style: none;
    display: flex;
    margin: 0;
    padding: 0;
}

nav li {
    margin-right: 1rem;
}

nav a {
    color: white;
    text-decoration: none;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem;
}

footer {
    background-color: #f8f9fa;
    padding: 1rem;
    text-align: center;
    margin-top: 2rem;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
}

.widget {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1rem;
    background-color: #f8f9fa;
}

.button {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 4px;
}

.flashes {
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
    color: #721c24;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border-radius: 4px;
}
""")

@app.context_processor
def inject_now():
    """Add current date to template context."""
    return {'now': datetime.now()}

if __name__ == '__main__':
    # Create template files
    create_templates()
    
    print("Flask Web Application")
    print("Available routes:")
    print("  /                  - Home page")
    print("  /players           - List players")
    print("  /players/<id>      - Player details")
    print("  /players/new       - Create new player")
    print("  /players/<id>/edit - Edit player")
    print("  /teams             - List teams")
    print("  /teams/<id>        - Team details")
    print("  /teams/new         - Create new team")
    print("  /teams/<id>/edit   - Edit team")
    print("  /search            - Search functionality")
    print("  /api/players       - API endpoint for players")
    print("  /api/teams         - API endpoint for teams")
    print("\nRunning on http://127.0.0.1:5000/")
    
    app.run(debug=True)