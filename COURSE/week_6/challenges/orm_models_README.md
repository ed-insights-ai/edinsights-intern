# Challenge 2: SQLAlchemy ORM Models for Soccer Analytics

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll implement SQLAlchemy ORM (Object-Relational Mapping) models for your soccer analytics database. These models will provide a Pythonic interface to your database, allowing you to perform CRUD (Create, Read, Update, Delete) operations and complex queries on your soccer data without writing raw SQL.

## Learning Objectives

- Understand the Object-Relational Mapping (ORM) pattern
- Implement Python classes that map to database tables
- Create relationships between ORM models
- Develop CRUD operations using SQLAlchemy
- Write methods for common soccer analytics queries
- Implement data validation logic

## Real-World Context

Sports analytics platforms use ORM layers to interact with their databases in a more intuitive, object-oriented way. This approach allows developers to work with database records as Python objects, making the code more readable and maintainable. NCAA soccer programs rely on these systems to track player development, analyze opponent strategies, and make data-driven decisions about training and game tactics.

## Challenge Details

### The Task

Implement SQLAlchemy ORM models that:

1. Map to the database tables you designed in Challenge 1
2. Include appropriate relationships between models
3. Provide CRUD operations for each model
4. Implement methods for common soccer analytics queries
5. Include data validation where appropriate

### ORM Model Structure Diagram

```
+-------------------------+
|        Base Class       |
+-------------------------+
         /|\
          |
 +--------+--------+--------+--------+
 |        |        |        |        |
 v        v        v        v        v
+------+ +------+ +------+ +------+ +------+
|Player| | Team | |Match | |PlayerStat| |TeamSeason|
+------+ +------+ +------+ +------+ +------+
|Fields| |Fields| |Fields| |Fields| |Fields|
+------+ +------+ +------+ +------+ +------+
|Methods| |Methods| |Methods| |Methods| |Methods|
+------+ +------+ +------+ +------+ +------+
```

## Tips and Hints

### Basic ORM Model Structure

```python
class Player(Base):
    __tablename__ = 'players'
    
    # Fields
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    # More fields...
    
    # Relationships
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="players")
    statistics = relationship("PlayerMatchStatistic", back_populates="player")
    
    # Model methods
    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name}>"
        
    # CRUD class methods
    @classmethod
    def create(cls, session, **kwargs):
        # Logic to create a new player
        
    @classmethod
    def get_by_id(cls, session, player_id):
        # Logic to get a player by ID
        
    # Other methods...
```

### CRUD Operations

Here's how you might implement CRUD operations for the Player model:

**Create Operation:**
```python
@classmethod
def create(cls, session, **kwargs):
    """Create a new player in the database."""
    player = cls(**kwargs)
    session.add(player)
    session.commit()
    return player
```

**Read Operations:**
```python
@classmethod
def get_by_id(cls, session, player_id):
    """Get a player by ID."""
    return session.query(cls).filter_by(id=player_id).first()
    
@classmethod
def get_all(cls, session):
    """Get all players."""
    return session.query(cls).all()
    
@classmethod
def search(cls, session, **kwargs):
    """Search for players by various criteria."""
    query = session.query(cls)
    for key, value in kwargs.items():
        if hasattr(cls, key):
            query = query.filter(getattr(cls, key) == value)
    return query.all()
```

**Update Operation:**
```python
def update(self, session, **kwargs):
    """Update player attributes."""
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)
    session.commit()
    return self
```

**Delete Operation:**
```python
def delete(self, session):
    """Delete the player from the database."""
    session.delete(self)
    session.commit()
```

### Analytics Methods

You can add methods to perform common soccer analytics operations:

```python
def get_season_stats(self, session, season):
    """Get a player's statistics for a specific season."""
    # Logic to aggregate statistics across all matches in a season
    from sqlalchemy import func
    
    stats = session.query(
        func.sum(PlayerMatchStatistic.goals).label("total_goals"),
        func.sum(PlayerMatchStatistic.assists).label("total_assists"),
        func.sum(PlayerMatchStatistic.shots).label("total_shots"),
        func.sum(PlayerMatchStatistic.minutes_played).label("total_minutes")
    ).join(Match).filter(
        PlayerMatchStatistic.player_id == self.id,
        Match.season == season
    ).first()
    
    return {
        "player_id": self.id,
        "player_name": f"{self.first_name} {self.last_name}",
        "season": season,
        "total_goals": stats.total_goals or 0,
        "total_assists": stats.total_assists or 0,
        "total_shots": stats.total_shots or 0,
        "total_minutes": stats.total_minutes or 0,
        "shots_per_goal": stats.total_shots / stats.total_goals if stats.total_goals else float('inf'),
        "minutes_per_goal": stats.total_minutes / stats.total_goals if stats.total_goals else float('inf')
    }
```

### Data Validation

You can add validation logic to ensure data integrity:

```python
@validates('jersey_number')
def validate_jersey_number(self, key, number):
    """Validate that jersey numbers are in a valid range."""
    if number is not None and (number < 1 or number > 99):
        raise ValueError("Jersey number must be between 1 and 99")
    return number
    
@validates('position')
def validate_position(self, key, position):
    """Validate that the position is valid."""
    valid_positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
    if position not in valid_positions:
        raise ValueError(f"Position must be one of: {', '.join(valid_positions)}")
    return position
```

## Testing Your Solution

Your solution should:

1. Successfully create ORM models for all tables in your schema
2. Establish proper relationships between models
3. Implement CRUD operations for each model
4. Include methods for common soccer analytics queries
5. Add appropriate validation logic

Test your models by:

1. Creating an in-memory SQLite database
2. Creating instances of your models
3. Performing CRUD operations on those instances
4. Running your analytics methods
5. Verifying that validation logic works as expected

## Application to Capstone

The ORM models you create in this challenge will be used throughout your capstone project to:

1. Interface with your database from your Python code
2. Store and retrieve data collected by your web scraper
3. Process and analyze soccer statistics
4. Generate insights for your web application
5. Validate data to ensure integrity

These models will serve as a critical layer between your database and your application logic, making it easier to work with soccer data in a Pythonic way.

## Resources

- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [SQLAlchemy Query API](https://docs.sqlalchemy.org/en/14/orm/query.html)
- [SQLAlchemy Relationship Patterns](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)
- [Data Validation in SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators)
- [SQLAlchemy Session Basics](https://docs.sqlalchemy.org/en/14/orm/session_basics.html)
- [Advanced SQLAlchemy Queries](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query)
- [SQLAlchemy Core vs ORM](https://docs.sqlalchemy.org/en/14/orm/queryguide.html)