from turtle import Turtle,Screen
import random
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="wjich turtle will win the the race? emter the color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtuls=[ ]



for turtle_index in range(0,6):
    turtle=Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtuls.append(turtle)

if user_bet:
    is_race_on=True

    while is_race_on:
        for i in all_turtuls:
            if i.xcor() > 230:
                is_race_on = False
                winer_turtle=i.pencolor()
                if winer_turtle == user_bet:
                    print(f'you right {winer_turtle} is win')
                
                else:
                    print(f"you lose:{winer_turtle} is win")

            i.forward(random.randint(1,50))
screen.exitonclick()