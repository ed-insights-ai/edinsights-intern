"""
CHALLENGE: Soccer Analytics Database Schema Design

Your task is to design a database schema for a NCAA soccer analytics system.
This schema will be the foundation for storing and analyzing soccer player and team statistics.

The schema should include:
1. Tables for players, teams, matches, and statistical data
2. Appropriate relationships between tables (one-to-many, many-to-many)
3. Primary keys, foreign keys, and constraints
4. Indexes for optimization

REQUIREMENTS:
- Use SQLAlchemy's declarative syntax to define tables
- Create appropriate relationships between tables
- Include relevant fields for soccer analytics
- Add appropriate data types and constraints
- Include documentation for tables and relationships
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

# Create a base class for declarative class definitions
Base = declarative_base()

# TODO: Create your database schema here

# Example structure (replace this with your implementation):
"""
class Player(Base):
    __tablename__ = 'players'
    
    # Fields...
    # Relationships...
    
class Team(Base):
    __tablename__ = 'teams'
    
    # Fields...
    # Relationships...
    
class Match(Base):
    __tablename__ = 'matches'
    
    # Fields...
    # Relationships...
    
class PlayerStatistic(Base):
    __tablename__ = 'player_statistics'
    
    # Fields...
    # Relationships...
    
class TeamStatistic(Base):
    __tablename__ = 'team_statistics'
    
    # Fields...
    # Relationships...
"""

# TODO: Define your tables for the soccer analytics database

class Player(Base):
    """
    Represents a soccer player in the database.
    
    This table should store information about individual players, including:
    - Basic biographical information
    - Team affiliations
    - Player attributes
    
    TODO: Implement this table with appropriate fields and relationships
    """
    pass


class Team(Base):
    """
    Represents a soccer team in the database.
    
    This table should store information about soccer teams, including:
    - Team name and information
    - Division and conference
    - Season information
    
    TODO: Implement this table with appropriate fields and relationships
    """
    pass


class Match(Base):
    """
    Represents a soccer match between two teams.
    
    This table should store information about individual matches, including:
    - Teams involved
    - Match date and location
    - Score and result
    
    TODO: Implement this table with appropriate fields and relationships
    """
    pass


class PlayerMatchStatistic(Base):
    """
    Represents statistics for a player in a specific match.
    
    This table should store detailed statistics for a player's performance in a match:
    - Goals, assists, shots
    - Playing time
    - Other relevant metrics
    
    TODO: Implement this table with appropriate fields and relationships
    """
    pass


class TeamSeason(Base):
    """
    Represents a team's performance over a season.
    
    This table should store aggregated statistics for a team's season:
    - Win/loss record
    - Goals for/against
    - Season ranking
    
    TODO: Implement this table with appropriate fields and relationships
    """
    pass


def create_tables(engine):
    """
    Creates all tables in the database.
    
    Args:
        engine: SQLAlchemy engine instance
    """
    Base.metadata.create_all(engine)


def main():
    """
    Main function to create the database and tables.
    """
    # Create an SQLite database in memory (for testing)
    engine = create_engine('sqlite:///:memory:', echo=True)
    
    # Create the tables
    create_tables(engine)
    
    print("Database schema created successfully!")


if __name__ == "__main__":
    main()