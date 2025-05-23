"""
Class Hierarchy Implementation for Soccer League
----------------------------
Implements the soccer league class hierarchy according to the specified requirements.
This exercise focuses on inheritance, polymorphism, and method overriding.
"""

import random  # For simulating random events in matches

class Person:
    """
    Base class for all people in the soccer domain.
    
    Attributes:
        first_name (str): The person's first name
        last_name (str): The person's last name
        age (int): The person's age
        nationality (str): The person's nationality
        
    Methods:
        full_name(): Return the person's full name
        __str__(): Return a string representation of the person
    """
    
    def __init__(self, first_name, last_name, age, nationality):
        """
        Initialize a new Person instance.
        
        Args:
            first_name (str): The person's first name
            last_name (str): The person's last name
            age (int): The person's age
            nationality (str): The person's nationality
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    
    def full_name(self):
        """Return the person's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        """Return a string representation of the Person."""
        return f"{self.full_name()}, {self.age}, {self.nationality}"


class Player(Person):
    """
    Class representing a soccer player.
    
    Additional Attributes:
        position (str): The player's position
        jersey_number (int): The player's jersey number
        dominant_foot (str): The player's dominant foot
        goals (int): Number of goals scored
        assists (int): Number of assists made
        matches_played (int): Number of matches played
        minutes_played (int): Total minutes played
        
    Methods:
        score_goal(): Record a goal for the player
        record_assist(): Record an assist for the player
        play_match(minutes_played): Record playing in a match
        __str__(): Return a string representation of the player
    """
    
    def __init__(self, first_name, last_name, age, nationality, position, jersey_number, dominant_foot="right"):
        """
        Initialize a new Player instance.
        
        Args:
            first_name (str): The player's first name
            last_name (str): The player's last name
            age (int): The player's age
            nationality (str): The player's nationality
            position (str): The player's position
            jersey_number (int): The player's jersey number
            dominant_foot (str, optional): The player's dominant foot. Defaults to "right".
        """
        super().__init__(first_name, last_name, age, nationality)
        self.position = position
        self.jersey_number = jersey_number
        self.dominant_foot = dominant_foot
        self.goals = 0
        self.assists = 0
        self.matches_played = 0
        self.minutes_played = 0
    
    def score_goal(self):
        """
        Record a goal for the player.
        
        Returns:
            int: Updated goals count
        """
        self.goals += 1
        return self.goals
    
    def record_assist(self):
        """
        Record an assist for the player.
        
        Returns:
            int: Updated assists count
        """
        self.assists += 1
        return self.assists
    
    def play_match(self, minutes_played):
        """
        Record that the player played in a match.
        
        Args:
            minutes_played (int): Minutes played in the match
        
        Returns:
            int: Total matches played
        """
        self.matches_played += 1
        self.minutes_played += minutes_played
        return self.matches_played
    
    def __str__(self):
        """Return a string representation of the Player."""
        return f"{self.full_name()}, #{self.jersey_number}, {self.position}"


class StaffMember(Person):
    """
    Class representing a staff member of a soccer team.
    
    Additional Attributes:
        role (str): The staff member's role
        years_of_experience (int): Years of experience in the role
        
    Methods:
        describe_role(): Return a description of the staff member's role
        add_experience(years): Add years of experience
        __str__(): Return a string representation of the staff member
    """
    
    def __init__(self, first_name, last_name, age, nationality, role, years_of_experience):
        """
        Initialize a new StaffMember instance.
        
        Args:
            first_name (str): The staff member's first name
            last_name (str): The staff member's last name
            age (int): The staff member's age
            nationality (str): The staff member's nationality
            role (str): The staff member's role
            years_of_experience (int): Years of experience in the role
        """
        super().__init__(first_name, last_name, age, nationality)
        self.role = role
        self.years_of_experience = years_of_experience
    
    def describe_role(self):
        """Return a description of the staff member's role."""
        return f"{self.full_name()} works as a {self.role} with {self.years_of_experience} years of experience."
    
    def add_experience(self, years):
        """
        Add years of experience.
        
        Args:
            years (int): Years to add to experience
            
        Returns:
            int: Updated years of experience
        """
        self.years_of_experience += years
        return self.years_of_experience
    
    def __str__(self):
        """Return a string representation of the StaffMember."""
        return f"{self.full_name()}, {self.role}, {self.years_of_experience} years experience"


