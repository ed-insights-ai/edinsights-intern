# Challenge 2: Soccer League Class Hierarchy

This challenge focuses on creating an object-oriented hierarchy of classes to model a soccer league system with teams, players, and staff members.

## Overview

Inheritance is a powerful OOP concept that allows you to create specialized classes based on more general ones. In soccer, there are many hierarchical relationships (e.g., a goalkeeper is a type of player, who is a type of person). This challenge will help you model these relationships using inheritance.

## Learning Focus

- Class inheritance and parent-child relationships
- Method overriding
- Polymorphism
- Abstract classes and concrete implementations
- Class hierarchies for modeling real-world relationships

## Classes to Implement

### 1. Base Classes

These form the foundation of your hierarchy. They may contain common attributes and methods that will be inherited by more specific classes.

#### `Person` Class (Base class)

**Tips:**
- This should be the most general class with basic person information
- Include common attributes like name, age, and nationality
- Define methods that are common to all people in the soccer domain

**Pseudocode:**
```
class Person:
    # Constructor
    function __init__(first_name, last_name, age, nationality):
        store first_name, last_name, age, nationality as attributes
    
    # Get full name
    function full_name():
        return first_name + " " + last_name
    
    # String representation
    function __str__():
        return formatted string with name, age, and nationality
```

### 2. Inheritance Level 1

These classes inherit directly from Person and specialize based on role in a soccer organization.

#### `Player` Class (Inherits from Person)

**Tips:**
- Add player-specific attributes and methods
- Override parent methods as needed
- Consider what all players have in common regardless of position

**Pseudocode:**
```
class Player inherits from Person:
    # Constructor
    function __init__(first_name, last_name, age, nationality, position, jersey_number, dominant_foot="right"):
        call parent constructor with first_name, last_name, age, nationality
        store position, jersey_number, dominant_foot as attributes
        initialize statistics (goals, assists, matches_played) to 0
    
    # Record a goal
    function score_goal():
        increment goals count
        return updated goals count
    
    # Record an assist
    function record_assist():
        increment assists count
        return updated assists count
    
    # Play in a match
    function play_match(minutes_played):
        increment matches_played
        store minutes_played
        return total matches played
    
    # String representation (override parent method)
    function __str__():
        return formatted string with name, position, and jersey number
```

#### `StaffMember` Class (Inherits from Person)

**Tips:**
- Add attributes and methods specific to non-player staff
- Consider different types of staff and their common characteristics
- Include role and responsibilities information

**Pseudocode:**
```
class StaffMember inherits from Person:
    # Constructor
    function __init__(first_name, last_name, age, nationality, role, years_of_experience):
        call parent constructor with first_name, last_name, age, nationality
        store role, years_of_experience as attributes
    
    # Describe role
    function describe_role():
        return description of the staff member's role
    
    # Gain experience
    function add_experience(years):
        increase years_of_experience by years
        return updated years_of_experience
    
    # String representation (override parent method)
    function __str__():
        return formatted string with name, role, and experience
```

### 3. Inheritance Level 2

These classes inherit from the Level 1 classes and provide more specialized implementations.

#### `Goalkeeper` Class (Inherits from Player)

**Tips:**
- Add goalkeeper-specific attributes and methods
- Override player methods as needed for goalkeeper stats
- Include specialized goalkeeper metrics

**Pseudocode:**
```
class Goalkeeper inherits from Player:
    # Constructor
    function __init__(first_name, last_name, age, nationality, jersey_number, dominant_foot="right"):
        call parent constructor with first_name, last_name, age, nationality, "Goalkeeper", jersey_number, dominant_foot
        initialize goalkeeper_stats (saves, clean_sheets, goals_conceded) to 0
    
    # Record a save
    function make_save():
        increment saves count
        return updated saves count
    
    # Record a clean sheet
    function record_clean_sheet():
        increment clean_sheets count
        return updated clean_sheets count
    
    # Concede a goal
    function concede_goal():
        increment goals_conceded count
        return updated goals_conceded count
    
    # Calculate save percentage
    function save_percentage():
        if (saves + goals_conceded) equals 0:
            return 0
        return (saves / (saves + goals_conceded)) * 100
```

#### `FieldPlayer` Class (Inherits from Player)

