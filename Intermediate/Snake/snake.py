import turtle as tl

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

# Snake Class and Functions
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.can_change_direction = True  # Lock mechanism

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = tl.Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor() # Get X coordinate of segment ahead of current segment
            new_y = self.segments[segment - 1].ycor() # Get Y coordinate of segment ahead of current segment
            self.segments[segment].goto(new_x, new_y) # Move segment into position of segment ahead
        self.head.forward(MOVE_DISTANCE)
        
        # Unlock direction change after the snake moves
        self.can_change_direction = True

    def set_direction(self, direction):
        if self.can_change_direction and self.head.setheading() != direction:
            self.head.setheading(direction)
            self.can_change_direction = False

    def up(self):
        if self.can_change_direction and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.can_change_direction = False  # Prevent immediate reversal

    def down(self):
        if self.can_change_direction and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.can_change_direction = False

    def left(self):
        if self.can_change_direction and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.can_change_direction = False

    def right(self):
        if self.can_change_direction and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.can_change_direction = False