class Goalkeeper(Player):
    """
    Class representing a goalkeeper.
    
    Additional Attributes:
        saves (int): Number of saves made
        clean_sheets (int): Number of clean sheets kept
        goals_conceded (int): Number of goals conceded
        
    Methods:
        make_save(): Record a save for the goalkeeper
        record_clean_sheet(): Record a clean sheet for the goalkeeper
        concede_goal(): Record a conceded goal for the goalkeeper
        save_percentage(): Calculate save percentage
    """
    
    def __init__(self, first_name, last_name, age, nationality, jersey_number, dominant_foot="right"):
        """
        Initialize a new Goalkeeper instance.
        
        Args:
            first_name (str): The goalkeeper's first name
            last_name (str): The goalkeeper's last name
            age (int): The goalkeeper's age
            nationality (str): The goalkeeper's nationality
            jersey_number (int): The goalkeeper's jersey number
            dominant_foot (str, optional): The goalkeeper's dominant foot. Defaults to "right".
        """
        super().__init__(first_name, last_name, age, nationality, "Goalkeeper", jersey_number, dominant_foot)
        self.saves = 0
        self.clean_sheets = 0
        self.goals_conceded = 0
    
    def make_save(self):
        """
        Record a save for the goalkeeper.
        
        Returns:
            int: Updated saves count
        """
        self.saves += 1
        return self.saves
    
    def record_clean_sheet(self):
        """
        Record a clean sheet for the goalkeeper.
        
        Returns:
            int: Updated clean sheets count
        """
        self.clean_sheets += 1
        return self.clean_sheets
    
    def concede_goal(self):
        """
        Record a conceded goal for the goalkeeper.
        
        Returns:
            int: Updated goals conceded count
        """
        self.goals_conceded += 1
        return self.goals_conceded
    
    def save_percentage(self):
        """
        Calculate save percentage.
        
        Returns:
            float: Save percentage (saves / (saves + goals_conceded)) * 100
        """
        total_shots = self.saves + self.goals_conceded
        if total_shots == 0:
            return 0
        return (self.saves / total_shots) * 100


class FieldPlayer(Player):
    """
    Class representing a field player (non-goalkeeper).
    
    Additional Attributes:
        passes_completed (int): Number of passes completed
        tackles (int): Number of tackles made
        distance_covered (float): Total distance covered in kilometers
        
    Methods:
        complete_pass(): Record a completed pass
        make_tackle(): Record a tackle
        cover_distance(kilometers): Record distance covered
        position_rating(): Calculate position-specific performance rating
    """
    
    def __init__(self, first_name, last_name, age, nationality, position, jersey_number, dominant_foot="right"):
        """
        Initialize a new FieldPlayer instance.
        
        Args:
            first_name (str): The field player's first name
            last_name (str): The field player's last name
            age (int): The field player's age
            nationality (str): The field player's nationality
            position (str): The field player's position
            jersey_number (int): The field player's jersey number
            dominant_foot (str, optional): The field player's dominant foot. Defaults to "right".
            
        Raises:
            ValueError: If position is "Goalkeeper"
        """
        if position == "Goalkeeper":
            raise ValueError("FieldPlayer cannot have Goalkeeper position")
        super().__init__(first_name, last_name, age, nationality, position, jersey_number, dominant_foot)
        self.passes_completed = 0
        self.tackles = 0
        self.distance_covered = 0
    
    def complete_pass(self):
        """
        Record a completed pass for the field player.
        
        Returns:
            int: Updated passes completed count
        """
        self.passes_completed += 1
        return self.passes_completed
    
    def make_tackle(self):
        """
        Record a tackle for the field player.
        
        Returns:
            int: Updated tackles count
        """
        self.tackles += 1
        return self.tackles
    
    def cover_distance(self, kilometers):
        """
        Record distance covered by the field player.
        
        Args:
            kilometers (float): Distance covered in kilometers
            
        Returns:
            float: Updated total distance covered
        """
        self.distance_covered += kilometers
        return self.distance_covered
    
    def position_rating(self):
        """
        Calculate position-specific performance rating.
        
        Returns:
            float: Performance rating based on position
        """
        if self.position == "Defender":
            # For defenders, tackles are more important
            return (self.tackles * 2 + self.passes_completed * 0.5 + self.goals * 3) / max(1, self.matches_played)
        elif self.position == "Midfielder":
            # For midfielders, passes are important
            return (self.tackles * 0.5 + self.passes_completed * 1 + self.goals * 2 + self.assists * 1.5) / max(1, self.matches_played)
        elif self.position == "Forward":
            # For forwards, goals and assists are most important
            return (self.passes_completed * 0.2 + self.goals * 3 + self.assists * 2) / max(1, self.matches_played)
        else:
            # Generic rating for other positions
            return (self.tackles + self.passes_completed + self.goals * 2 + self.assists) / max(1, self.matches_played)


