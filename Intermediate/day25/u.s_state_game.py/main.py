import turtle

import pandas

screen = turtle.Screen()
screen.title('U.S State Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 States Correct',
        prompt="What's another state's name?",
    )
    if answer_state == 'Exit':
        missing_states = [
            state for state in all_state if state not in guessed_states
        ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    # If answer_state is one of the states in all the states of the 50_states_csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# State_to_learn.csv
