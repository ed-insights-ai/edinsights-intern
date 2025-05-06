"""
Database Schema Design
------------------
Design a database schema for a soccer statistics system.
This exercise focuses on creating a well-structured database with appropriate tables and relationships.
"""

import sqlite3
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("database_schema.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Database file path
DB_FILE = 'soccer_stats.db'

def create_database():
    """
    Create the soccer statistics database with all tables.
    
    Returns:
        bool: True if database was created successfully
    """
    try:
        # Connect to the database (this will create the file if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create tables - modify as needed for your schema design
        
        # 1. Teams Table
        # YOUR CODE HERE - Create the teams table
        # The table should include:
        # - id (primary key)
        # - name
        # - location
        # - conference
        # - Additional fields as needed
        
        # 2. Players Table
        # YOUR CODE HERE - Create the players table
        # The table should include:
        # - id (primary key)
        # - first_name
        # - last_name
        # - team_id (foreign key to teams)
        # - position
        # - jersey_number
        # - height
        # - weight
        # - year (freshman, sophomore, etc.)
        # - Additional fields as needed
        
        # 3. Matches Table
        # YOUR CODE HERE - Create the matches table
        # The table should include:
        # - id (primary key)
        # - home_team_id (foreign key to teams)
        # - away_team_id (foreign key to teams)
        # - date
        # - location
        # - home_score
        # - away_score
        # - Additional fields as needed
        
        # 4. Player Statistics Table
        # YOUR CODE HERE - Create the player_stats table
        # The table should include:
        # - id (primary key)
        # - player_id (foreign key to players)
        # - match_id (foreign key to matches)
        # - minutes_played
        # - goals
        # - assists
        # - shots
        # - shots_on_goal
        # - Additional fields as needed
        
        # 5. Team Statistics Table
        # YOUR CODE HERE - Create the team_stats table
        # The table should include:
        # - id (primary key)
        # - team_id (foreign key to teams)
        # - match_id (foreign key to matches)
        # - shots
        # - shots_on_goal
        # - corners
        # - fouls
        # - Additional fields as needed
        
        # 6. Seasons Table
        # YOUR CODE HERE - Create the seasons table
        # The table should include:
        # - id (primary key)
        # - year
        # - name (e.g., "Fall 2023")
        # - start_date
        # - end_date
        # - Additional fields as needed
        
        # 7. Create any other tables you think are necessary
        # YOUR CODE HERE
        
        # Create indexes for performance
        # YOUR CODE HERE - Create appropriate indexes
        # Consider which columns will be frequently queried
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        logger.info(f"Database created successfully at {DB_FILE}")
        return True
    
    except Exception as e:
        logger.error(f"Error creating database: {e}")
        return False

def insert_sample_data():
    """
    Insert sample data into the database.
    
    Returns:
        bool: True if data was inserted successfully
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Insert sample teams
        # YOUR CODE HERE
        
        # Insert sample players
        # YOUR CODE HERE
        
        # Insert sample matches
        # YOUR CODE HERE
        
        # Insert sample player statistics
        # YOUR CODE HERE
        
        # Insert sample team statistics
        # YOUR CODE HERE
        
        # Insert sample seasons
        # YOUR CODE HERE
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        logger.info("Sample data inserted successfully")
        return True
    
    except Exception as e:
        logger.error(f"Error inserting sample data: {e}")
        return False

def run_sample_queries():
    """
    Run sample queries to demonstrate the database schema.
    
    Returns:
        dict: Results of the sample queries
    """
    results = {}
    
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        
        # Sample Query 1: Get all players with their team names
        # YOUR CODE HERE
        
        # Sample Query 2: Get top goal scorers
        # YOUR CODE HERE
        
        # Sample Query 3: Get match results for a specific team
        # YOUR CODE HERE
        
        # Sample Query 4: Get player statistics for a specific match
        # YOUR CODE HERE
        
        # Sample Query 5: Get team standings in a conference
        # YOUR CODE HERE
        
        # Close connection
        conn.close()
        
        logger.info("Sample queries executed successfully")
        return results
    
    except Exception as e:
        logger.error(f"Error running sample queries: {e}")
        return {"error": str(e)}

def main():
    """Create the database schema and run sample operations."""
    print("Soccer Statistics Database Schema")
    
    # Check if database already exists
    db_exists = os.path.exists(DB_FILE)
    
    if db_exists:
        print(f"Database already exists at {DB_FILE}")
        choice = input("Do you want to recreate the database? This will delete all existing data. (y/n): ")
        if choice.lower() == 'y':
            os.remove(DB_FILE)
            print("Existing database deleted.")
            db_exists = False
        else:
            print("Using existing database.")
    
    if not db_exists:
        print("Creating new database...")
        success = create_database()
        if success:
            print("Database created successfully!")
            
            print("Inserting sample data...")
            success = insert_sample_data()
            if success:
                print("Sample data inserted successfully!")
            else:
                print("Failed to insert sample data.")
        else:
            print("Failed to create database.")
    
    print("\nRunning sample queries...")
    results = run_sample_queries()
    
    if "error" in results:
        print(f"Error running queries: {results['error']}")
    else:
        print("Sample query results:")
        for query_name, query_results in results.items():
            print(f"\n{query_name}:")
            for row in query_results:
                print(row)

if __name__ == "__main__":
    main()