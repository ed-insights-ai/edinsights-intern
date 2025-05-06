"""
Soccer Player Class
-----------------
Design and implement a SoccerPlayer class according to the specified requirements.
This exercise focuses on applying OOP concepts to model soccer player data.
"""

class SoccerPlayer:
    """
    A class representing a soccer player with various statistics and methods
    to calculate performance metrics.
    
    Attributes:
        player_id (str): Unique identifier for the player
        first_name (str): First name of the player
        last_name (str): Last name of the player
        position (str): Playing position (F, MF, D, GK)
        team (str): Team name
        games_played (int): Number of games played
        minutes (int): Total minutes played
        goals (int): Number of goals scored
        assists (int): Number of assists
        shots (int): Number of shots taken
        shots_on_goal (int): Number of shots on goal
        yellow_cards (int): Number of yellow cards received
        red_cards (int): Number of red cards received
        fouls_committed (int): Number of fouls committed
        fouls_suffered (int): Number of fouls suffered
    
    Methods:
        full_name(): Return the player's full name
        update_stats(): Update player statistics
        goals_per_90(): Calculate goals per 90 minutes
        assists_per_90(): Calculate assists per 90 minutes
        goal_contributions(): Calculate total goal contributions
        shot_accuracy(): Calculate shot accuracy percentage
        conversion_rate(): Calculate goal conversion rate
        card_ratio(): Calculate cards per game ratio
        fouls_ratio(): Calculate ratio of fouls committed to suffered
        efficiency_score(): Calculate an overall efficiency score
    """
    
    def __init__(self, player_id, first_name, last_name, position, team):
        """
        Initialize a new SoccerPlayer instance.
        
        Args:
            player_id (str): Unique identifier for the player
            first_name (str): First name of the player
            last_name (str): Last name of the player
            position (str): Playing position (F, MF, D, GK)
            team (str): Team name
        
        All statistics are initialized to 0.
        """
        # YOUR CODE HERE
        pass
    
    def full_name(self):
        """
        Get the player's full name (first and last name combined).
        
        Returns:
            str: The player's full name
        """
        # YOUR CODE HERE
        pass
    
    def update_stats(self, games=0, minutes=0, goals=0, assists=0, shots=0, 
                    shots_on_goal=0, yellow_cards=0, red_cards=0, 
                    fouls_committed=0, fouls_suffered=0):
        """
        Update player statistics.
        
        Args:
            games (int): Additional games played
            minutes (int): Additional minutes played
            goals (int): Additional goals scored
            assists (int): Additional assists
            shots (int): Additional shots taken
            shots_on_goal (int): Additional shots on goal
            yellow_cards (int): Additional yellow cards
            red_cards (int): Additional red cards
            fouls_committed (int): Additional fouls committed
            fouls_suffered (int): Additional fouls suffered
            
        Returns:
            dict: A dictionary containing all current statistics
        """
        # YOUR CODE HERE
        pass
    
    def goals_per_90(self):
        """
        Calculate goals per 90 minutes played.
        
        Returns:
            float: Goals per 90 minutes, or 0 if player hasn't played
        """
        # YOUR CODE HERE
        pass
    
    def assists_per_90(self):
        """
        Calculate assists per 90 minutes played.
        
        Returns:
            float: Assists per 90 minutes, or 0 if player hasn't played
        """
        # YOUR CODE HERE
        pass
    
    def goal_contributions(self):
        """
        Calculate total goal contributions (goals + assists).
        
        Returns:
            int: Total of goals and assists
        """
        # YOUR CODE HERE
        pass
    
    def shot_accuracy(self):
        """
        Calculate shot accuracy (shots on goal / total shots).
        
        Returns:
            float: Shot accuracy as a percentage (0-100), or 0 if no shots taken
        """
        # YOUR CODE HERE
        pass
    
    def conversion_rate(self):
        """
        Calculate goal conversion rate (goals / shots).
        
        Returns:
            float: Conversion rate as a percentage (0-100), or 0 if no shots taken
        """
        # YOUR CODE HERE
        pass
    
    def card_ratio(self):
        """
        Calculate cards per game ratio.
        
        Returns:
            float: Average number of cards per game, or 0 if no games played
        """
        # YOUR CODE HERE
        pass
    
    def fouls_ratio(self):
        """
        Calculate ratio of fouls committed to fouls suffered.
        
        Returns:
            float: Ratio (committed/suffered), or 0 if no fouls suffered
        """
        # YOUR CODE HERE
        pass
    
    def efficiency_score(self):
        """
        Calculate an overall efficiency score based on multiple metrics.
        This is a composite score that weighs different aspects of a player's performance.
        The formula should be position-specific:
        
        For Forwards (F): Goals, conversion rate, and shot accuracy are weighted heavily
        For Midfielders (MF): Assists, goals, and fouls ratio are weighted heavily
        For Defenders (D): Fouls ratio, card ratio are weighted heavily
        For Goalkeepers (GK): Only minutes and games played are considered
        
        Returns:
            float: An efficiency score from 0-100
        """
        # YOUR CODE HERE
        pass
    
    def __str__(self):
        """
        Return a string representation of the player.
        
        Returns:
            str: A formatted string with the player's information
        """
        # YOUR CODE HERE
        pass


