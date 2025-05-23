class Player:
    """
    A class representing a soccer player.
    
    Attributes:
        name (str): The player's name
        position (str): The player's position (GK, DEF, MID, FWD)
        number (int): The player's jersey number
        team (SoccerTeam): The player's current team
        goals (int): Number of goals scored
        assists (int): Number of assists made
        yellow_cards (int): Number of yellow cards received
        red_cards (int): Number of red cards received
        minutes_played (int): Total minutes played
    """
    
    def __init__(self, name, position, number, team=None):
        """
        Initialize a new Player instance.
        
        Args:
            name (str): The player's name
            position (str): The player's position
            number (int): The player's jersey number
            team (SoccerTeam, optional): The player's team. Defaults to None.
        """
        self.name = name
        self.position = position
        self.number = number
        self.team = team
        
        # Statistics
        self.goals = 0
        self.assists = 0
        self.yellow_cards = 0
        self.red_cards = 0
        self.minutes_played = 0
    
    def score_goal(self):
        """
        Increment the player's goal count.
        
        Returns:
            int: The updated goal count
        """
        self.goals += 1
        return self.goals
    
    def make_assist(self):
        """
        Increment the player's assist count.
        
        Returns:
            int: The updated assist count
        """
        self.assists += 1
        return self.assists
    
    def receive_card(self, card_type):
        """
        Record a card received by the player.
        
        Args:
            card_type (str): The type of card ("yellow" or "red")
            
        Returns:
            int: The updated count for the specific card type
        """
        if card_type == "yellow":
            self.yellow_cards += 1
            return self.yellow_cards
        elif card_type == "red":
            self.red_cards += 1
            return self.red_cards
        else:
            raise ValueError("Card type must be 'yellow' or 'red'")
    
    def add_playing_time(self, minutes):
        """
        Add to the player's total minutes played.
        
        Args:
            minutes (int): Number of minutes to add
            
        Returns:
            int: The updated total minutes played
        """
        self.minutes_played += minutes
        return self.minutes_played
    
    def get_stats(self):
        """
        Get the player's current statistics.
        
        Returns:
            dict: A dictionary of player statistics
        """
        return {
            "name": self.name,
            "position": self.position,
            "number": self.number,
            "team": self.team.team_name if self.team else None,
            "goals": self.goals,
            "assists": self.assists,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "minutes_played": self.minutes_played
        }
    
    def __str__(self):
        """
        Return a string representation of the player.
        
        Returns:
            str: A formatted string describing the player
        """
        team_info = f" ({self.team.team_name})" if self.team else ""
        return f"{self.name} (#{self.number}, {self.position}){team_info}"