class Coach(StaffMember):
    """
    Class representing a coach.
    
    Additional Attributes:
        coaching_style (str): The coach's style (e.g., "Balanced", "Attacking")
        matches (int): Number of matches coached
        wins (int): Number of wins
        draws (int): Number of draws
        losses (int): Number of losses
        preferred_formation (str): The coach's preferred formation
        
    Methods:
        record_match_result(result): Record a match result
        set_formation(formation): Set preferred formation
        win_percentage(): Calculate win percentage
    """
    
    def __init__(self, first_name, last_name, age, nationality, years_of_experience, coaching_style="Balanced"):
        """
        Initialize a new Coach instance.
        
        Args:
            first_name (str): The coach's first name
            last_name (str): The coach's last name
            age (int): The coach's age
            nationality (str): The coach's nationality
            years_of_experience (int): Years of coaching experience
            coaching_style (str, optional): The coach's style. Defaults to "Balanced".
        """
        super().__init__(first_name, last_name, age, nationality, "Coach", years_of_experience)
        self.coaching_style = coaching_style
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.preferred_formation = "4-4-2"
    
    def record_match_result(self, result):
        """
        Record a match result.
        
        Args:
            result (str): Match result - "win", "draw", or "loss"
            
        Returns:
            dict: Current coaching stats
        """
        self.matches += 1
        if result == "win":
            self.wins += 1
        elif result == "draw":
            self.draws += 1
        elif result == "loss":
            self.losses += 1
            
        return {
            "matches": self.matches,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses
        }
    
    def set_formation(self, formation):
        """
        Set preferred formation.
        
        Args:
            formation (str): New preferred formation
            
        Returns:
            str: Updated preferred formation
        """
        self.preferred_formation = formation
        return self.preferred_formation
    
    def win_percentage(self):
        """
        Calculate win percentage.
        
        Returns:
            float: Win percentage (wins / matches) * 100
        """
        if self.matches == 0:
            return 0
        return (self.wins / self.matches) * 100


