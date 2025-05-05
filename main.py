from turtle import Turtle, Screen
import random

teenage_mutant_ninja_turtle = {'leo': 'red', 'raph': 'blue', 'mickie': 'orange', 'don': 'purple'}
turtle_colors = ['red', 'blue', 'orange', 'purple']
y_positions = [-100, 0, 100, 200]
all_turtles = []

for turtle_index in range(0, 4):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-370, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

screen = Screen()
screen.screensize(500, 500)
user_bet = screen.textinput(title='Make your bet!!',
                           prompt='Which turtle do you think will win the race leo/raph/mickie/don ??').lower()

is_race_on = False
if user_bet in teenage_mutant_ninja_turtle:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winning_color = turtle.pencolor()
            winning_turtle_name = ""
            for name, color in teenage_mutant_ninja_turtle.items():
                if color == winning_color:
                    winning_turtle_name = name
                    break

            if winning_turtle_name == user_bet:
                print(f'You have won!! the {winning_turtle_name} turtle is the winner!!')
            else:
                print(f'You have lost!! the {winning_turtle_name} turtle is the winner!')
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
