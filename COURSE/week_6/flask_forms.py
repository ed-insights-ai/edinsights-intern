"""
CHALLENGE: Flask-WTF Forms for Soccer Analytics

Your task is to create web forms using Flask-WTF that will allow users to interact with
your soccer analytics database. These forms will enable users to add, edit, and filter
soccer data through a web interface.

REQUIREMENTS:
- Create forms for all major data entities (players, teams, matches, etc.)
- Implement validation rules for each form field
- Add custom validators for soccer-specific data
- Create search/filter forms for querying the database
- Connect forms to Flask routes and templates
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, DateField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional, ValidationError
import datetime
from typing import List, Dict, Any

# Create Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for CSRF protection

# TODO: Implement your forms below

class PlayerForm(FlaskForm):
    """
    Form for adding and editing player information.
    
    This form should include all relevant fields for a soccer player, along with
    appropriate validators to ensure data integrity.
    """
    # TODO: Add form fields with appropriate validators
    # Example:
    # first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    # last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    
    # TODO: Add custom validators if needed
    
    # TODO: Add submit button
    # submit = SubmitField('Save Player')
    
    pass


class TeamForm(FlaskForm):
    """
    Form for adding and editing team information.
    
    This form should include all relevant fields for a soccer team, along with
    appropriate validators to ensure data integrity.
    """
    # TODO: Add form fields with appropriate validators
    
    pass


class MatchForm(FlaskForm):
    """
    Form for adding and editing match information.
    
    This form should include all relevant fields for a soccer match, along with
    appropriate validators to ensure data integrity.
    """
    # TODO: Add form fields with appropriate validators
    
    pass


class PlayerStatisticsForm(FlaskForm):
    """
    Form for adding and editing player match statistics.
    
    This form should include all relevant fields for tracking a player's performance
    in a match, along with appropriate validators to ensure data integrity.
    """
    # TODO: Add form fields with appropriate validators
    
    pass


class PlayerSearchForm(FlaskForm):
    """
    Form for searching and filtering players.
    
    This form should include fields that allow users to search for players based on
    various criteria such as name, position, team, or statistical thresholds.
    """
    # TODO: Add search/filter fields
    # Example:
    # name = StringField('Player Name', validators=[Optional()])
    # position = SelectField('Position', choices=[('', 'All'), ('Forward', 'Forward'), ('Midfielder', 'Midfielder'), 
    #                                          ('Defender', 'Defender'), ('Goalkeeper', 'Goalkeeper')], validators=[Optional()])
    # min_goals = IntegerField('Minimum Goals', validators=[Optional(), NumberRange(min=0)])
    
    # TODO: Add submit button
    # submit = SubmitField('Search')
    
    pass


class TeamSearchForm(FlaskForm):
    """
    Form for searching and filtering teams.
    
    This form should include fields that allow users to search for teams based on
    various criteria such as name, conference, or performance metrics.
    """
    # TODO: Add search/filter fields
    
    pass


# Custom validator examples

def validate_jersey_number(form, field):
    """
    Custom validator for jersey numbers.
    
    Args:
        form: The form containing the field
        field: The field to validate
    
    Raises:
        ValidationError: If the jersey number is invalid
    """
    if field.data is not None and (field.data < 1 or field.data > 99):
        raise ValidationError('Jersey number must be between 1 and 99')


def validate_match_date(form, field):
    """
    Custom validator for match dates.
    
    Args:
        form: The form containing the field
        field: The field to validate
    
    Raises:
        ValidationError: If the match date is invalid
    """
    if field.data > datetime.date.today():
        raise ValidationError('Match date cannot be in the future')


# Example Flask routes for using forms

@app.route('/player/add', methods=['GET', 'POST'])
def add_player():
    """
    Route for adding a new player.
    
    This route should display a form for adding a player and process
    the form submission to create a new player in the database.
    """
    # TODO: Implement this route
    # Example:
    # form = PlayerForm()
    # if form.validate_on_submit():
    #     # Process form data and add player to database
    #     # ...
    #     flash('Player added successfully!', 'success')
    #     return redirect(url_for('player_list'))
    # return render_template('add_player.html', form=form)
    
    pass


@app.route('/player/search', methods=['GET', 'POST'])
def search_players():
    """
    Route for searching players.
    
    This route should display a form for searching/filtering players and
    process the form submission to display matching players.
    """
    # TODO: Implement this route
    
    pass


def main():
    """
    Main function to run the Flask application.
    """
    # This is just for illustration - in a real app, you'd use proper configuration
    # and run the app using a proper server
    app.run(debug=True)


if __name__ == "__main__":
    main()