class Team:
    """
    Class representing a soccer team.
    
    Attributes:
        name (str): Team name
        founded_year (int): Year the team was founded
        players (list): List of Player objects
        staff (list): List of StaffMember objects
        
    Methods:
        add_player(player): Add a player to the team
        add_staff(staff_member): Add a staff member to the team
        get_roster(): Get the full team roster
        get_starters(): Get the starting 11 players
        get_team_stats(): Get the team's overall statistics
    """
    
    def __init__(self, name, founded_year):
        """
        Initialize a new Team instance.
        
        Args:
            name (str): Team name
            founded_year (int): Year the team was founded
        """
        self.name = name
        self.founded_year = founded_year
        self.players = []
        self.staff = []
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0
    
    def add_player(self, player):
        """
        Add a player to the team.
        
        Args:
            player (Player): Player to add
            
        Returns:
            int: Number of players in the team
        """
        if not isinstance(player, Player):
            raise TypeError("Can only add Player objects to the team")
        self.players.append(player)
        return len(self.players)
    
    def add_staff(self, staff_member):
        """
        Add a staff member to the team.
        
        Args:
            staff_member (StaffMember): Staff member to add
            
        Returns:
            int: Number of staff members in the team
        """
        if not isinstance(staff_member, StaffMember):
            raise TypeError("Can only add StaffMember objects to the team")
        self.staff.append(staff_member)
        return len(self.staff)
    
    def get_roster(self):
        """
        Get the full team roster.
        
        Returns:
            dict: Dictionary containing all players and staff
        """
        # Group players by position
        position_groups = {}
        for player in self.players:
            if player.position not in position_groups:
                position_groups[player.position] = []
            position_groups[player.position].append(player)
        
        # Group staff by role
        role_groups = {}
        for staff in self.staff:
            if staff.role not in role_groups:
                role_groups[staff.role] = []
            role_groups[staff.role].append(staff)
        
        return {
            "team_name": self.name,
            "founded": self.founded_year,
            "players_by_position": position_groups,
            "staff_by_role": role_groups
        }
    
    def get_starters(self, formation="4-3-3"):
        """
        Get a potential starting 11 based on a formation.
        
        Args:
            formation (str, optional): Formation to use. Defaults to "4-3-3".
            
        Returns:
            list: List of 11 players (1 GK + 10 field players)
        """
        starters = []
        
        # Get the best goalkeeper
        goalkeepers = [p for p in self.players if p.position == "Goalkeeper"]
        if goalkeepers:
            starters.append(goalkeepers[0])
        
        # Parse the formation
        parts = formation.split("-")
        if len(parts) >= 3:
            defenders_count = int(parts[0])
            midfielders_count = int(parts[1])
            forwards_count = int(parts[2])
            
            # Get the best defenders
            defenders = [p for p in self.players if p.position == "Defender"]
            starters.extend(defenders[:defenders_count])
            
            # Get the best midfielders
            midfielders = [p for p in self.players if p.position == "Midfielder"]
            starters.extend(midfielders[:midfielders_count])
            
            # Get the best forwards
            forwards = [p for p in self.players if p.position == "Forward"]
            starters.extend(forwards[:forwards_count])
        
        return starters[:11]  # Ensure we return at most 11 players
    
    def record_match(self, opponent, goals_scored, goals_conceded):
        """
        Record a match result.
        
        Args:
            opponent (str): Name of the opponent team
            goals_scored (int): Goals scored by this team
            goals_conceded (int): Goals conceded by this team
            
        Returns:
            dict: Match result info
        """
        self.matches_played += 1
        self.goals_scored += goals_scored
        self.goals_conceded += goals_conceded
        
        result = "draw"
        if goals_scored > goals_conceded:
            result = "win"
            self.wins += 1
        elif goals_scored < goals_conceded:
            result = "loss"
            self.losses += 1
        else:
            self.draws += 1
        
        # Update coach's record if available
        coaches = [s for s in self.staff if isinstance(s, Coach)]
        if coaches:
            coaches[0].record_match_result(result)
        
        return {
            "opponent": opponent,
            "result": result,
            "score": f"{goals_scored}-{goals_conceded}",
            "match_number": self.matches_played
        }
    
    def get_team_stats(self):
        """
        Get the team's overall statistics.
        
        Returns:
            dict: Team statistics
        """
        return {
            "matches_played": self.matches_played,
            "wins": self.wins,
            "draws": self.draws,
            "losses": self.losses,
            "goals_scored": self.goals_scored,
            "goals_conceded": self.goals_conceded,
            "win_rate": (self.wins / self.matches_played * 100) if self.matches_played > 0 else 0,
            "points": self.wins * 3 + self.draws,
            "top_scorer": self._get_top_scorer(),
            "top_assister": self._get_top_assister(),
            "squad_size": len(self.players)
        }
    
    def _get_top_scorer(self):
        """Find the player with the most goals."""
        if not self.players:
            return None
        
        top_scorer = max(self.players, key=lambda p: p.goals)
        return {
            "name": top_scorer.full_name(),
            "goals": top_scorer.goals
        }
    
    def _get_top_assister(self):
        """Find the player with the most assists."""
        if not self.players:
            return None
        
        top_assister = max(self.players, key=lambda p: p.assists)
        return {
            "name": top_assister.full_name(),
            "assists": top_assister.assists
        }
    
    def __str__(self):
        """Return a string representation of the Team."""
        return f"{self.name} (Founded: {self.founded_year}) - {len(self.players)} players, {len(self.staff)} staff"


