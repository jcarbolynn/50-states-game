import pandas
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class State_Names(Turtle):
  
  def __init__(self):
    super().__init__()
    self.states_list = pandas.read_csv("50_states.csv")
    self.penup()
    self.hideturtle()
    self.xcoor = 0
    self.ycoor = 0
    self.states_guessed = 0

  def print_state(self, state):
    self.write(f"{state}", align=ALIGNMENT, font=FONT)

  #TODO: when guess state equals a state in the list set x and y coordinates
  def state_xcoor(self, state):
    self.xcoor = int(self.states_list[self.states_list.state == state].x)
    return self.xcoor
  
  def state_ycoor(self, state):
    self.ycoor = int(self.states_list[self.states_list.state == state].y)
    return self.ycoor

  def inc_states_guessed(self):
    self.states_guessed += 1
