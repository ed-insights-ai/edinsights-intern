"""
Advanced Flask Application
----------------------
Build an advanced Flask application with database integration, authentication, and CRUD operations.
This exercise combines all the elements from previous exercises.
"""

from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, session, g
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
import os
import logging
import datetime
import json
import re
from functools import wraps

# Import forms (in a real application, these would be imported from flask_forms.py)
# Since we don't want to import from a separate file for this exercise, we'll define them here
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, DateField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional, ValidationError

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("advanced_flask_app.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')  # In production, use environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soccer_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Set up database
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)

# Define database models
# These would typically be in a separate file (orm_models.py)
class User(Base, UserMixin):
    """User model for authentication."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    def set_password(self, password):
        """Set the password hash."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check the password against the hash."""
        return check_password_hash(self.password_hash, password)

# Import the models from orm_models.py
# For this exercise, we'll define simplified versions of the models here
class Team(Base):
    """Team model."""
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100))
    conference = Column(String(100))
    
    players = relationship('Player', back_populates='team')

class Player(Base):
    """Player model."""
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))
    position = Column(String(10))
    jersey_number = Column(Integer)
    
    team = relationship('Team', back_populates='players')
    stats = relationship('PlayerStats', back_populates='player')

class Match(Base):
    """Match model."""
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime)
    location = Column(String(100))
    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)
    
    home_team = relationship('Team', foreign_keys=[home_team_id])
    away_team = relationship('Team', foreign_keys=[away_team_id])
    player_stats = relationship('PlayerStats', back_populates='match')

class PlayerStats(Base):
    """Player statistics model."""
    __tablename__ = 'player_stats'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    match_id = Column(Integer, ForeignKey('matches.id'))
    minutes_played = Column(Integer, default=0)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    shots = Column(Integer, default=0)
    shots_on_goal = Column(Integer, default=0)
    
    player = relationship('Player', back_populates='stats')
    match = relationship('Match', back_populates='player_stats')

# Forms (for brevity, defining only a few key forms)
class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    """Registration form."""
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class TeamForm(FlaskForm):
    """Team form."""
    name = StringField('Team Name', validators=[DataRequired(), Length(max=100)])
    location = StringField('Location', validators=[Length(max=100)])
    conference = StringField('Conference', validators=[Length(max=100)])
    submit = SubmitField('Submit')

class PlayerForm(FlaskForm):
    """Player form."""
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    team_id = SelectField('Team', coerce=int, validators=[DataRequired()])
    position = SelectField('Position', choices=[
        ('F', 'Forward'), 
        ('MF', 'Midfielder'), 
        ('D', 'Defender'), 
        ('GK', 'Goalkeeper')
    ])
    jersey_number = IntegerField('Jersey Number', validators=[NumberRange(min=0, max=99)])
    submit = SubmitField('Submit')

