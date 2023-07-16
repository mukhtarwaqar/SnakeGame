# Simple snake game

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game by Waqar")
window.bgcolor("dark green")
window.setup(width=600, height=600)
window.tracer(0)  # turns off sreen updates

# Create snake head
head = turtle.Turtle()  # creates turtle

# snake head turtle properties
head.speed(0) # animation speed of turtle  0 is fastes/no slowdown
head.shape("square")
head.color("light green")
head.penup()  # tutles were created to draw lines. this ensures no drawinf
head.goto(0, 0)  # turtle default starts in middle but good idea to intial ourslf
head.direction = "stop"  # on game startup, snake does not move

# New turtle for apple
apple = turtle.Turtle()
apple.speed(0) # animation speed of turtle  0 is fastes/no slowdown
apple.shape("circle")
apple.color("red")
apple.penup()  # tutles were created to draw lines. this ensures no drawinf


# function for apple postion
def apple_pos():
    x = random.randint(-290, 290)
    y = random.randint(-290, 200)
    apple.goto(x, y)


apple_pos()


# Code for the body growing
body_segments = []

# Code to write score on the screen. turtle has function called write to do that
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()  # dont wanna draw lines
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score:0", align="center", font=("Courier", 24, "normal"))



# Functions
# if up is called will move up 20
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# functions to chnage direction
def go_up():
    if head.direction != "down":  # prevent the snake going in the direction its body came from
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def pause_game():
    head.direction = "stop"


# keyboard binding: combines a key press with a certain function
window.listen()  # look for a keyboard press
window.onkeypress(go_up, "Up")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")
window.onkeypress(go_down, "Down")
# window.onkeypress(pause_game, "space")


# Main game loop
while True:
    # since we had screen update turned off, we need to turn it on to see the "snake"
    window.update()

    # check for collosion with border
    if head.xcor() > 295 or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -295:
        time.sleep(1)  # pauses the game
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments after collison/reset body length
        for segment in body_segments:
            segment.hideturtle()
        body_segments.clear()  # same as body_segment = []

        # reset score on border collision
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # reset the speed
        delay = 0.1
    # we know that both the apple and head is 20 so if the distance btween the two is less than 20
    # the two must be touching
    # Check for collision with food
    if head.distance(apple) < 20:
        # Move the apple to random spot after touch
        apple_pos()

        # add a segment if collision occures
        new_segment = turtle.Turtle()
        new_segment.speed(0)  # again this is animation speed
        new_segment.shape("square")
        new_segment.color("dark blue")
        new_segment.penup()
        body_segments.append(new_segment)

        # Shorten delay since as you add more turtles the game will run slower
        delay -= 0.001
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # make sure the new segments move with the head
    # move the end segments first
    # if on segment 10 you wann get the turtle segment to move where
    # segment 9 is so on all th way down to before the second to last index
    for index in range(len(body_segments)-1, 0, -1):
        x = body_segments[index - 1].xcor()  # move to x coordinate of the segment in front of it
        y = body_segments[index - 1].ycor()  # move to y coordinate of the segment in front of it
        body_segments[index].goto(x, y)

    # move segment 0 to where head is
    # cant do this in the previous for loop since head is a separate turtle not in the list of body segemnts
    if len(body_segments) > 0:  # checks if there is any additional body segments
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    move()  # intially snake moved of screen too quickly

    # check for collison with self
    for segment in body_segments:
        if segment.distance(head) < 20:
            time.sleep(1)  # delay
            head.goto(0, 0)  # reset position
            head.direction = "stop"  # stop movement
            # Hide the segments after collision/reset body length/score
            for seg in body_segments:
                seg.hideturtle()
            body_segments.clear()  # same as body_segment = []
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # reset turtle speed
            delay = 0.1
    time.sleep(delay)  # thus we need a delay

# keep the window open
window.mainloop()
