import math
import turtle

class SoccerField:
    def __init__(self, width=68, height=105, scale=5):
        self.width = width
        self.height = height
        self.scale = scale
        self.field_drawer = turtle.Turtle()
        self.field_drawer.speed(0)
        self.field_drawer.pencolor("white")
        self.field_drawer.hideturtle()
        # ...initialize screen if needed...

    def field_to_screen_coords(self, x, y):
        return (x * self.scale, y * self.scale)

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

# Remove or comment out the Simulation code unless you define/import it
# if __name__ == "__main__":
#     sim = Simulation()
#     sim.run()