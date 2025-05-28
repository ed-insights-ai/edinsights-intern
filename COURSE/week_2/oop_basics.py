class SoccerTeam:
    """
    A class representing a soccer team with financial and performance tracking.
    
    Attributes:
        team_name (str): The name of the team
        coach_name (str): The name of the team's coach
        budget (float): The team's current budget
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
        
        return {
            'matches_played': self.matches_played,
            'wins': self.wins,
            'draws': self.draws,
            'losses': self.losses,
            'goals_scored': self.goals_scored,
            'goals_conceded': self.goals_conceded
        }


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
    
    def add_goal(self, team, player_name, minute):
        """
        Record a goal in the match.
        
        Args:
            team (SoccerTeam): The team that scored
            player_name (str): The name of the player who scored
            minute (int): The minute when the goal was scored
            
        Returns:
            tuple: The current score as (home_goals, away_goals)
            
        Raises:
            ValueError: If the team is not playing in this match
        """
        if team != self.home_team and team != self.away_team:
            raise ValueError("Team is not playing in this match")
        
        # Create event dictionary
        goal_event = {
            'team': team.team_name,
            'player_name': player_name,
            'minute': minute,
            'event_type': 'goal'
        }
        
        self.match_events.append(goal_event)
        
        # Update score
        if team == self.home_team:
            self.home_goals += 1
        else:
            self.away_goals += 1
        
        return (self.home_goals, self.away_goals)
    
    def add_card(self, team, player_name, card_type, minute):
        """
        Record a card given in the match.
        
        Args:
            team (SoccerTeam): The team of the player who received the card
            player_name (str): The name of the player who received the card
            card_type (str): The type of card ("yellow" or "red")
            minute (int): The minute when the card was given
            
        Returns:
            list: The updated match events list
            
        Raises:
            ValueError: If the card type is invalid or the team is not playing
        """
        if team != self.home_team and team != self.away_team:
            raise ValueError("Team is not playing in this match")
        
        if card_type not in ["yellow", "red"]:
            raise ValueError("Card type must be 'yellow' or 'red'")
        
        # Create event dictionary
        card_event = {
            'team': team.team_name,
            'player_name': player_name,
            'card_type': card_type,
            'minute': minute,
            'event_type': 'card'
        }
        
        self.match_events.append(card_event)
        
        return self.match_events
    
    def complete_match(self):
        """
        Mark the match as completed and update team statistics.
        
        Returns:
            dict: A dictionary with the match result
            
        Raises:
            ValueError: If the match is already completed
        """
        if self.is_completed:
            raise ValueError("Match already completed")
        
        self.is_completed = True
        
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
            'venue': self.venue
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
    """Test the soccer management system with example usage."""
    print("Testing Soccer Team Management System...")
    
    # Create teams
    barcelona = SoccerTeam("FC Barcelona", "Xavi Hernandez", 100000000)
    real_madrid = SoccerTeam("Real Madrid", "Carlo Ancelotti", 120000000)
    
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
    
    # Record match events
    el_clasico.add_goal(barcelona, "Lewandowski", 23)
    el_clasico.add_goal(real_madrid, "Mbappé", 45)
    el_clasico.add_goal(barcelona, "Gavi", 67)
    el_clasico.add_card(real_madrid, "Rüdiger", "yellow", 70)
    
    # Complete the match
    result = el_clasico.complete_match()
    print(f"\nMatch completed: {el_clasico}")
    
    # Check team stats
    print(f"\n{barcelona.team_name} stats:")
    print(f"Matches: {barcelona.matches_played}, Wins: {barcelona.wins}, Draws: {barcelona.draws}, Losses: {barcelona.losses}")
    print(f"Goals scored: {barcelona.goals_scored}, Goals conceded: {barcelona.goals_conceded}")
    
    print(f"\n{real_madrid.team_name} stats:")
    print(f"Matches: {real_madrid.matches_played}, Wins: {real_madrid.wins}, Draws: {real_madrid.draws}, Losses: {real_madrid.losses}")
    print(f"Goals scored: {real_madrid.goals_scored}, Goals conceded: {real_madrid.goals_conceded}")


if __name__ == "__main__":
    main()