class SoccerTeam:
    """
    A class representing a soccer team with financial and performance tracking.
    
    Attributes:
        team_name (str): The name of the team
        coach_name (str): The name of the team's coach
        budget (float): The team's current budget
        roster (list): List of Player objects in the team
        matches_played (int): Number of matches played
        wins (int): Number of matches won
        draws (int): Number of matches drawn
        losses (int): Number of matches lost
        goals_scored (int): Total goals scored by the team
        goals_conceded (int): Total goals conceded by the team
    """
    
    def __init__(self, team_name, coach_name, initial_budget=0):
        """
        Initialize a new SoccerTeam instance.
        
        Args:
            team_name (str): The name of the team
            coach_name (str): The name of the team's coach
            initial_budget (float, optional): The starting budget. Defaults to 0.
            
        Raises:
            ValueError: If initial_budget is negative
        """
        if initial_budget < 0:
            raise ValueError("Initial budget cannot be negative")
        
        self.team_name = team_name
        self.coach_name = coach_name
        self.budget = initial_budget
        self.roster = []  # List to store Player objects
        
        # Initialize performance tracking
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0
    
    def add_funds(self, amount):
        """
        Add funds to the team's budget.
        
        Args:
            amount (float): The amount to add
            
        Returns:
            float: The new budget
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative")
        
        self.budget += amount
        return self.budget
    
    def spend_funds(self, amount):
        """
        Spend funds from the team's budget.
        
        Args:
            amount (float): The amount to spend
            
        Returns:
            float: The new budget
            
        Raises:
            ValueError: If amount is negative or exceeds current budget
        """
        if amount < 0:
            raise ValueError("Amount to spend cannot be negative")
        if amount > self.budget:
            raise ValueError("Insufficient funds")
        
        self.budget -= amount
        return self.budget
    
    def get_balance(self):
        """
        Get the current budget balance.
        
        Returns:
            float: The current budget
        """
        return self.budget
    
    def add_player(self, player):
        """
        Add a player to the team's roster.
        
        Args:
            player (Player): The player to add
            
        Returns:
            list: The updated roster
        """
        self.roster.append(player)
        player.team = self  # Update the player's team reference
        return self.roster
    
    def remove_player(self, player):
        """
        Remove a player from the team's roster.
        
        Args:
            player (Player): The player to remove
            
        Returns:
            list: The updated roster
            
        Raises:
            ValueError: If player is not in the roster
        """
        if player in self.roster:
            self.roster.remove(player)
            player.team = None  # Clear the player's team reference
            return self.roster
        else:
            raise ValueError("Player not found in the roster")
    
    def get_player_by_name(self, name):
        """
        Find a player in the roster by name.
        
        Args:
            name (str): The name of the player to find
            
        Returns:
            Player or None: The found player or None if not found
        """
        for player in self.roster:
            if player.name == name:
                return player
        return None
    
    def get_player_by_number(self, number):
        """
        Find a player in the roster by jersey number.
        
        Args:
            number (int): The jersey number of the player to find
            
        Returns:
            Player or None: The found player or None if not found
        """
        for player in self.roster:
            if player.number == number:
                return player
        return None
    
    def get_team_stats(self):
        """
        Get the team's current performance statistics.
        
        Returns:
            dict: A dictionary with team stats
        """
        return {
            'team_name': self.team_name,
            'matches_played': self.matches_played,
            'wins': self.wins,
            'draws': self.draws,
            'losses': self.losses,
            'goals_scored': self.goals_scored,
            'goals_conceded': self.goals_conceded,
            'goal_difference': self.goals_scored - self.goals_conceded,
            'points': (self.wins * 3) + self.draws
        }
    
    def record_match_result(self, goals_for, goals_against):
        """
        Record the result of a match and update team statistics.
        
        Args:
            goals_for (int): Goals scored by this team
            goals_against (int): Goals scored by the opponent
            
        Returns:
            dict: A dictionary with updated team stats
        """
        self.matches_played += 1
        self.goals_scored += goals_for
        self.goals_conceded += goals_against
        
        if goals_for > goals_against:
            self.wins += 1
        elif goals_for == goals_against:
            self.draws += 1
        else:
            self.losses += 1
        
        return self.get_team_stats()
    
    def __str__(self):
        """
        Return a string representation of the team.
        
        Returns:
            str: A formatted string describing the team
        """
        return f"{self.team_name} (Coach: {self.coach_name}, Players: {len(self.roster)})"


class SoccerField:
    """
    A class representing a soccer field with specific dimensions and conditions.
    
    Attributes:
        length (float): The length of the field in meters
        width (float): The width of the field in meters
        surface_type (str): The type of field surface (e.g., "grass", "artificial")
        condition_rating (int): The field condition rating from 0-100
    """
    
    def __init__(self, length, width, surface_type="grass"):
        """
        Initialize a new SoccerField instance.
        
        Args:
            length (float): The length of the field in meters
            width (float): The width of the field in meters
            surface_type (str, optional): The type of field surface. Defaults to "grass".
            
        Raises:
            ValueError: If length or width is not positive
        """
        if length <= 0 or width <= 0:
            raise ValueError("Field dimensions must be positive")
        
        self.length = length
        self.width = width
        self.surface_type = surface_type
        self.condition_rating = 100  # Perfect condition initially
    
    def area(self):
        """
        Calculate the total area of the field.
        
        Returns:
            float: The area in square meters
        """
        return self.length * self.width
    
    def penalty_box_area(self):
        """
        Calculate the area of the penalty box.
        
        Returns:
            float: The penalty box area in square meters
        """
        # Standard penalty box is 16.5m x 40.3m
        penalty_box_length = 16.5
        penalty_box_width = 40.3
        return penalty_box_length * penalty_box_width
    
    def is_regulation_size(self):
        """
        Check if the field dimensions meet FIFA regulations.
        
        Returns:
            bool: True if the field meets regulation size, False otherwise
        """
        # FIFA regulation field is between 90-120m length and 45-90m width
        return (90 <= self.length <= 120) and (45 <= self.width <= 90)
    
    def update_condition(self, weather_impact=-5):
        """
        Update the field condition rating based on weather or use.
        
        Args:
            weather_impact (int, optional): The impact on the condition (-100 to 100). 
                                         Defaults to -5 (slight deterioration).
            
        Returns:
            int: The new condition rating
        """
        self.condition_rating += weather_impact
        
        # Ensure condition stays within valid range
        if self.condition_rating < 0:
            self.condition_rating = 0
        if self.condition_rating > 100:
            self.condition_rating = 100
            
        return self.condition_rating


class SoccerMatch:
    """
    A class representing a soccer match with teams, score tracking, and match events.
    
    Attributes:
        home_team (SoccerTeam): The home team
        away_team (SoccerTeam): The away team
        match_date (str): The date of the match
        venue (str): The venue where the match is played
        home_goals (int): Goals scored by the home team
        away_goals (int): Goals scored by the away team
        match_events (list): List of events during the match
        is_completed (bool): Whether the match is completed
        players_played (list): List of players who played in the match
    """
    
    def __init__(self, home_team, away_team, match_date, venue):
        """
        Initialize a new SoccerMatch instance.
        
        Args:
            home_team (SoccerTeam): The home team
            away_team (SoccerTeam): The away team
            match_date (str): The date of the match
            venue (str): The venue where the match is played
        """
        self.home_team = home_team
        self.away_team = away_team
        self.match_date = match_date
        self.venue = venue
        
        self.home_goals = 0
        self.away_goals = 0
        self.match_events = []
        self.is_completed = False
        self.players_played = []  # Track players who participated
    
    def add_player_to_match(self, player, starting_minute=0):
        """
        Add a player to the match and record starting time.
        
        Args:
            player (Player): The player to add to the match
            starting_minute (int, optional): The minute when the player entered. Defaults to 0 (starter).
            
        Returns:
            list: Updated players_played list
            
        Raises:
            ValueError: If player's team is not playing in this match
        """
        if player.team != self.home_team and player.team != self.away_team:
            raise ValueError("Player's team is not playing in this match")
        
        # Create player participation record
        participation = {
            'player': player,
            'starting_minute': starting_minute,
            'ending_minute': None,  # Will be set when subbed off or match ends
            'played_full_match': False
        }
        
        self.players_played.append(participation)
        return self.players_played
    
    def substitute_player(self, player_out, player_in, minute):
        """
        Substitute one player for another during the match.
        
        Args:
            player_out (Player): The player leaving the field
            player_in (Player): The player entering the field
            minute (int): The minute when the substitution occurred
            
        Returns:
            dict: A dictionary describing the substitution
            
        Raises:
            ValueError: If either player's team is not playing or player_out not found
        """
        if player_out.team != self.home_team and player_out.team != self.away_team:
            raise ValueError("Player's team is not playing in this match")
        
        if player_in.team != self.home_team and player_in.team != self.away_team:
            raise ValueError("Player's team is not playing in this match")
        
        # Find the player_out in the players_played list
        found = False
        for p in self.players_played:
            if p['player'] == player_out and p['ending_minute'] is None:
                p['ending_minute'] = minute
                p['played_full_match'] = False
                found = True
                break
        
        if not found:
            raise ValueError("Player to substitute out was not found in the active players")
        
        # Add the new player
        self.add_player_to_match(player_in, minute)
        
        # Create substitution event
        sub_event = {
            'team': player_out.team.team_name,
            'player_out': player_out.name,
            'player_in': player_in.name,
            'minute': minute,
            'event_type': 'substitution'
        }
        
        self.match_events.append(sub_event)
        return sub_event
    
    def add_goal(self, player, minute, assist_player=None):
        """
        Record a goal in the match.
        
        Args:
            player (Player): The player who scored
            minute (int): The minute when the goal was scored
            assist_player (Player, optional): The player who made the assist
            
        Returns:
            tuple: The current score as (home_goals, away_goals)
            
        Raises:
            ValueError: If player's team is not playing in this match
        """
        if player.team != self.home_team and player.team != self.away_team:
            raise ValueError("Player's team is not playing in this match")
        
        if assist_player and (assist_player.team != self.home_team and assist_player.team != self.away_team):
            raise ValueError("Assist player's team is not playing in this match")
        
        # Update player stats
        player.score_goal()
        if assist_player:
            assist_player.make_assist()
        
        # Create event dictionary
        goal_event = {
            'team': player.team.team_name,
            'player': player.name,
            'player_number': player.number,
            'minute': minute,
            'event_type': 'goal',
            'assist': assist_player.name if assist_player else None
        }
        
        self.match_events.append(goal_event)
        
        # Update score
        if player.team == self.home_team:
            self.home_goals += 1
        else:
            self.away_goals += 1
        
        return (self.home_goals, self.away_goals)
    
    def add_card(self, player, card_type, minute):
        """
        Record a card given in the match.
        
        Args:
            player (Player): The player who received the card
            card_type (str): The type of card ("yellow" or "red")
            minute (int): The minute when the card was given
            
        Returns:
            dict: The card event dictionary
            
        Raises:
            ValueError: If the card type is invalid or player's team is not playing
        """
        if player.team != self.home_team and player.team != self.away_team:
            raise ValueError("Player's team is not playing in this match")
        
        if card_type not in ["yellow", "red"]:
            raise ValueError("Card type must be 'yellow' or 'red'")
        
        # Update player stats
        player.receive_card(card_type)
        
        # Create event dictionary
        card_event = {
            'team': player.team.team_name,
            'player': player.name,
            'player_number': player.number,
            'card_type': card_type,
            'minute': minute,
            'event_type': 'card'
        }
        
        self.match_events.append(card_event)
        
        return card_event
    
    def complete_match(self, final_minute=90):
        """
        Mark the match as completed and update team statistics.
        
        Args:
            final_minute (int, optional): The minute when the match ended. Defaults to 90.
            
        Returns:
            dict: A dictionary with the match result
            
        Raises:
            ValueError: If the match is already completed
        """
        if self.is_completed:
            raise ValueError("Match already completed")
        
        self.is_completed = True
        
        # Update player stats for minutes played
        for p in self.players_played:
            if p['ending_minute'] is None:
                # Player stayed on until the end
                p['ending_minute'] = final_minute
                p['played_full_match'] = (p['starting_minute'] == 0)
                
                # Update player's total minutes
                played_minutes = final_minute - p['starting_minute']
                p['player'].add_playing_time(played_minutes)
        
        # Update home team's stats
        self.home_team.record_match_result(self.home_goals, self.away_goals)
        
        # Update away team's stats
        self.away_team.record_match_result(self.away_goals, self.home_goals)
        
        return {
            'home_team': self.home_team.team_name,
            'away_team': self.away_team.team_name,
            'score': f"{self.home_goals}-{self.away_goals}",
            'winner': self.home_team.team_name if self.home_goals > self.away_goals else 
                     (self.away_team.team_name if self.away_goals > self.home_goals else "Draw"),
            'date': self.match_date,
            'venue': self.venue,
            'events': len(self.match_events)
        }
    
    def get_match_stats(self):
        """
        Get detailed statistics for the match.
        
        Returns:
            dict: A dictionary with match statistics
        """
        # Count events by type
        goal_count = sum(1 for event in self.match_events if event['event_type'] == 'goal')
        card_count = sum(1 for event in self.match_events if event['event_type'] == 'card')
        yellow_cards = sum(1 for event in self.match_events if event['event_type'] == 'card' and event['card_type'] == 'yellow')
        red_cards = sum(1 for event in self.match_events if event['event_type'] == 'card' and event['card_type'] == 'red')
        substitutions = sum(1 for event in self.match_events if event['event_type'] == 'substitution')
        
        return {
            'score': f"{self.home_goals}-{self.away_goals}",
            'total_goals': goal_count,
            'total_cards': card_count,
            'yellow_cards': yellow_cards,
            'red_cards': red_cards,
            'substitutions': substitutions,
            'status': 'Completed' if self.is_completed else 'In Progress',
            'home_team': self.home_team.team_name,
            'away_team': self.away_team.team_name
        }
    
    def __str__(self):
        """
        Return a string representation of the match.
        
        Returns:
            str: A formatted string describing the match
        """
        if self.is_completed:
            result = f"{self.home_team.team_name} {self.home_goals} - {self.away_goals} {self.away_team.team_name}"
            return f"Match Result: {result} (Played on {self.match_date} at {self.venue})"
        else:
            return f"Scheduled Match: {self.home_team.team_name} vs {self.away_team.team_name} on {self.match_date} at {self.venue}"


def main():
    """Test the improved soccer management system with example usage."""
    print("Testing Improved Soccer Team Management System...")
    
    # Create teams
    barcelona = SoccerTeam("FC Barcelona", "Xavi Hernandez", 100000000)
    real_madrid = SoccerTeam("Real Madrid", "Carlo Ancelotti", 120000000)
    
    # Create players for Barcelona
    print("\nCreating players for Barcelona:")
    lewandowski = Player("Robert Lewandowski", "FWD", 9)
    gavi = Player("Pablo Gavi", "MID", 6)
    ter_stegen = Player("Marc-André ter Stegen", "GK", 1)
    pedri = Player("Pedri González", "MID", 8)
    araujo = Player("Ronald Araújo", "DEF", 4)
    
    # Add players to Barcelona
    barcelona.add_player(lewandowski)
    barcelona.add_player(gavi)
    barcelona.add_player(ter_stegen)
    barcelona.add_player(pedri)
    barcelona.add_player(araujo)
    
    # Create players for Real Madrid
    print("Creating players for Real Madrid:")
    mbappe = Player("Kylian Mbappé", "FWD", 9)
    modric = Player("Luka Modrić", "MID", 10)
    courtois = Player("Thibaut Courtois", "GK", 1)
    rudiger = Player("Antonio Rüdiger", "DEF", 2)
    vinicius = Player("Vinícius Júnior", "FWD", 7)
    
    # Add players to Real Madrid
    real_madrid.add_player(mbappe)
    real_madrid.add_player(modric)
    real_madrid.add_player(courtois)
    real_madrid.add_player(rudiger)
    real_madrid.add_player(vinicius)
    
    # Test team finances
    print(f"\n{barcelona.team_name} initial budget: ${barcelona.get_balance():,}")
    barcelona.spend_funds(25000000)
    print(f"After transfer spending: ${barcelona.get_balance():,}")
    barcelona.add_funds(10000000)
    print(f"After sponsorship deal: ${barcelona.get_balance():,}")
    
    # Create a field
    camp_nou = SoccerField(105, 68, "grass")
    print(f"\nCamp Nou area: {camp_nou.area()} square meters")
    print(f"Is regulation size: {camp_nou.is_regulation_size()}")
    print(f"Initial condition: {camp_nou.condition_rating}/100")
    print(f"Condition after rain: {camp_nou.update_condition(-15)}/100")
    
    # Create a match
    el_clasico = SoccerMatch(barcelona, real_madrid, "2025-05-22", "Camp Nou")
    print(f"\n{el_clasico}")
    
    # Add players to the match
    print("\nAdding players to the match:")
    # Add Barcelona starters
    el_clasico.add_player_to_match(lewandowski)
    el_clasico.add_player_to_match(gavi)
    el_clasico.add_player_to_match(ter_stegen)
    el_clasico.add_player_to_match(pedri)
    el_clasico.add_player_to_match(araujo)
    
    # Add Real Madrid starters
    el_clasico.add_player_to_match(mbappe)
    el_clasico.add_player_to_match(modric)
    el_clasico.add_player_to_match(courtois)
    el_clasico.add_player_to_match(rudiger)
    el_clasico.add_player_to_match(vinicius)
    
    # Record match events
    print("\nRecording match events:")
    el_clasico.add_goal(lewandowski, 23)
    print(f"Goal by {lewandowski.name} at 23'")
    
    el_clasico.add_goal(mbappe, 45)
    print(f"Goal by {mbappe.name} at 45'")
    
    el_clasico.add_goal(gavi, 67, lewandowski)
    print(f"Goal by {gavi.name} at 67' (Assist: {lewandowski.name})")
    
    el_clasico.add_card(rudiger, "yellow", 70)
    print(f"Yellow card to {rudiger.name} at 70'")
    
    # Make a substitution
    sub = el_clasico.substitute_player(modric, Player("Eduardo Camavinga", "MID", 12, real_madrid), 75)
    print(f"Substitution at 75': {sub['player_out']} off, {sub['player_in']} on")
    
    # Complete the match
    result = el_clasico.complete_match()
    print(f"\nMatch completed: {el_clasico}")
    
    # Print match stats
    match_stats = el_clasico.get_match_stats()
    print("\nMatch Statistics:")
    for key, value in match_stats.items():
        print(f"{key}: {value}")
    
    # Check team stats
    print(f"\n{barcelona.team_name} stats:")
    team_stats = barcelona.get_team_stats()
    for key, value in team_stats.items():
        print(f"{key}: {value}")
    
    print(f"\n{real_madrid.team_name} stats:")
    team_stats = real_madrid.get_team_stats()
    for key, value in team_stats.items():
        print(f"{key}: {value}")
    
    # Check player stats
    print("\nPlayer Statistics:")
    for player in [lewandowski, gavi, mbappe, rudiger]:
        stats = player.get_stats()
        print(f"\n{player.name} (#{player.number}, {player.position}):")
        for key, value in stats.items():
            if key not in ["name", "position", "number"]:
                print(f"  {key}: {value}")


if __name__ == "__main__":
    main()