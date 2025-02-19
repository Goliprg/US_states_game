import turtle
import pandas


screen = turtle.Screen()
screen.setup(width= 750,height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
states = pandas.read_csv("50_states.csv")
states_names = states.state
#states_names_list = states.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    user_answer = (screen.textinput(f"Guess States: {len(guessed_states)}/50","What is another state's name?")).strip().title()
    if user_answer == "Exit":
        break

    if (user_answer in states.state.values) and (user_answer not in guessed_states):
        guessed_states.append(user_answer)
        x_cor = states[states_names == user_answer].x.values[0]
        y_cor = states[states_names == user_answer].y.values[0]
        timmy.goto(x_cor, y_cor)
        timmy.write(user_answer)




if len(guessed_states) == 50:
    timmy.goto(0,0)
    timmy.write("YOU WIN!")
else:
    remaining_states = []
    states_names_list = states_names.to_list()
    for item in states_names_list:
        if item not in guessed_states:
            remaining_states.append(item)
    remaining_states = pandas.DataFrame(remaining_states)
    remaining_states.to_csv("remaining_states.csv")

