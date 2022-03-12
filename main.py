
from turtle import Turtle,Screen
import time
from food import Food
from scoreboard import ScoreBoard


from snake import Snake 

print(Snake)
# Creacion del tablero 
screen = Screen ()
screen.setup( width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake game")
screen.tracer(0)

snake = Snake()
#creamos el objeto de comida
food = Food()

#creamos la variable tablero 
scoreboard = ScoreBoard()
#metodo de escucha de las teclas 

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")


#animacion serpiente 
game_is_on = True

#contador de puntos 
points= 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detectar colicion con comida
    if snake.head.distance(food) < 15:
        food.refrech()
        scoreboard.increase_score()
        snake.extend()
        


    # Detector de colicion de paredes 

    if snake.head.xcor()>280 or  snake.head.xcor()<-280:
        game_is_on = False 
        scoreboard.game_over()       

    if snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on = False 
        scoreboard.game_over()    

    # detector de las colidiones de segmento de la serpiente 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()