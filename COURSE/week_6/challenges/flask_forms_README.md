# Challenge 3: Flask-WTF Forms for Soccer Analytics

**Difficulty: ⭐⭐⭐⭐☆**

## Challenge Overview

In this challenge, you'll create web forms using Flask-WTF that will allow users to interact with your soccer analytics database. These forms will enable data entry, editing, and searching, providing a user-friendly interface for managing and querying NCAA soccer data.

## Learning Objectives

- Understand web form creation and processing in Flask
- Implement form validation and error handling
- Create custom validators for sports-specific data
- Connect forms to database operations
- Build search and filtering interfaces

## Real-World Context

Sports analytics platforms need user interfaces that allow coaches, players, and analysts to enter and retrieve data. Form-based interfaces provide a structured way to collect information about matches, player performances, and team statistics. NCAA soccer programs use these interfaces to update player information, record match results, and search for specific statistics to inform their decision-making.

## Challenge Details

### The Task

Create Flask-WTF forms that:

1. Allow users to add, edit, and search for players, teams, matches, and statistics
2. Implement validation rules for each form field
3. Include custom validators for soccer-specific data
4. Connect to your database operations
5. Provide a user-friendly interface for interacting with soccer data

### Form Hierarchy and Flow

```
+---------------------+
|     Base Forms      |
+---------------------+
         /|\
          |
+----------+----------+----------+----------+
|          |          |          |          |
v          v          v          v          v
+------+  +------+  +------+  +--------+  +------+
|Player|  | Team |  |Match |  |PlayerStat|  |Search|
|Form  |  | Form |  | Form |  |  Form   |  | Forms|
+------+  +------+  +------+  +--------+  +------+
    |        |         |          |           |
    v        v         v          v           v
+---------------------------------------------+
|             Form Processing                 |
+---------------------------------------------+
    |        |         |          |           |
    v        v         v          v           v
+---------------------------------------------+
|             Database Operations             |
+---------------------------------------------+
```

## Tips and Hints

### Basic Form Structure

A typical Flask-WTF form looks like this:

```python
class PlayerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    jersey_number = IntegerField('Jersey Number', validators=[DataRequired(), NumberRange(min=1, max=99)])
    position = SelectField('Position', choices=[
        ('', 'Select a position'),
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward')
    ], validators=[DataRequired()])
    birth_date = DateField('Birth Date', validators=[Optional()])
    height_cm = IntegerField('Height (cm)', validators=[Optional(), NumberRange(min=150, max=220)])
    weight_kg = FloatField('Weight (kg)', validators=[Optional(), NumberRange(min=50, max=120)])
    submit = SubmitField('Save Player')
```

### Custom Validators

You can create custom validators for soccer-specific data:

```python
def validate_jersey_number(form, field):
    """Validate that jersey numbers are in a valid range."""
    if field.data is not None and (field.data < 1 or field.data > 99):
        raise ValidationError('Jersey number must be between 1 and 99')

class PlayerForm(FlaskForm):
    jersey_number = IntegerField('Jersey Number', validators=[
        DataRequired(), 
        NumberRange(min=1, max=99),
        validate_jersey_number
    ])
    # Other fields...
```

### Form Processing in Flask Routes

Here's how you might process a form in a Flask route:

```python
@app.route('/player/add', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    
    if form.validate_on_submit():
        # Get data from the form
        player_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'jersey_number': form.jersey_number.data,
            'position': form.position.data,
            'birth_date': form.birth_date.data,
            'height_cm': form.height_cm.data,
            'weight_kg': form.weight_kg.data,
            'team_id': form.team_id.data
        }
        
        # Create a new player in the database
        Player.create(db.session, **player_data)
        
        flash('Player added successfully!', 'success')
        return redirect(url_for('player_list'))
        
    return render_template('add_player.html', form=form)
```

### Search and Filter Forms

Search forms allow users to filter data based on various criteria:

```python
class PlayerSearchForm(FlaskForm):
    name = StringField('Player Name', validators=[Optional()])
    position = SelectField('Position', choices=[
        ('', 'All Positions'),
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward')
    ], validators=[Optional()])
    team = SelectField('Team', validators=[Optional()])
    min_goals = IntegerField('Minimum Goals', validators=[Optional(), NumberRange(min=0)])
    max_goals = IntegerField('Maximum Goals', validators=[Optional(), NumberRange(min=0)])
    season = SelectField('Season', validators=[Optional()])
    submit = SubmitField('Search')
    
    def __init__(self, *args, **kwargs):
        super(PlayerSearchForm, self).__init__(*args, **kwargs)
        # Populate team choices from database
        self.team.choices = [('', 'All Teams')] + [
            (str(team.id), team.name) for team in Team.get_all(db.session)
        ]
        # Populate season choices from database
        self.season.choices = [('', 'All Seasons')] + [
            (season, season) for season in get_all_seasons(db.session)
        ]
```

### Processing Search Forms

Search forms require special handling to build dynamic queries:

```python
@app.route('/player/search', methods=['GET', 'POST'])
def search_players():
    form = PlayerSearchForm()
    players = []
    
    if form.validate_on_submit() or request.args:
        # Get search parameters
        name = form.name.data or request.args.get('name', '')
        position = form.position.data or request.args.get('position', '')
        team_id = form.team.data or request.args.get('team', '')
        min_goals = form.min_goals.data or request.args.get('min_goals', 0)
        max_goals = form.max_goals.data or request.args.get('max_goals', '')
        season = form.season.data or request.args.get('season', '')
        
        # Build the query
        query = db.session.query(Player)
        
        if name:
            # Search in both first and last name
            query = query.filter(
                (Player.first_name.ilike(f'%{name}%')) |
                (Player.last_name.ilike(f'%{name}%'))
            )
        
        if position:
            query = query.filter(Player.position == position)
            
        if team_id:
            query = query.filter(Player.team_id == int(team_id))
        
        # Apply goals filtering if searching by season
        if season and (min_goals or max_goals is not None):
            # Join with statistics to filter by goals
            # This requires a more complex query...
            pass
            
        players = query.all()
        
    return render_template('search_players.html', form=form, players=players)
```

## Testing Your Solution

Your solution should:

1. Create forms for all major entities (players, teams, matches, statistics)
2. Implement validation rules for each form field
3. Include custom validators for soccer-specific data
4. Provide search and filtering functionality
5. Connect to your database operations

Test your forms by:

1. Rendering them in templates
2. Submitting valid and invalid data
3. Verifying that validation rules work as expected
4. Checking that form data is correctly processed
5. Ensuring that search forms return the expected results

## Application to Capstone

The forms you create in this challenge will be used in your capstone project to:

1. Provide a user interface for managing soccer data
2. Enable data entry for manual statistics recording
3. Create search and filtering capabilities for data analysis
4. Ensure data integrity through validation
5. Enhance the user experience of your web application

A well-designed form system will make your capstone project more usable and help maintain the quality of your soccer data.

## Resources

- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [WTForms Field Types](https://wtforms.readthedocs.io/en/2.3.x/fields/)
- [WTForms Validators](https://wtforms.readthedocs.io/en/2.3.x/validators/)
- [Flask Form Handling Tutorial](https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/)
- [Custom Form Validators](https://wtforms.readthedocs.io/en/2.3.x/validators/#custom-validators)
- [Flask Flash Messages](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/)
- [Bootstrap Form Styling](https://getbootstrap.com/docs/5.0/forms/overview/)