def create_team_roster():
    """
    Create a sample team roster with different types of players and staff.
    
    Returns:
        Team: A team object with players and staff
    """
    # Create a team
    team = Team("FC Python United", 2023)
    
    # Add a coach
    coach = Coach("Jürgen", "Klopp", 55, "German", 20, "Gegenpressing")
    team.add_staff(coach)
    
    # Add a goalkeeper
    goalkeeper = Goalkeeper("Alisson", "Becker", 29, "Brazilian", 1)
    team.add_player(goalkeeper)
    
    # Add field players - Defenders
    team.add_player(FieldPlayer("Virgil", "van Dijk", 31, "Dutch", "Defender", 4))
    team.add_player(FieldPlayer("Trent", "Alexander-Arnold", 24, "English", "Defender", 66))
    team.add_player(FieldPlayer("Andrew", "Robertson", 28, "Scottish", "Defender", 26))
    team.add_player(FieldPlayer("Joel", "Matip", 30, "Cameroonian", "Defender", 32))
    
    # Add field players - Midfielders
    team.add_player(FieldPlayer("Kevin", "De Bruyne", 31, "Belgian", "Midfielder", 17))
    team.add_player(FieldPlayer("N'Golo", "Kanté", 31, "French", "Midfielder", 7))
    team.add_player(FieldPlayer("Bruno", "Fernandes", 28, "Portuguese", "Midfielder", 8))
    team.add_player(FieldPlayer("Luka", "Modric", 37, "Croatian", "Midfielder", 10))
    
    # Add field players - Forwards
    team.add_player(FieldPlayer("Harry", "Kane", 29, "English", "Forward", 9))
    team.add_player(FieldPlayer("Mohamed", "Salah", 30, "Egyptian", "Forward", 11))
    team.add_player(FieldPlayer("Kylian", "Mbappé", 24, "French", "Forward", 7))
    
    # Add other staff
    team.add_staff(StaffMember("Carlo", "Pintus", 60, "Italian", "Fitness Coach", 25))
    team.add_staff(StaffMember("John", "Achterberg", 51, "Dutch", "Goalkeeper Coach", 15))
    
    return team