**Tips:**
- Add field player specific attributes and methods
- Consider metrics that apply to all field players (defenders, midfielders, forwards)
- Include movement and position-related functionalities

**Pseudocode:**
```
class FieldPlayer inherits from Player:
    # Constructor
    function __init__(first_name, last_name, age, nationality, position, jersey_number, dominant_foot="right"):
        if position equals "Goalkeeper":
            raise ValueError("FieldPlayer cannot have Goalkeeper position")
        call parent constructor with first_name, last_name, age, nationality, position, jersey_number, dominant_foot
        initialize field_stats (passes_completed, tackles, distance_covered) to 0
    
    # Record pass
    function complete_pass():
        increment passes_completed count
        return updated passes_completed count
    
    # Record tackle
    function make_tackle():
        increment tackles count
        return updated tackles count
    
    # Record distance covered
    function cover_distance(kilometers):
        add kilometers to distance_covered
        return updated distance_covered
    
    # Get position-specific performance metric
    function position_rating():
        if position equals "Defender":
            return defensive_rating calculation
        else if position equals "Midfielder":
            return midfield_rating calculation
        else if position equals "Forward":
            return offensive_rating calculation
```

#### `Coach` Class (Inherits from StaffMember)

**Tips:**
- Add coach-specific attributes and methods
- Include coaching style, formation preference, etc.
- Track coaching statistics and achievements

**Pseudocode:**
```
class Coach inherits from StaffMember:
    # Constructor
    function __init__(first_name, last_name, age, nationality, years_of_experience, coaching_style="Balanced"):
        call parent constructor with first_name, last_name, age, nationality, "Coach", years_of_experience
        store coaching_style as attribute
        initialize coaching_stats (matches, wins, draws, losses) to 0
        initialize preferred_formation to "4-4-2"
    
    # Record match result
    function record_match_result(result):
        increment matches
        if result equals "win":
            increment wins
        else if result equals "draw":
            increment draws
        else if result equals "loss":
            increment losses
        return current coaching_stats
    
    # Change preferred formation
    function set_formation(formation):
        update preferred_formation to formation
        return preferred_formation
    
    # Calculate win percentage
    function win_percentage():
        if matches equals 0:
            return 0
        return (wins / matches) * 100
```

### 4. Usage and Testing

Create instances of each class and demonstrate inheritance advantages like polymorphism (treating different types of objects through a common interface).

**Pseudocode:**
```
# Create a team roster with different types of players and staff
function create_team_roster():
    create an empty list called roster
    
    # Add a coach
    add Coach("Jürgen", "Klopp", 55, "German", 20, "Gegenpressing") to roster
    
    # Add a goalkeeper
    add Goalkeeper("Alisson", "Becker", 29, "Brazilian", 1) to roster
    
    # Add field players
    add FieldPlayer("Virgil", "van Dijk", 31, "Dutch", "Defender", 4) to roster
    add FieldPlayer("Kevin", "De Bruyne", 31, "Belgian", "Midfielder", 17) to roster
    add FieldPlayer("Harry", "Kane", 29, "English", "Forward", 9) to roster
    
    # Demonstrate polymorphism by calling common methods on different objects
    for each person in roster:
        print person's __str__() output
        if person is a Player:
            call play_match(90) on person
        if person is a Coach:
            call record_match_result("win") on person
    
    return roster
```

## Testing Your Implementation

Run the file to verify your implementation:

```python
python class_hierarchy.py
```

Ensure that each class properly inherits attributes and methods from its parent while implementing its own specialized functionality.

## Further Exploration

After completing the challenge, consider:

1. How would you add another level of specialization for forwards (e.g., striker, winger)?

2. Could you create a more general `Team` class that could hold any collection of `Person` objects (players, coaches, etc.)?

3. How might you implement interfaces or protocols to enforce certain capabilities across different branches of your hierarchy?

## Connect to Capstone

This class hierarchy directly relates to your NCAA soccer analysis system. As you design your object model, think about:

- What specializations exist in NCAA soccer that might need their own classes?
- How can inheritance help you avoid code duplication when tracking different types of players?
- What polymorphic operations would be useful when analyzing diverse player types with a common interface?

A well-designed class hierarchy will make your NCAA soccer analysis system more maintainable, extensible, and representative of the real-world domain it models!