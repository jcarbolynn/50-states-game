import turtle
from state_names import State_Names

states = State_Names()

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



still_guessing = True
while still_guessing:
  answer_state = (screen.textinput(title = f"{states.states_guessed}/50", prompt="What's another state's name?")).title()

  # only prints state if it appears in the states list
  for state in states.states_list.state:
    if state == answer_state:
      states.goto(states.state_xcoor(state), states.state_ycoor(state))
      states.print_state(answer_state)
      states.inc_states_guessed()


  if states.states_guessed == 50:
    still_guessing = False


turtle.mainloop()
