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
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        
        # Initialize all statistics to 0
        self.games_played = 0
        self.minutes = 0
        self.goals = 0
        self.assists = 0
        self.shots = 0
        self.shots_on_goal = 0
        self.yellow_cards = 0
        self.red_cards = 0
        self.fouls_committed = 0
        self.fouls_suffered = 0
    
    def full_name(self):
        """
        Get the player's full name (first and last name combined).
        
        Returns:
            str: The player's full name
        """
        return f"{self.first_name} {self.last_name}"
    
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
        self.games_played += games
        self.minutes += minutes
        self.goals += goals
        self.assists += assists
        self.shots += shots
        self.shots_on_goal += shots_on_goal
        self.yellow_cards += yellow_cards
        self.red_cards += red_cards
        self.fouls_committed += fouls_committed
        self.fouls_suffered += fouls_suffered
        
        return {
            'games_played': self.games_played,
            'minutes': self.minutes,
            'goals': self.goals,
            'assists': self.assists,
            'shots': self.shots,
            'shots_on_goal': self.shots_on_goal,
            'yellow_cards': self.yellow_cards,
            'red_cards': self.red_cards,
            'fouls_committed': self.fouls_committed,
            'fouls_suffered': self.fouls_suffered
        }
    
    def goals_per_90(self):
        """
        Calculate goals per 90 minutes played.
        
        Returns:
            float: Goals per 90 minutes, or 0 if player hasn't played
        """
        if self.minutes == 0:
            return 0
        return (self.goals / self.minutes) * 90
    
    def assists_per_90(self):
        """
        Calculate assists per 90 minutes played.
        
        Returns:
            float: Assists per 90 minutes, or 0 if player hasn't played
        """
        if self.minutes == 0:
            return 0
        return (self.assists / self.minutes) * 90
    
    def goal_contributions(self):
        """
        Calculate total goal contributions (goals + assists).
        
        Returns:
            int: Total of goals and assists
        """
        return self.goals + self.assists
    
    def shot_accuracy(self):
        """
        Calculate shot accuracy (shots on goal / total shots).
        
        Returns:
            float: Shot accuracy as a percentage (0-100), or 0 if no shots taken
        """
        if self.shots == 0:
            return 0
        return (self.shots_on_goal / self.shots) * 100
    
    def conversion_rate(self):
        """
        Calculate goal conversion rate (goals / shots).
        
        Returns:
            float: Conversion rate as a percentage (0-100), or 0 if no shots taken
        """
        if self.shots == 0:
            return 0
        return (self.goals / self.shots) * 100
    
    def card_ratio(self):
        """
        Calculate cards per game ratio.
        
        Returns:
            float: Average number of cards per game, or 0 if no games played
        """
        if self.games_played == 0:
            return 0
        total_cards = self.yellow_cards + self.red_cards
        return total_cards / self.games_played
    
    def fouls_ratio(self):
        """
        Calculate ratio of fouls committed to fouls suffered.
        
        Returns:
            float: Ratio (committed/suffered), or 0 if no fouls suffered
        """
        if self.fouls_suffered == 0:
            return 0
        return self.fouls_committed / self.fouls_suffered
    
    def efficiency_score(self):
        """
        Calculate an overall efficiency score based on multiple metrics.
        This is a composite score that weighs different aspects of a player's performance.
        The formula is position-specific.
        
        Returns:
            float: An efficiency score from 0-100
        """
        if self.games_played == 0:
            return 0
        
        if self.position == "F":  # Forward
            # Forwards: Goals (40%), Conversion Rate (30%), Shot Accuracy (20%), Assists (10%)
            goals_score = min((self.goals_per_90() / 0.5) * 40, 40)  # 0.5 goals/90 = max score
            conversion_score = min(self.conversion_rate() * 0.3, 30)
            accuracy_score = min(self.shot_accuracy() * 0.2, 20)
            assist_score = min((self.assists_per_90() / 0.3) * 10, 10)  # 0.3 assists/90 = max score
            return goals_score + conversion_score + accuracy_score + assist_score
            
        elif self.position == "MF":  # Midfielder
            # Midfielders: Assists (30%), Goals (25%), Goal Contributions (25%), Fouls Ratio (20%)
            assists_score = min((self.assists_per_90() / 0.4) * 30, 30)  # 0.4 assists/90 = max score
            goals_score = min((self.goals_per_90() / 0.3) * 25, 25)  # 0.3 goals/90 = max score
            contributions_score = min((self.goal_contributions() / 15) * 25, 25)  # 15 contributions = max
            fouls_score = max(0, 20 - (self.fouls_ratio() * 10))  # Lower ratio is better
            return assists_score + goals_score + contributions_score + fouls_score
            
        elif self.position == "D":  # Defender
            # Defenders: Fouls Ratio (40%), Card Ratio (30%), Minutes (20%), Assists (10%)
            fouls_score = max(0, 40 - (self.fouls_ratio() * 20))  # Lower ratio is better
            cards_score = max(0, 30 - (self.card_ratio() * 30))  # Lower ratio is better
            minutes_score = min((self.minutes / self.games_played / 90) * 20, 20) if self.games_played > 0 else 0
            assist_score = min((self.assists_per_90() / 0.2) * 10, 10)  # 0.2 assists/90 = max score
            return fouls_score + cards_score + minutes_score + assist_score
            
        elif self.position == "GK":  # Goalkeeper
            # Goalkeepers: Just based on playing time percentage
            if self.games_played > 0:
                return min((self.minutes / (self.games_played * 90)) * 100, 100)
            return 0
        
        return 0
    
    def __str__(self):
        """
        Return a string representation of the player.
        
        Returns:
            str: A formatted string with the player's information
        """
        return (f"{self.full_name()} ({self.position}) - {self.team}\n"
                f"Games: {self.games_played}, Minutes: {self.minutes}\n"
                f"Goals: {self.goals}, Assists: {self.assists}\n"
                f"Shots: {self.shots} (On Target: {self.shots_on_goal})\n"
                f"Cards: {self.yellow_cards}Y {self.red_cards}R")