class Team:
    """
    A class representing a soccer team, composed of multiple SoccerPlayer objects.
    
    Attributes:
        name (str): Team name
        players (list): List of SoccerPlayer objects
        
    Methods:
        add_player(player): Add a player to the team
        remove_player(player_id): Remove a player from the team
        get_player(player_id): Get a player by ID
        team_stats(): Calculate team-level statistics
        best_scorer(): Find the player with the most goals
        best_assistant(): Find the player with the most assists
        most_efficient_player(): Find the player with the highest efficiency score
    """
    
    def __init__(self, name):
        """
        Initialize a new Team instance.
        
        Args:
            name (str): Team name
        """
        # YOUR CODE HERE
        pass
    
    def add_player(self, player):
        """
        Add a player to the team.
        
        Args:
            player (SoccerPlayer): The player to add
            
        Returns:
            int: The number of players on the team
            
        Raises:
            ValueError: If a player with the same ID already exists
        """
        # YOUR CODE HERE
        pass
    
    def remove_player(self, player_id):
        """
        Remove a player from the team.
        
        Args:
            player_id (str): The ID of the player to remove
            
        Returns:
            SoccerPlayer: The removed player
            
        Raises:
            ValueError: If the player is not found
        """
        # YOUR CODE HERE
        pass
    
    def get_player(self, player_id):
        """
        Get a player by ID.
        
        Args:
            player_id (str): The ID of the player to get
            
        Returns:
            SoccerPlayer: The player with the specified ID, or None if not found
        """
        # YOUR CODE HERE
        pass
    
    def team_stats(self):
        """
        Calculate team-level statistics.
        
        Returns:
            dict: A dictionary containing team statistics like total goals,
                 total assists, average efficiency, etc.
        """
        # YOUR CODE HERE
        pass
    
    def best_scorer(self):
        """
        Find the player with the most goals.
        
        Returns:
            SoccerPlayer: The player with the most goals, or None if no players
        """
        # YOUR CODE HERE
        pass
    
    def best_assistant(self):
        """
        Find the player with the most assists.
        
        Returns:
            SoccerPlayer: The player with the most assists, or None if no players
        """
        # YOUR CODE HERE
        pass
    
    def most_efficient_player(self):
        """
        Find the player with the highest efficiency score.
        
        Returns:
            SoccerPlayer: The player with the highest efficiency score, or None if no players
        """
        # YOUR CODE HERE
        pass


def main():
    """Test the SoccerPlayer and Team classes with some examples."""
    # Create some players
    player1 = SoccerPlayer("DII001", "John", "Smith", "F", "Western State")
    player1.update_stats(games=20, minutes=1750, goals=12, assists=8, shots=45, 
                        shots_on_goal=30, yellow_cards=2, fouls_committed=15, fouls_suffered=25)
    
    player2 = SoccerPlayer("DII002", "Maria", "Garcia", "MF", "Eastern College")
    player2.update_stats(games=18, minutes=1620, goals=5, assists=10, shots=25, 
                        shots_on_goal=15, yellow_cards=3, fouls_committed=18, fouls_suffered=20)
    
    player3 = SoccerPlayer("DII003", "David", "Johnson", "D", "Northern University")
    player3.update_stats(games=19, minutes=1710, goals=1, assists=3, shots=10, 
                        shots_on_goal=5, yellow_cards=4, red_cards=1, fouls_committed=22, fouls_suffered=8)
    
    # Print player statistics
    print("Player 1:")
    print(player1)
    print(f"Goals per 90 minutes: {player1.goals_per_90():.2f}")
    print(f"Shot accuracy: {player1.shot_accuracy():.2f}%")
    print(f"Efficiency score: {player1.efficiency_score():.2f}")
    
    print("\nPlayer 2:")
    print(player2)
    print(f"Goals per 90 minutes: {player2.goals_per_90():.2f}")
    print(f"Assists per 90 minutes: {player2.assists_per_90():.2f}")
    print(f"Efficiency score: {player2.efficiency_score():.2f}")
    
    print("\nPlayer 3:")
    print(player3)
    print(f"Card ratio: {player3.card_ratio():.2f}")
    print(f"Fouls ratio: {player3.fouls_ratio():.2f}")
    print(f"Efficiency score: {player3.efficiency_score():.2f}")
    
    # Create a team and add players
    team = Team("All-Stars FC")
    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)
    
    # Test team methods
    print("\nTeam Statistics:")
    team_stats = team.team_stats()
    for stat, value in team_stats.items():
        print(f"{stat}: {value}")
    
    print("\nBest Scorer:", team.best_scorer().full_name())
    print("Best Assistant:", team.best_assistant().full_name())
    print("Most Efficient Player:", team.most_efficient_player().full_name())

if __name__ == "__main__":
    main()