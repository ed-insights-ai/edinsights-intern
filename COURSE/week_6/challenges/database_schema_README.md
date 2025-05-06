# Challenge 1: Soccer Analytics Database Schema Design

**Difficulty: ⭐⭐⭐☆☆**

## Challenge Overview

In this challenge, you'll design a database schema for storing NCAA soccer analytics data. This schema will serve as the foundation for your capstone project's data storage, enabling efficient queries and analysis of player and team performance.

## Learning Objectives

- Design relational database tables with appropriate fields and relationships
- Implement primary keys, foreign keys, and constraints
- Create efficient schemas for storing sports statistics
- Use SQLAlchemy's declarative syntax for database definition
- Understand one-to-many and many-to-many relationships

## Real-World Context

Sports analytics systems rely on well-designed databases to store player statistics, match results, and performance metrics. NCAA soccer programs use these databases to track player development, analyze opponents, and inform strategic decisions. A properly designed schema allows coaches and analysts to quickly retrieve the information they need, from individual player performance to team trends over time.

## Challenge Details

### The Task

Design a SQLAlchemy database schema that includes:

1. Tables for players, teams, matches, and statistics
2. Appropriate relationships between tables (one-to-many, many-to-many)
3. Primary keys, foreign keys, and constraints
4. Indexes for optimizing common queries
5. Documentation for each table and relationship

### Database Entity Relationship Diagram

```
  +-------------+       +---------------+       +--------------+
  |    Team     |       | TeamSeason    |       |    Match     |
  +-------------+       +---------------+       +--------------+
  | id          |<----->| id            |       | id           |
  | name        |       | team_id       |       | home_team_id |
  | mascot      |       | season_year   |       | away_team_id |
  | division    |       | wins          |       | date         |
  | conference  |       | losses        |       | home_score   |
  | city        |       | ties          |       | away_score   |
  | state       |       | goals_for     |       | venue        |
  +-------------+       | goals_against |       +--------------+
         ^              | ranking       |              ^
         |              +---------------+              |
         |                                             |
  +------|------------------------------------------- |-------+
  |      |                                             |       |
  |      v                                             v       |
  | +-------------+                           +------------------+
  | |   Player    |                           |PlayerMatchStatistic|
  | +-------------+                           +------------------+
  | | id          |<----------------------->  | id               |
  | | first_name  |                           | player_id        |
  | | last_name   |                           | match_id         |
  | | team_id     |                           | minutes_played   |
  | | jersey_num  |                           | goals            |
  | | position    |                           | assists          |
  | | height      |                           | shots            |
  | | weight      |                           | shots_on_goal    |
  | | year        |                           | yellow_cards     |
  | | hometown    |                           | red_cards        |
  | +-------------+                           +------------------+
```

## Tips and Hints

### Table Structure and Relationships

**Players Table:**
- Player biographical info (name, hometown, etc.)
- Physical attributes (height, weight, etc.)
- Team affiliation (foreign key to Teams)
- Academic information (year, major, etc.)

**Teams Table:**
- Team identification (name, mascot, etc.)
- Division and conference information
- Location information
- Team contact info

**Matches Table:**
- Match date and location
- Home and away teams (foreign keys to Teams)
- Scores
- Match conditions (weather, field type, etc.)

**Player Match Statistics Table:**
- Foreign keys to Players and Matches tables
- Performance metrics (goals, assists, shots, etc.)
- Playing time information
- Cards and penalties

**Team Season Table:**
- Foreign key to Teams table
- Season identifier (year)
- Season statistics (wins, losses, ties, etc.)

### SQLAlchemy Implementation Example

Here's how you might define a Player table with SQLAlchemy:

```python
class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    jersey_number = Column(Integer)
    position = Column(String(30))
    birth_date = Column(Date)
    height_cm = Column(Integer)
    weight_kg = Column(Float)
    hometown = Column(String(100))
    
    # Foreign key relationship
    team_id = Column(Integer, ForeignKey('teams.id'))
    
    # Relationship definition
    team = relationship("Team", back_populates="players")
    statistics = relationship("PlayerMatchStatistic", back_populates="player")
    
    # Indexing for common queries
    __table_args__ = (
        Index('idx_player_name', 'last_name', 'first_name'),
        Index('idx_player_position', 'position'),
    )
```

### Common Relationship Patterns

**One-to-Many Relationships:**
```python
# In the "One" model (e.g., Team)
players = relationship("Player", back_populates="team")

# In the "Many" model (e.g., Player)
team_id = Column(Integer, ForeignKey('teams.id'))
team = relationship("Team", back_populates="players")
```

**Many-to-Many Relationships:**
```python
# Association table
player_match = Table('player_match', Base.metadata,
    Column('player_id', Integer, ForeignKey('players.id'), primary_key=True),
    Column('match_id', Integer, ForeignKey('matches.id'), primary_key=True)
)

# In the Player model
matches = relationship("Match", secondary=player_match, back_populates="players")

# In the Match model
players = relationship("Player", secondary=player_match, back_populates="matches")
```

## Testing Your Solution

Your solution should:
1. Create all necessary tables with appropriate fields and data types
2. Establish proper relationships between tables
3. Include primary keys, foreign keys, and constraints
4. Add indexes for optimizing common queries
5. Successfully create tables when the script is run
6. Include comprehensive documentation

Test your schema by:
1. Running the script to create an in-memory SQLite database
2. Verifying that all tables are created correctly
3. Checking that relationships are established properly
4. Ensuring constraints and indexes are applied

## Application to Capstone

The database schema you design in this challenge will be foundational to your capstone project. It will:

1. Store all NCAA soccer data collected by your scraper
2. Enable efficient queries for your analytics algorithms
3. Support the web interface for data visualization
4. Allow tracking of player and team performance over time
5. Facilitate complex analytics and comparisons

A well-designed schema will scale as your dataset grows and support increasingly complex analytics as your capstone project evolves.

## Resources

- [SQLAlchemy ORM Documentation](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [Database Normalization Guide](https://www.guru99.com/database-normalization.html)
- [SQL Indexing Best Practices](https://use-the-index-luke.com/)
- [Entity-Relationship Diagrams Tutorial](https://www.lucidchart.com/pages/er-diagrams)
- [Sports Database Schema Examples](https://www.vertabelo.com/blog/a-sports-data-model/)
- [Foreign Keys and Relationships in SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)