class MatchForm(FlaskForm):
    """Match form."""
    home_team_id = SelectField('Home Team', coerce=int, validators=[DataRequired()])
    away_team_id = SelectField('Away Team', coerce=int, validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    location = StringField('Location', validators=[Length(max=100)])
    home_score = IntegerField('Home Score', default=0)
    away_score = IntegerField('Away Score', default=0)
    submit = SubmitField('Submit')

class PlayerStatsForm(FlaskForm):
    """Player stats form."""
    player_id = SelectField('Player', coerce=int, validators=[DataRequired()])
    match_id = SelectField('Match', coerce=int, validators=[DataRequired()])
    minutes_played = IntegerField('Minutes Played', validators=[NumberRange(min=0, max=120)])
    goals = IntegerField('Goals', default=0)
    assists = IntegerField('Assists', default=0)
    shots = IntegerField('Shots', default=0)
    shots_on_goal = IntegerField('Shots on Goal', default=0)
    submit = SubmitField('Submit')

# Setup login manager
@login_manager.user_loader
def load_user(user_id):
    """Load a user by ID."""
    return db_session.query(User).get(int(user_id))

# Create database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    Base.metadata.create_all(engine)
    
    # Create admin user if it doesn't exist
    admin = db_session.query(User).filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@example.com', is_admin=True)
        admin.set_password('adminpassword')
        db_session.add(admin)
        db_session.commit()

# Request handlers
@app.before_request
def before_request():
    """Set up database session before each request."""
    g.db_session = db_session()

@app.teardown_request
def teardown_request(exception=None):
    """Clean up database session after each request."""
    if hasattr(g, 'db_session'):
        g.db_session.close()

# Custom decorators
def admin_required(f):
    """Decorator to require admin privileges."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin privileges required', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    """Render the home page."""
    # YOUR CODE HERE
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    # YOUR CODE HERE
    pass

@app.route('/logout')
@login_required
def logout():
    """Handle user logout."""
    # YOUR CODE HERE
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    # YOUR CODE HERE
    pass

@app.route('/profile')
@login_required
def profile():
    """Show user profile."""
    # YOUR CODE HERE
    pass

# Team routes
@app.route('/teams')
def list_teams():
    """List all teams."""
    # YOUR CODE HERE
    pass

@app.route('/teams/new', methods=['GET', 'POST'])
@login_required
def new_team():
    """Create a new team."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<int:team_id>')
def view_team(team_id):
    """View a specific team."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<int:team_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    """Edit a specific team."""
    # YOUR CODE HERE
    pass

@app.route('/teams/<int:team_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_team(team_id):
    """Delete a specific team."""
    # YOUR CODE HERE
    pass

# Player routes
@app.route('/players')
def list_players():
    """List all players."""
    # YOUR CODE HERE
    pass

@app.route('/players/new', methods=['GET', 'POST'])
@login_required
def new_player():
    """Create a new player."""
    # YOUR CODE HERE
    pass

@app.route('/players/<int:player_id>')
def view_player(player_id):
    """View a specific player."""
    # YOUR CODE HERE
    pass

@app.route('/players/<int:player_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_player(player_id):
    """Edit a specific player."""
    # YOUR CODE HERE
    pass

@app.route('/players/<int:player_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_player(player_id):
    """Delete a specific player."""
    # YOUR CODE HERE
    pass

# Match routes
@app.route('/matches')
def list_matches():
    """List all matches."""
    # YOUR CODE HERE
    pass

@app.route('/matches/new', methods=['GET', 'POST'])
@login_required
def new_match():
    """Create a new match."""
    # YOUR CODE HERE
    pass

@app.route('/matches/<int:match_id>')
def view_match(match_id):
    """View a specific match."""
    # YOUR CODE HERE
    pass

@app.route('/matches/<int:match_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_match(match_id):
    """Edit a specific match."""
    # YOUR CODE HERE
    pass

@app.route('/matches/<int:match_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_match(match_id):
    """Delete a specific match."""
    # YOUR CODE HERE
    pass

# Player stats routes
@app.route('/stats/player/new', methods=['GET', 'POST'])
@login_required
def new_player_stats():
    """Create new player statistics."""
    # YOUR CODE HERE
    pass

@app.route('/stats/player/<int:stats_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_player_stats(stats_id):
    """Edit player statistics."""
    # YOUR CODE HERE
    pass

# API routes
@app.route('/api/teams')
def api_teams():
    """API endpoint for teams."""
    # YOUR CODE HERE
    pass

@app.route('/api/players')
def api_players():
    """API endpoint for players."""
    # YOUR CODE HERE
    pass

@app.route('/api/matches')
def api_matches():
    """API endpoint for matches."""
    # YOUR CODE HERE
    pass

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return render_template('error.html', error='Server error'), 500

def create_template_files():
    """Create basic template files if they don't exist."""
    templates_dir = os.path.join(app.root_path, 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # Create basic templates - similar to those in flask_app.py from Week 5
    # In a real application, you would create more comprehensive templates
    
    # Create static directory for CSS, JS, etc.
    static_dir = os.path.join(app.root_path, 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    # Create basic CSS file
    css_dir = os.path.join(static_dir, 'css')
    os.makedirs(css_dir, exist_ok=True)
    
    css_path = os.path.join(css_dir, 'style.css')
    if not os.path.exists(css_path):
        with open(css_path, 'w') as f:
            f.write("""/* Basic styles for Soccer Stats App */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
}

/* Add more CSS as needed */
""")

def main():
    """Run the Flask application."""
    print("Advanced Flask Application")
    print("In a real application, you would run this with Flask's development server")
    print("or a production server like Gunicorn or uWSGI.")
    
    # Create template files
    create_template_files()
    
    print("\nAvailable routes:")
    print("Authentication Routes:")
    print("  /login            - User login")
    print("  /logout           - User logout")
    print("  /register         - User registration")
    print("  /profile          - User profile")
    
    print("\nTeam Routes:")
    print("  /teams            - List all teams")
    print("  /teams/new        - Create a new team")
    print("  /teams/<id>       - View a specific team")
    print("  /teams/<id>/edit  - Edit a specific team")
    print("  /teams/<id>/delete - Delete a specific team")
    
    print("\nPlayer Routes:")
    print("  /players          - List all players")
    print("  /players/new      - Create a new player")
    print("  /players/<id>     - View a specific player")
    print("  /players/<id>/edit - Edit a specific player")
    print("  /players/<id>/delete - Delete a specific player")
    
    print("\nMatch Routes:")
    print("  /matches          - List all matches")
    print("  /matches/new      - Create a new match")
    print("  /matches/<id>     - View a specific match")
    print("  /matches/<id>/edit - Edit a specific match")
    print("  /matches/<id>/delete - Delete a specific match")
    
    print("\nAPI Routes:")
    print("  /api/teams        - Teams API endpoint")
    print("  /api/players      - Players API endpoint")
    print("  /api/matches      - Matches API endpoint")
    
    # In a real application, you would start the Flask server here
    # app.run(debug=True)

if __name__ == "__main__":
    main()