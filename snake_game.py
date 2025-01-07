import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game Made by Sujan")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(2)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

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

# Show "Game Over" and "Try Again" messages
def show_message(message, x, y):
    message_turtle = turtle.Turtle()
    message_turtle.speed(0)
    message_turtle.color("yellow")
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(x, y)
    message_turtle.write(message, align="center", font=("Courier", 24, "bold"))
    return message_turtle

# Restart the game
def restart_game():
    global score, delay, segments
    score = 0
    delay = 0.1
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Clear any existing "Game Over" messages
    wn.clearscreen()
    wn.bgcolor("blue")
    main_game_loop()

# Key bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(restart_game, "space")

# Main game loop
def main_game_loop():
    global score, high_score, delay, segments
    while True:
        try:
            wn.update()

            # Check for collision with the border
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                show_message("GAME OVER", 0, 50)
                show_message("Press SPACE to Try Again", 0, -50)
                break

            # Check for collision with the food
            if head.distance(food) < 20:
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                food.goto(x, y)

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                segments.append(new_segment)

                delay -= 0.001
                score += 10
                if score > high_score:
                    high_score = score

                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Move the segments in reverse order
            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)

            # Move the first segment to where the head is
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)

            move()

            # Check for collision with the body
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    show_message("GAME OVER", 0, 50)
                    show_message("Press SPACE to Try Again", 0, -50)
                    break

            time.sleep(delay)
        except turtle.Terminator:
            break

main_game_loop()
wn.mainloop()