if __name__ == "__main__":
    # Create a team with players and staff
    team = create_team_roster()
    print(f"Created team: {team}")
    
    # Display the team roster by position
    roster = team.get_roster()
    print("\nTeam Roster by Position:")
    for position, players in roster["players_by_position"].items():
        print(f"\n{position}s ({len(players)}):")
        for player in players:
            print(f"  - {player}")
    
    print("\nStaff by Role:")
    for role, staff_members in roster["staff_by_role"].items():
        print(f"\n{role}s ({len(staff_members)}):")
        for staff in staff_members:
            print(f"  - {staff}")
    
    # Display a starting lineup
    formation = "4-3-3"
    starters = team.get_starters(formation)
    print(f"\nStarting XI ({formation}):")
    for player in starters:
        print(f"  - {player}")
    
    # Simulate some matches
    print("\nSimulating Season:")
    matches = [
        {"opponent": "FC Barcelona", "goals_for": 3, "goals_against": 1},
        {"opponent": "Bayern Munich", "goals_for": 2, "goals_against": 2},
        {"opponent": "Liverpool FC", "goals_for": 0, "goals_against": 2},
        {"opponent": "Real Madrid", "goals_for": 4, "goals_against": 0},
        {"opponent": "Manchester City", "goals_for": 2, "goals_against": 1}
    ]
    
    for match in matches:
        result = team.record_match(match["opponent"], match["goals_for"], match["goals_against"])
        print(f"  Match {result['match_number']}: {team.name} {result['score']} {result['opponent']} - {result['result'].upper()}")
        
        # Simulate player actions in the match
        for player in team.players:
            # Only update stats for starters
            if player in starters:
                # All players play a match
                player.play_match(90)
                
                # Goalkeepers make saves and might concede goals
                if isinstance(player, Goalkeeper):
                    saves = match["goals_against"] + 3  # Arbitrary saves count
                    for _ in range(saves):
                        player.make_save()
                    
                    for _ in range(match["goals_against"]):
                        player.concede_goal()
                    
                    if match["goals_against"] == 0:
                        player.record_clean_sheet()
                
                # Field players have various actions
                elif isinstance(player, FieldPlayer):
                    # All players cover some distance
                    player.cover_distance(8 + 4 * random.random())  # 8-12 km
                    
                    # Position-specific actions
                    if player.position == "Defender":
                        tackles = int(3 + 5 * random.random())  # 3-8 tackles
                        for _ in range(tackles):
                            player.make_tackle()
                    
                    passes = int(20 + 40 * random.random())  # 20-60 passes
                    for _ in range(passes):
                        player.complete_pass()
                    
                    # Simulate goals and assists
                    if player.position == "Forward" and random.random() < 0.4:
                        player.score_goal()
                    
                    if (player.position == "Midfielder" or player.position == "Forward") and random.random() < 0.3:
                        player.record_assist()
    
    # Display team stats
    stats = team.get_team_stats()
    print("\nSeason Summary:")
    print(f"  Matches: {stats['matches_played']}")
    print(f"  Record: {stats['wins']}-{stats['draws']}-{stats['losses']} (W-D-L)")
    print(f"  Points: {stats['points']} (3 pts for win, 1 pt for draw)")
    print(f"  Win Rate: {stats['win_rate']:.1f}%")
    print(f"  Goals: {stats['goals_scored']} scored, {stats['goals_conceded']} conceded")
    
    if stats['top_scorer']:
        print(f"  Top Scorer: {stats['top_scorer']['name']} ({stats['top_scorer']['goals']} goals)")
    
    if stats['top_assister']:
        print(f"  Top Assister: {stats['top_assister']['name']} ({stats['top_assister']['assists']} assists)")
    
    # Show player performance metrics
    print("\nPlayer Performance Metrics:")
    
    # Goalkeeper stats
    for player in team.players:
        if isinstance(player, Goalkeeper):
            print(f"\n{player.full_name()} (Goalkeeper):")
            print(f"  Matches: {player.matches_played}")
            print(f"  Clean Sheets: {player.clean_sheets}")
            print(f"  Saves: {player.saves}")
            print(f"  Goals Conceded: {player.goals_conceded}")
            print(f"  Save Percentage: {player.save_percentage():.1f}%")
    
    # Field player stats by position
    for position in ["Defender", "Midfielder", "Forward"]:
        position_players = [p for p in team.players if isinstance(p, FieldPlayer) and p.position == position]
        
        if position_players:
            print(f"\n{position} Stats:")
            for player in sorted(position_players, key=lambda p: p.position_rating(), reverse=True):
                print(f"\n  {player.full_name()} (#{player.jersey_number}):")
                print(f"    Matches: {player.matches_played}")
                print(f"    Goals: {player.goals}")
                print(f"    Assists: {player.assists}")
                
                if position == "Defender":
                    print(f"    Tackles: {player.tackles}")
                
                print(f"    Passes: {player.passes_completed}")
                print(f"    Distance: {player.distance_covered:.1f} km")
                print(f"    Rating: {player.position_rating():.2f}")
    
    # Coach performance
    coaches = [s for s in team.staff if isinstance(s, Coach)]
    if coaches:
        coach = coaches[0]
        print(f"\nCoach Performance - {coach.full_name()}:")
        print(f"  Formation: {coach.preferred_formation}")
        print(f"  Style: {coach.coaching_style}")
        print(f"  Win Rate: {coach.win_percentage():.1f}%")
        print(f"  Record: {coach.wins}-{coach.draws}-{coach.losses} (W-D-L)")
        print(f"  Experience: {coach.years_of_experience} years")