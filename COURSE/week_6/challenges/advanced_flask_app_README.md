# Challenge 4: Advanced Flask Application for Soccer Analytics

**Difficulty: ⭐⭐⭐⭐☆**

## Challenge Overview

In this challenge, you'll build an advanced Flask web application that provides a complete interface to your soccer analytics database. This application will include user authentication, CRUD operations, a dashboard for visualizing key metrics, and a simple API for programmatic access to soccer data.

## Learning Objectives

- Build a full-featured web application with Flask
- Implement user authentication and authorization
- Create routes for all CRUD operations
- Design a dashboard for visualizing key metrics
- Implement RESTful API endpoints
- Use Bootstrap for responsive design

## Real-World Context

NCAA soccer programs use web-based analytics platforms to track player performance, analyze team statistics, and make data-driven decisions. These applications need to be secure, user-friendly, and provide various ways to access and visualize data. Coaches, players, and analysts rely on these systems to review past performance, identify trends, and develop strategic insights for upcoming matches.

## Challenge Details

### The Task

Create a Flask web application that:

1. Implements user authentication and authorization
2. Provides CRUD operations for all database models
3. Includes a dashboard for visualizing key soccer metrics
4. Offers search and filtering functionality
5. Implements RESTful API endpoints for programmatic access
6. Uses Bootstrap for responsive design

### Application Architecture

```
+-------------------------------------+
|             Client Browser          |
+-------------------------------------+
                   |
                   v
+-------------------------------------+
|             Flask Application       |
+-------------------------------------+
|                                     |
|  +-------------------------------+  |
|  |       Authentication          |  |
|  +-------------------------------+  |
|                                     |
|  +-------------------------------+  |
|  |     Routes & Controllers      |  |
|  +-------------------------------+  |
|                                     |
|  +-------------------------------+  |
|  |       Templates & Forms       |  |
|  +-------------------------------+  |
|                                     |
|  +-------------------------------+  |
|  |       API Endpoints           |  |
|  +-------------------------------+  |
|                                     |
+-------------------------------------+
                   |
                   v
+-------------------------------------+
|        SQLAlchemy ORM Layer         |
+-------------------------------------+
                   |
                   v
+-------------------------------------+
|           Database                  |
+-------------------------------------+
```

## Tips and Hints

### Application Structure

A well-organized Flask application might have this structure:

```
/advanced_flask_app.py    # Main application file
/templates/               # Jinja2 templates
    /base.html            # Base template with common elements
    /auth/                # Authentication templates
        /login.html
        /register.html
    /players/             # Player-related templates
        /index.html
        /detail.html
        /form.html
    /teams/               # Team-related templates
    /matches/             # Match-related templates
    /stats/               # Statistics templates
    /dashboard.html       # Dashboard template
/static/                  # Static files
    /css/
    /js/
    /images/
```

### User Authentication

Flask-Login provides a simple way to handle user authentication:

```python
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Set up Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('auth/login.html')
```

### CRUD Routes

Here's an example of CRUD routes for players:

```python
@app.route('/players')
@login_required
def player_list():
    """Route for listing players."""
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    players = Player.query.paginate(page=page, per_page=per_page)
    
    return render_template('players/index.html', players=players)

@app.route('/player/<int:player_id>')
@login_required
def player_detail(player_id):
    """Route for viewing player details."""
    player = Player.query.get_or_404(player_id)
    return render_template('players/detail.html', player=player)

@app.route('/player/add', methods=['GET', 'POST'])
@login_required
def player_add():
    """Route for adding a new player."""
    form = PlayerForm()
    
    if form.validate_on_submit():
        player = Player()
        form.populate_obj(player)
        db.session.add(player)
        db.session.commit()
        
        flash('Player added successfully!', 'success')
        return redirect(url_for('player_detail', player_id=player.id))
        
    return render_template('players/form.html', form=form, title='Add Player')

@app.route('/player/<int:player_id>/edit', methods=['GET', 'POST'])
@login_required
def player_edit(player_id):
    """Route for editing a player."""
    player = Player.query.get_or_404(player_id)
    form = PlayerForm(obj=player)
    
    if form.validate_on_submit():
        form.populate_obj(player)
        db.session.commit()
        
        flash('Player updated successfully!', 'success')
        return redirect(url_for('player_detail', player_id=player.id))
        
    return render_template('players/form.html', form=form, title='Edit Player')

@app.route('/player/<int:player_id>/delete', methods=['POST'])
@login_required
def player_delete(player_id):
    """Route for deleting a player."""
    player = Player.query.get_or_404(player_id)
    
    db.session.delete(player)
    db.session.commit()
    
    flash('Player deleted successfully!', 'success')
    return redirect(url_for('player_list'))
```

