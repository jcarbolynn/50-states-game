import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

print_state = turtle.Turtle()
print_state.penup()
print_state.hideturtle()

states = pandas.read_csv("50_states.csv")

def state_xcoor(state):
  xcoor = int(states[states.state == state].x)
  return xcoor

def state_ycoor(state):
  ycoor = int(states[states.state == state].y)
  return ycoor

# # to print whole row by state name
# for state in states.state:
#   print(states[states.state == state])

still_guessing = True
states_guessed = 0
while still_guessing:
  answer_state = (screen.textinput(title = f"Guess the state {states_guessed}/50", prompt="What's another state's name?")).title()

  for state in states.state:
    if state == answer_state:
      print_state.goto(state_xcoor(state), state_ycoor(state))
      print_state.write(f"{answer_state}", align=ALIGNMENT, font=FONT)
      states_guessed += 1

  if states_guessed == 50:
    still_guessing = False

# if states[states.state == answer_state]:
#   print(answer_state)

turtle.mainloop()
############################ANGELA DID########
# # to find x and y coordinates on map image so we can use them to print names of states in correct locations
# def get_mouse_click_coor(x,y):
#   print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

# # alternative to exitonclick() to keep the screen open
# # turtle.mainloop()
##############################################
