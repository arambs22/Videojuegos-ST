"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector

# Initial positions for food and snake; aim determines the snake's direction
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# List of possible colors for snake and food, excluding red
colors = ['blue', 'yellow', 'purple', 'orange', 'pink']

# Random color selection for snake and food, ensuring they are different
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

def change(x, y):
    """Change snake direction based on key press."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if the snake's head is within game boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food one step in a random direction within boundaries."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(directions)
    new_food_pos = food + move

    # Ensure food does not move outside the game boundaries
    if -200 < new_food_pos.x < 190 and -200 < new_food_pos.y < 190:
        food.move(move)

def move():
    """Move snake forward one segment, check collisions, and update game state."""
    head = snake[-1].copy()
    head.move(aim)

    # End the game if the snake hits the boundary or itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Add new head to the snake
    snake.append(head)

    # Check if snake has eaten the food
    if head == food:
        print('Snake:', len(snake))
        # Place new food at a random position within boundaries
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Remove last segment if food was not eaten
        snake.pop(0)

    clear()

    # Draw each segment of the snake
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Draw the food
    square(food.x, food.y, 9, food_color)
    update()

    # Move food one step in a random direction
    move_food()
    ontimer(move, 100)  # Set timer to call move() again after 100 milliseconds

# Set up the game window and controls
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