class Team:
    """
    A class representing a soccer team, composed of multiple SoccerPlayer objects.
    """
    
    def __init__(self, name):
        """
        Initialize a new Team instance.
        
        Args:
            name (str): Team name
        """
        self.name = name
        self.players = []
    
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
        # Check if player with same ID already exists
        for existing_player in self.players:
            if existing_player.player_id == player.player_id:
                raise ValueError(f"Player with ID {player.player_id} already exists on the team")
        
        self.players.append(player)
        return len(self.players)
    
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
        for i, player in enumerate(self.players):
            if player.player_id == player_id:
                return self.players.pop(i)
        
        raise ValueError(f"Player with ID {player_id} not found on the team")
    
    def get_player(self, player_id):
        """
        Get a player by ID.
        
        Args:
            player_id (str): The ID of the player to get
            
        Returns:
            SoccerPlayer: The player with the specified ID, or None if not found
        """
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None
    
    def team_stats(self):
        """
        Calculate team-level statistics.
        
        Returns:
            dict: A dictionary containing team statistics
        """
        if not self.players:
            return {
                'total_players': 0,
                'total_goals': 0,
                'total_assists': 0,
                'total_shots': 0,
                'total_games': 0,
                'average_efficiency': 0
            }
        
        total_goals = sum(player.goals for player in self.players)
        total_assists = sum(player.assists for player in self.players)
        total_shots = sum(player.shots for player in self.players)
        total_games = sum(player.games_played for player in self.players)
        total_minutes = sum(player.minutes for player in self.players)
        total_yellow = sum(player.yellow_cards for player in self.players)
        total_red = sum(player.red_cards for player in self.players)
        
        efficiency_scores = [player.efficiency_score() for player in self.players]
        average_efficiency = sum(efficiency_scores) / len(efficiency_scores)
        
        return {
            'total_players': len(self.players),
            'total_goals': total_goals,
            'total_assists': total_assists,
            'total_shots': total_shots,
            'total_games': total_games,
            'total_minutes': total_minutes,
            'total_yellow_cards': total_yellow,
            'total_red_cards': total_red,
            'average_efficiency': round(average_efficiency, 2),
            'goals_per_game': round(total_goals / total_games, 2) if total_games > 0 else 0,
            'assists_per_game': round(total_assists / total_games, 2) if total_games > 0 else 0
        }
    
    def best_scorer(self):
        """
        Find the player with the most goals.
        
        Returns:
            SoccerPlayer: The player with the most goals, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.goals)
    
    def best_assistant(self):
        """
        Find the player with the most assists.
        
        Returns:
            SoccerPlayer: The player with the most assists, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.assists)
    
    def most_efficient_player(self):
        """
        Find the player with the highest efficiency score.
        
        Returns:
            SoccerPlayer: The player with the highest efficiency score, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.efficiency_score())


import json
import csv
from datetime import datetime


class Team:
    """
    A class representing a soccer team, composed of multiple SoccerPlayer objects.
    """
    
    def __init__(self, name):
        """
        Initialize a new Team instance.
        
        Args:
            name (str): Team name
        """
        self.name = name
        self.players = []
    
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
        # Check if player with same ID already exists
        for existing_player in self.players:
            if existing_player.player_id == player.player_id:
                raise ValueError(f"Player with ID {player.player_id} already exists on the team")
        
        self.players.append(player)
        return len(self.players)
    
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
        for i, player in enumerate(self.players):
            if player.player_id == player_id:
                return self.players.pop(i)
        
        raise ValueError(f"Player with ID {player_id} not found on the team")
    
    def get_player(self, player_id):
        """
        Get a player by ID.
        
        Args:
            player_id (str): The ID of the player to get
            
        Returns:
            SoccerPlayer: The player with the specified ID, or None if not found
        """
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None
    
    def team_stats(self):
        """
        Calculate team-level statistics.
        
        Returns:
            dict: A dictionary containing team statistics
        """
        if not self.players:
            return {
                'total_players': 0,
                'total_goals': 0,
                'total_assists': 0,
                'total_shots': 0,
                'total_games': 0,
                'average_efficiency': 0
            }
        
        total_goals = sum(player.goals for player in self.players)
        total_assists = sum(player.assists for player in self.players)
        total_shots = sum(player.shots for player in self.players)
        total_games = sum(player.games_played for player in self.players)
        total_minutes = sum(player.minutes for player in self.players)
        total_yellow = sum(player.yellow_cards for player in self.players)
        total_red = sum(player.red_cards for player in self.players)
        
        efficiency_scores = [player.efficiency_score() for player in self.players]
        average_efficiency = sum(efficiency_scores) / len(efficiency_scores)
        
        return {
            'total_players': len(self.players),
            'total_goals': total_goals,
            'total_assists': total_assists,
            'total_shots': total_shots,
            'total_games': total_games,
            'total_minutes': total_minutes,
            'total_yellow_cards': total_yellow,
            'total_red_cards': total_red,
            'average_efficiency': round(average_efficiency, 2),
            'goals_per_game': round(total_goals / total_games, 2) if total_games > 0 else 0,
            'assists_per_game': round(total_assists / total_games, 2) if total_games > 0 else 0
        }
    
    def best_scorer(self):
        """
        Find the player with the most goals.
        
        Returns:
            SoccerPlayer: The player with the most goals, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.goals)
    
    def best_assistant(self):
        """
        Find the player with the most assists.
        
        Returns:
            SoccerPlayer: The player with the most assists, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.assists)
    
    def most_efficient_player(self):
        """
        Find the player with the highest efficiency score.
        
        Returns:
            SoccerPlayer: The player with the highest efficiency score, or None if no players
        """
        if not self.players:
            return None
        
        return max(self.players, key=lambda player: player.efficiency_score())
    
    def export_to_csv(self, filename=None):
        """
        Export team data to CSV file for analysis.
        
        Args:
            filename (str): Output filename (defaults to team_name_timestamp.csv)
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.name.replace(' ', '_')}_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['player_id', 'first_name', 'last_name', 'position', 'team',
                         'games_played', 'minutes', 'goals', 'assists', 'shots',
                         'shots_on_goal', 'yellow_cards', 'red_cards', 
                         'fouls_committed', 'fouls_suffered', 'efficiency_score',
                         'goals_per_90', 'assists_per_90', 'shot_accuracy', 'conversion_rate']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for player in self.players:
                writer.writerow({
                    'player_id': player.player_id,
                    'first_name': player.first_name,
                    'last_name': player.last_name,
                    'position': player.position,
                    'team': player.team,
                    'games_played': player.games_played,
                    'minutes': player.minutes,
                    'goals': player.goals,
                    'assists': player.assists,
                    'shots': player.shots,
                    'shots_on_goal': player.shots_on_goal,
                    'yellow_cards': player.yellow_cards,
                    'red_cards': player.red_cards,
                    'fouls_committed': player.fouls_committed,
                    'fouls_suffered': player.fouls_suffered,
                    'efficiency_score': round(player.efficiency_score(), 2),
                    'goals_per_90': round(player.goals_per_90(), 2),
                    'assists_per_90': round(player.assists_per_90(), 2),
                    'shot_accuracy': round(player.shot_accuracy(), 2),
                    'conversion_rate': round(player.conversion_rate(), 2)
                })
        
        print(f"Team data exported to {filename}")
        return filename
    
    def import_from_csv(self, filename):
        """
        Import team data from CSV file.
        
        Args:
            filename (str): Input CSV filename
        """
        self.players = []  # Clear existing players
        
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Create player with basic info
                player = SoccerPlayer(
                    row['player_id'],
                    row['first_name'],
                    row['last_name'],
                    row['position'],
                    row['team']
                )
                
                # Update stats from CSV
                player.update_stats(
                    games=int(row['games_played']),
                    minutes=int(row['minutes']),
                    goals=int(row['goals']),
                    assists=int(row['assists']),
                    shots=int(row['shots']),
                    shots_on_goal=int(row['shots_on_goal']),
                    yellow_cards=int(row['yellow_cards']),
                    red_cards=int(row['red_cards']),
                    fouls_committed=int(row['fouls_committed']),
                    fouls_suffered=int(row['fouls_suffered'])
                )
                
                self.players.append(player)
        
        print(f"Imported {len(self.players)} players from {filename}")
    
    def save_to_json(self, filename=None):
        """
        Save team data to JSON format for web applications.
        
        Args:
            filename (str): Output filename (defaults to team_name.json)
        """
        if filename is None:
            filename = f"{self.name.replace(' ', '_')}.json"
        
        team_data = {
            'team_name': self.name,
            'last_updated': datetime.now().isoformat(),
            'team_stats': self.team_stats(),
            'players': []
        }
        
        for player in self.players:
            player_data = {
                'player_id': player.player_id,
                'name': player.full_name(),
                'position': player.position,
                'stats': {
                    'games_played': player.games_played,
                    'minutes': player.minutes,
                    'goals': player.goals,
                    'assists': player.assists,
                    'shots': player.shots,
                    'shots_on_goal': player.shots_on_goal,
                    'yellow_cards': player.yellow_cards,
                    'red_cards': player.red_cards,
                    'fouls_committed': player.fouls_committed,
                    'fouls_suffered': player.fouls_suffered
                },
                'metrics': {
                    'efficiency_score': round(player.efficiency_score(), 2),
                    'goals_per_90': round(player.goals_per_90(), 2),
                    'assists_per_90': round(player.assists_per_90(), 2),
                    'shot_accuracy': round(player.shot_accuracy(), 2),
                    'conversion_rate': round(player.conversion_rate(), 2),
                    'goal_contributions': player.goal_contributions(),
                    'card_ratio': round(player.card_ratio(), 2),
                    'fouls_ratio': round(player.fouls_ratio(), 2)
                }
            }
            team_data['players'].append(player_data)
        
        with open(filename, 'w') as jsonfile:
            json.dump(team_data, jsonfile, indent=2)
        
        print(f"Team data saved to {filename}")
        return filename


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
    
    # Export data for analysis
    print("\n--- Data Export Demo ---")
    csv_file = team.export_to_csv()
    json_file = team.save_to_json()
    
    print(f"\nData exported to:")
    print(f"- CSV: {csv_file} (for data analysis in pandas, Excel, etc.)")
    print(f"- JSON: {json_file} (for web applications, APIs)")
    
    # Demo importing data
    print("\n--- Data Import Demo ---")
    new_team = Team("Imported Team")
    new_team.import_from_csv(csv_file)
    print(f"Successfully loaded {len(new_team.players)} players")

if __name__ == "__main__":
    main()