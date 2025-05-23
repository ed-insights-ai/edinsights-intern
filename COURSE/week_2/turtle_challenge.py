import turtle
import math
import time
import random

class SoccerField:
    def __init__(self, width=68, height=105, scale=5):
        """Initialize the soccer field with the given dimensions and scale.
        Note: width and height are swapped to make the field vertical"""
        self.width = width
        self.height = height
        self.scale = scale
        
        # Create and configure the screen
        self.screen = turtle.Screen()
        self.screen.title("Soccer Field Visualization")
        screen_width = width * scale + 50  # Add some padding
        screen_height = height * scale + 50
        self.screen.setup(screen_width, screen_height)
        self.screen.tracer(0)  # Turn off animation for faster drawing
        
        # Create field drawer turtle
        self.field_drawer = turtle.Turtle()
        self.field_drawer.speed(0)  # Fastest speed
        self.field_drawer.pencolor("white")
        self.field_drawer.hideturtle()
        
        # Draw the field
        self.draw_field()
        self.screen.update()
    
    def draw_field(self):
        """Draw the complete soccer field with all markings."""
        self.screen.bgcolor("green")
        
        # Draw field elements
        self.draw_field_outline()
        self.draw_halfway_line()
        self.draw_center_circle()
        self.draw_penalty_areas()
        self.draw_goal_areas()
        self.draw_corner_arcs()
        self.draw_goals()
        
    def draw_field_outline(self):
        """Draw the outline of the field."""
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-self.width/2, -self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        
        for _ in range(2):
            self.field_drawer.forward(self.width * self.scale)
            self.field_drawer.left(90)
            self.field_drawer.forward(self.height * self.scale)
            self.field_drawer.left(90)
    
    def draw_halfway_line(self):
        """Draw the halfway line across the field."""
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-self.width/2, 0)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(self.width * self.scale)
    
    def draw_center_circle(self):
        """Draw the center circle."""
        # Center circle with correct orientation
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(0, 0)
        self.field_drawer.goto(x, y - 9.15 * self.scale)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.circle(9.15 * self.scale)
        
        # Draw center spot
        self.field_drawer.penup()
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.dot(5)
    
    def draw_penalty_areas(self):
        """Draw both penalty areas."""
        # Bottom penalty area
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-16.5, -self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(33 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(16.5 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(33 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(16.5 * self.scale)
        
        # Top penalty area
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-16.5, self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(33 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(16.5 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(33 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(16.5 * self.scale)
        
        # Penalty spots
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(0, -self.height/2 + 11)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.dot(5)
        
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(0, self.height/2 - 11)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.dot(5)
        
        # Draw shorter penalty arcs - both top and bottom using same technique
        arc_radius = 9.15  # radius in meters
        arc_angle = 120  # reduced from 180 to make arcs shorter (less than semi-circle)
        
        # Draw top penalty arc
        penalty_spot_x, penalty_spot_y = 0, self.height/2 - 11
        
        # Calculate start angle to center the arc
        start_angle = 180 - (arc_angle / 2)
        
        # Start at the beginning of the arc
        start_x = penalty_spot_x + arc_radius * math.cos(math.radians(start_angle))
        start_y = penalty_spot_y + arc_radius * math.sin(math.radians(start_angle))
        
        screen_x, screen_y = self.field_to_screen_coords(start_x, start_y)
        self.field_drawer.penup()
        self.field_drawer.goto(screen_x, screen_y)
        self.field_drawer.pendown()
        
        # Draw the arc segment by segment
        segments = 30  # Number of segments
        angle_increment = arc_angle / segments
        center_x, center_y = self.field_to_screen_coords(penalty_spot_x, penalty_spot_y)
        radius = arc_radius * self.scale
        
        for i in range(segments + 1):
            angle = math.radians(start_angle + i * angle_increment)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.field_drawer.goto(x, y)
        
        # Draw bottom penalty arc
        penalty_spot_x, penalty_spot_y = 0, -self.height/2 + 11
        
        # For bottom arc, we need to flip the angles (adjusting for coordinate system)
        start_angle = 360 - (arc_angle / 2)
        
        start_x = penalty_spot_x + arc_radius * math.cos(math.radians(start_angle))
        start_y = penalty_spot_y + arc_radius * math.sin(math.radians(start_angle))
        
        screen_x, screen_y = self.field_to_screen_coords(start_x, start_y)
        self.field_drawer.penup()
        self.field_drawer.goto(screen_x, screen_y)
        self.field_drawer.pendown()
        
        center_x, center_y = self.field_to_screen_coords(penalty_spot_x, penalty_spot_y)
        
        # Draw the bottom arc segment by segment
        for i in range(segments + 1):
            angle = math.radians(start_angle - i * angle_increment)  # Note the - for drawing the other direction
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.field_drawer.goto(x, y)

    def draw_goal_areas(self):
        """Draw both goal areas."""
        # Bottom goal area
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-5.5, -self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(11 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(5.5 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(11 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(5.5 * self.scale)
        
        # Top goal area
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-5.5, self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(11 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(5.5 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(11 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(5.5 * self.scale)
    
    def draw_corner_arcs(self):
        """Draw the four corner arcs with correct orientation."""
        # Bottom left corner
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-self.width/2, -self.height/2)
        self.field_drawer.goto(x + 1 * self.scale, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(90)
        self.field_drawer.circle(-1 * self.scale, 90)
        
        # Bottom right corner
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(self.width/2, -self.height/2)
        self.field_drawer.goto(x - 1 * self.scale, y)
        self.field_drawer.pendown()
        self.field_drawer.setheading(180)
        self.field_drawer.circle(-1 * self.scale, 90)
        
        # Top right corner
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(self.width/2, self.height/2)
        self.field_drawer.goto(x, y - 1 * self.scale)
        self.field_drawer.pendown()
        self.field_drawer.setheading(270)
        self.field_drawer.circle(-1 * self.scale, 90)
        
        # Top left corner
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-self.width/2, self.height/2)
        self.field_drawer.goto(x, y - 1 * self.scale)
        self.field_drawer.pendown()
        self.field_drawer.setheading(0)
        self.field_drawer.circle(-1 * self.scale, 90)
    
    def draw_goals(self):
        """Draw both goals."""
        # Bottom goal
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-3.5, -self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.color("gray")
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(7 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(2 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(7 * self.scale)
        self.field_drawer.right(90)
        self.field_drawer.forward(2 * self.scale)
        self.field_drawer.color("white")
        
        # Top goal
        self.field_drawer.penup()
        x, y = self.field_to_screen_coords(-3.5, self.height/2)
        self.field_drawer.goto(x, y)
        self.field_drawer.pendown()
        self.field_drawer.color("gray")
        self.field_drawer.setheading(0)  # Point right
        self.field_drawer.forward(7 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(2 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(7 * self.scale)
        self.field_drawer.left(90)
        self.field_drawer.forward(2 * self.scale)
        self.field_drawer.color("white")
    
    def field_to_screen_coords(self, x, y):
        """Convert field coordinates (origin at center) to screen coordinates."""
        return (x * self.scale, y * self.scale)
    
    def get_screen(self):
        """Return the screen object for external use."""
        return self.screen


class Player:
    def __init__(self, field, name, number, position, x=0, y=0, color="red"):
        """Initialize a player with given attributes."""
        self.field = field
        self.name = name
        self.number = number
        self.position = position
        self.x = x
        self.y = y
        self.color = color
        
        # Create player turtle
        self.player_turtle = turtle.Turtle()
        self.player_turtle.shape("circle")
        self.player_turtle.color(color)
        self.player_turtle.speed(0)
        self.player_turtle.penup()
        
        # Enable drag and drop
        self.player_turtle.ondrag(self.drag)
        
        # Move to initial position
        self.move_to(x, y)
        
        # Write player number
        self.player_turtle.write(str(number), align="center", font=("Arial", 8, "bold"))
    
    def move_to(self, x, y):
        """Move player to specific coordinates."""
        self.x = x
        self.y = y
        screen_x, screen_y = self.field.field_to_screen_coords(x, y)
        self.player_turtle.goto(screen_x, screen_y)
    
    def move_by(self, dx, dy):
        """Move player by a relative amount."""
        self.move_to(self.x + dx, self.y + dy)
    
    def run_to(self, x, y, speed=1):
        """Run to a position over time (animation)."""
        start_x, start_y = self.x, self.y
        target_x, target_y = x, y
        
        # Calculate distance
        distance = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
        
        # Determine steps based on distance and speed
        steps = int(distance * 2 / speed)
        steps = max(steps, 1)  # Ensure at least one step
        
        for i in range(steps + 1):
            # Linear interpolation
            t = i / steps
            new_x = start_x + t * (target_x - start_x)
            new_y = start_y + t * (target_y - start_y)
            
            self.move_to(new_x, new_y)
            self.field.screen.update()
            time.sleep(0.01)  # Small delay for animation
    
    def show_info(self):
        """Display player information."""
        info = f"{self.name} (#{self.number})\n{self.position}"
        self.player_turtle.write(info, align="left", font=("Arial", 8, "normal"))
    
    def highlight(self, highlight=True):
        """Highlight the player."""
        if highlight:
            self.player_turtle.pensize(3)
            self.player_turtle.pencolor("yellow")
            self.show_info()
        else:
            self.player_turtle.pensize(1)
            self.player_turtle.pencolor("black")
    
    def drag(self, x, y):
        """Handle dragging the player with the mouse."""
        # Convert screen coordinates to field coordinates
        field_x = x / self.field.scale
        field_y = y / self.field.scale
        self.move_to(field_x, field_y)


class Formation:
    def __init__(self, field, formation_name="4-4-2", team_color="red"):
        """Initialize a formation with the specified parameters."""
        self.field = field
        self.formation_name = formation_name
        self.team_color = team_color
        self.players = []
        
        self.setup_formation()
    
    def setup_formation(self):
        """Create players in the formation."""
        # Clear existing players
        self.players = []
        
        # Basic player information (to be reused for different formations)
        positions = {
            "GK": "Goalkeeper",
            "LB": "Left Back",
            "CB": "Center Back",
            "RB": "Right Back",
            "LWB": "Left Wing Back",
            "RWB": "Right Wing Back",  # Added proper definition for RWB
            "DM": "Defensive Midfielder",
            "CM": "Central Midfielder",
            "RM": "Right Midfielder",
            "LM": "Left Midfielder",
            "AM": "Attacking Midfielder",
            "LW": "Left Winger",
            "RW": "Right Winger",
            "CF": "Center Forward",
            "ST": "Striker"
        }
        
        # Sample player names
        names = ["Smith", "Jones", "Garcia", "Kim", "Müller", "Silva", "Okafor", 
                "Nakamura", "Patel", "Ivanov", "Martinez"]
        
        # Create custom formations - adapted for vertical field
        if self.formation_name == "4-4-2":
            # Goalkeeper
            self.players.append(Player(self.field, random.choice(names), 1, positions["GK"], 0, -40, self.team_color))
            
            # Defenders
            self.players.append(Player(self.field, random.choice(names), 2, positions["LB"], -20, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 4, positions["CB"], -7, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 5, positions["CB"], 7, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 3, positions["RB"], 20, -30, self.team_color))
            
            # Midfielders
            self.players.append(Player(self.field, random.choice(names), 7, positions["LM"], -20, -10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 6, positions["CM"], -7, -10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 8, positions["CM"], 7, -10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 11, positions["RM"], 20, -10, self.team_color))
            
            # Forwards
            self.players.append(Player(self.field, random.choice(names), 9, positions["ST"], -7, 10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 10, positions["ST"], 7, 10, self.team_color))
            
        elif self.formation_name == "4-3-3":
            # Goalkeeper
            self.players.append(Player(self.field, random.choice(names), 1, positions["GK"], 0, -40, self.team_color))
            
            # Defenders
            self.players.append(Player(self.field, random.choice(names), 2, positions["LB"], -20, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 4, positions["CB"], -7, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 5, positions["CB"], 7, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 3, positions["RB"], 20, -30, self.team_color))
            
            # Midfielders
            self.players.append(Player(self.field, random.choice(names), 6, positions["DM"], 0, -20, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 8, positions["CM"], -12, -10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 10, positions["CM"], 12, -10, self.team_color))
            
            # Forwards
            self.players.append(Player(self.field, random.choice(names), 7, positions["LW"], -20, 10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 9, positions["CF"], 0, 10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 11, positions["RW"], 20, 10, self.team_color))
            
        elif self.formation_name == "3-5-2":
            # Goalkeeper
            self.players.append(Player(self.field, random.choice(names), 1, positions["GK"], 0, -40, self.team_color))
            
            # Defenders (3)
            self.players.append(Player(self.field, random.choice(names), 2, positions["CB"], -15, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 5, positions["CB"], 0, -30, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 6, positions["CB"], 15, -30, self.team_color))
            
            # Midfielders (5)
            self.players.append(Player(self.field, random.choice(names), 3, positions["LWB"], -25, -15, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 4, positions["DM"], -10, -20, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 8, positions["CM"], 0, -10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 10, positions["CM"], 10, -20, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 7, positions["RWB"], 25, -15, self.team_color))
            
            # Forwards (2)
            self.players.append(Player(self.field, random.choice(names), 9, positions["ST"], -7, 10, self.team_color))
            self.players.append(Player(self.field, random.choice(names), 11, positions["ST"], 7, 10, self.team_color))
    
    def shift_formation(self, dx, dy):
        """Move entire formation by an offset."""
        for player in self.players:
            player.move_by(dx, dy)
    
    def rotate_formation(self, angle_degrees):
        """Rotate formation around its center."""
        # Calculate formation center
        x_sum = sum(player.x for player in self.players)
        y_sum = sum(player.y for player in self.players)
        center_x = x_sum / len(self.players)
        center_y = y_sum / len(self.players)
        
        # Convert angle to radians
        angle_rad = math.radians(angle_degrees)
        
        # Apply rotation to each player
        for player in self.players:
            # Calculate position relative to center
            rel_x = player.x - center_x
            rel_y = player.y - center_y
            
            # Apply rotation
            new_x = rel_x * math.cos(angle_rad) - rel_y * math.sin(angle_rad)
            new_y = rel_x * math.sin(angle_rad) + rel_y * math.cos(angle_rad)
            
            # Move player to rotated position
            player.move_to(center_x + new_x, center_y + new_y)
    
    def change_formation(self, new_formation_name):
        """Switch to a different formation."""
        self.formation_name = new_formation_name
        
        # Clear and rebuild formation
        for player in self.players:
            player.player_turtle.hideturtle()
            player.player_turtle.clear()
        
        self.setup_formation()


class Ball:
    def __init__(self, field, x=0, y=0):
        """Initialize a ball with given position."""
        self.field = field
        self.x = x
        self.y = y
        
        # Create ball turtle
        self.ball_turtle = turtle.Turtle()
        self.ball_turtle.shape("circle")
        self.ball_turtle.shapesize(0.5, 0.5)  # Half the default size
        self.ball_turtle.color("white", "white")
        self.ball_turtle.speed(0)
        self.ball_turtle.penup()
        
        # Move to initial position
        self.move_to(x, y)
    
    def move_to(self, x, y):
        """Move ball to specific coordinates."""
        self.x = x
        self.y = y
        screen_x, screen_y = self.field.field_to_screen_coords(x, y)
        self.ball_turtle.goto(screen_x, screen_y)
    
    def move_by(self, dx, dy):
        """Move ball by a relative amount."""
        self.move_to(self.x + dx, self.y + dy)
    
    def animate_pass(self, from_player, to_player, speed=3):
        """Animate ball passing from one player to another."""
        # Start from the first player's position
        self.move_to(from_player.x, from_player.y)
        
        # Calculate midpoint with some arc
        mid_x = (from_player.x + to_player.x) / 2
        mid_y = (from_player.y + to_player.y) / 2
        
        # Add some height to the midpoint to create an arc
        dist = math.sqrt((to_player.x - from_player.x)**2 + (to_player.y - from_player.y)**2)
        mid_x += dist / 10  # Add a slight horizontal component for diagonal passes
        
        # Perform the animated pass with a Bezier curve
        steps = int(dist * 2 / speed)
        steps = max(steps, 10)  # Ensure at least 10 steps for short passes
        
        for i in range(steps + 1):
            t = i / steps
            # Quadratic Bezier curve
            x = (1-t)**2 * from_player.x + 2*(1-t)*t * mid_x + t**2 * to_player.x
            y = (1-t)**2 * from_player.y + 2*(1-t)*t * mid_y + t**2 * to_player.y
            
            self.move_to(x, y)
            self.field.screen.update()
            time.sleep(0.01)  # Small delay for animation


class Simulation:
    def __init__(self):
        """Initialize the simulation with field, teams, and ball."""
        self.field = SoccerField()
        
        # Create home and away formations
        self.home_formation = Formation(self.field, "4-3-3", "red")
        self.away_formation = Formation(self.field, "4-4-2", "blue")
        
        # Move away team up the field
        self.away_formation.shift_formation(0, 30)
        
        # Create ball
        self.ball = Ball(self.field)
        
        # Setup controls
        self.setup_controls()
        
        # Help text
        help_turtle = turtle.Turtle()
        help_turtle.hideturtle()
        help_turtle.penup()
        help_turtle.goto(-self.field.width * self.field.scale / 2 + 10, self.field.height * self.field.scale / 2 - 20)
        help_text = (
            "Controls:\n"
            "Arrow keys: Move home team\n"
            "A/D: Rotate home team\n"
            "W/S: Change home formation\n"
            "1: Run attacking play\n"
            "Drag players with mouse"
        )
        help_turtle.write(help_text, font=("Arial", 8, "normal"))
    
    def setup_controls(self):
        """Set up keyboard and mouse controls."""
        screen = self.field.get_screen()
        
        # Keyboard controls
        screen.onkeypress(self.rotate_home_clockwise, "d")
        screen.onkeypress(self.rotate_home_counterclockwise, "a")
        screen.onkeypress(self.shift_home_up, "Up")
        screen.onkeypress(self.shift_home_down, "Down")
        screen.onkeypress(self.shift_home_left, "Left")
        screen.onkeypress(self.shift_home_right, "Right")
        screen.onkeypress(self.next_formation, "w")
        screen.onkeypress(self.prev_formation, "s")
        screen.onkeypress(self.run_attacking_play, "1")
        
        screen.listen()
    
    def rotate_home_clockwise(self):
        """Rotate home formation clockwise."""
        self.home_formation.rotate_formation(15)
        self.field.screen.update()
    
    def rotate_home_counterclockwise(self):
        """Rotate home formation counterclockwise."""
        self.home_formation.rotate_formation(-15)
        self.field.screen.update()
    
    def shift_home_up(self):
        """Shift home formation up."""
        self.home_formation.shift_formation(0, 5)
        self.field.screen.update()
    
    def shift_home_down(self):
        """Shift home formation down."""
        self.home_formation.shift_formation(0, -5)
        self.field.screen.update()
    
    def shift_home_left(self):
        """Shift home formation left."""
        self.home_formation.shift_formation(-5, 0)
        self.field.screen.update()
    
    def shift_home_right(self):
        """Shift home formation right."""
        self.home_formation.shift_formation(5, 0)
        self.field.screen.update()
    
    def next_formation(self):
        """Change to next formation."""
        formations = ["4-4-2", "4-3-3", "3-5-2"]
        current_idx = formations.index(self.home_formation.formation_name)
        next_idx = (current_idx + 1) % len(formations)
        self.home_formation.change_formation(formations[next_idx])
        self.field.screen.update()
    
    def prev_formation(self):
        """Change to previous formation."""
        formations = ["4-4-2", "4-3-3", "3-5-2"]
        current_idx = formations.index(self.home_formation.formation_name)
        prev_idx = (current_idx - 1) % len(formations)
        self.home_formation.change_formation(formations[prev_idx])
        self.field.screen.update()
    
    def run_attacking_play(self):
        """Run a preset attacking play animation."""
        # Modified for vertical field - attacking upfield
        midfielder = self.home_formation.players[6]  # Central midfielder
        winger = self.home_formation.players[8]      # Right-side player
        striker = self.home_formation.players[9]     # Striker
        
        # Highlight players involved
        midfielder.highlight(True)
        winger.highlight(True)
        striker.highlight(True)
        
        # Sequence of coordinated movements for vertical field
        midfielder.run_to(0, 0, speed=2)  # Midfielder moves up to center
        self.ball.animate_pass(midfielder, winger, speed=3)  # Pass to winger
        
        winger.run_to(15, 15, speed=2)  # Winger runs forward and wide
        self.ball.animate_pass(winger, striker, speed=3)  # Cross to striker
        
        striker.run_to(0, 30, speed=1)  # Striker runs to goal
        
        # Ball goes to goal (top of field)
        self.ball.animate_pass(striker, Ball(self.field, 0, 45), speed=4)
        
        # Remove highlights
        striker.highlight(False)
        winger.highlight(False)
        midfielder.highlight(False)
    
    def run(self):
        """Run the main simulation loop."""
        self.field.screen.mainloop()


# Run the simulation
if __name__ == "__main__":
    sim = Simulation()
    sim.run()