### API Endpoints

You can create RESTful API endpoints like this:

```python
@app.route('/api/players')
def api_players():
    """API endpoint for accessing player data."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    # Get filter parameters
    name = request.args.get('name', '')
    position = request.args.get('position', '')
    team_id = request.args.get('team_id')
    
    # Build the query
    query = Player.query
    
    if name:
        query = query.filter(
            (Player.first_name.ilike(f'%{name}%')) | 
            (Player.last_name.ilike(f'%{name}%'))
        )
        
    if position:
        query = query.filter(Player.position == position)
        
    if team_id:
        query = query.filter(Player.team_id == int(team_id))
    
    # Paginate the results
    paginated = query.paginate(page=page, per_page=per_page)
    
    # Prepare the response
    result = {
        'players': [
            {
                'id': player.id,
                'first_name': player.first_name,
                'last_name': player.last_name,
                'position': player.position,
                'team_id': player.team_id,
                # Include other fields as needed
            }
            for player in paginated.items
        ],
        'pagination': {
            'page': paginated.page,
            'per_page': paginated.per_page,
            'total_pages': paginated.pages,
            'total_items': paginated.total
        }
    }
    
    return jsonify(result)
```

### Dashboard

The dashboard can showcase key soccer metrics:

```python
@app.route('/dashboard')
@login_required
def dashboard():
    """Route for the main dashboard."""
    # Get summary statistics
    total_players = Player.query.count()
    total_teams = Team.query.count()
    total_matches = Match.query.count()
    
    # Get top scorers
    top_scorers = db.session.query(
        Player, 
        db.func.sum(PlayerMatchStatistic.goals).label('total_goals')
    ).join(
        PlayerMatchStatistic
    ).group_by(
        Player.id
    ).order_by(
        db.desc('total_goals')
    ).limit(5).all()
    
    # Get recent matches
    recent_matches = Match.query.order_by(Match.date.desc()).limit(5).all()
    
    # Get team performance
    team_performance = db.session.query(
        Team,
        db.func.count(Match.id).label('total_matches'),
        db.func.sum(case(
            [(Match.home_team_id == Team.id, Match.home_score > Match.away_score),
             (Match.away_team_id == Team.id, Match.away_score > Match.home_score)],
            else_=False
        )).label('wins'),
        db.func.sum(case(
            [(Match.home_team_id == Team.id, Match.home_score < Match.away_score),
             (Match.away_team_id == Team.id, Match.away_score < Match.home_score)],
            else_=False
        )).label('losses')
    ).outerjoin(
        Match, 
        (Team.id == Match.home_team_id) | (Team.id == Match.away_team_id)
    ).group_by(
        Team.id
    ).all()
    
    return render_template(
        'dashboard.html',
        total_players=total_players,
        total_teams=total_teams,
        total_matches=total_matches,
        top_scorers=top_scorers,
        recent_matches=recent_matches,
        team_performance=team_performance
    )
```

## Testing Your Solution

Your solution should:

1. Implement user authentication and authorization
2. Provide routes for CRUD operations on all models
3. Include a dashboard with key metrics and visualizations
4. Offer search and filtering functionality
5. Implement RESTful API endpoints
6. Use Bootstrap for responsive design

Test your application by:

1. Registering users and testing authentication
2. Performing CRUD operations on all models
3. Verifying that the dashboard displays correct metrics
4. Testing search and filter functionality
5. Accessing API endpoints with different parameters
6. Checking that the application is responsive on different devices

## Application to Capstone

The advanced Flask application you create in this challenge will serve as the web interface for your capstone project. It will:

1. Provide secure access to your soccer analytics platform
2. Allow users to view and analyze NCAA soccer data
3. Enable manual data entry and editing
4. Visualize key metrics and trends
5. Offer programmatic access through API endpoints

This application will be the main way that users interact with your capstone project, so focus on creating a clean, intuitive, and responsive user interface.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [RESTful API Design](https://flask.palletsprojects.com/en/2.0.x/tutorial/views/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Chart.js for Data Visualization](https://www.chartjs.org/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.0.x/security/)