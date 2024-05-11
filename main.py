from turtle import  Screen
import time
from scateboard import Scoreboard

from food import Food
from snake import Snake
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True

while game_is_on:

    time.sleep(0.1)
    snake.move()
    screen.update()

    if snake.segments[0].distance(food) <= 15:
        food.refresh()
        snake.extent()
        score.update_board()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment)<10:
            score.game_over()
            game_is_on = False

screen.exitonclick()