from src.const import *
from src.button import Button

buttons = list()
side = 64

# Play/Pause
menu = Button(side, side, menuLength - side)
menu.setButton("assets\\buttons-48px\play.png")
buttons.append(menu)

# Reset
reset = Button(side, side, 0)
reset.setButton("assets\\buttons-48px\\reset.png")
buttons.append(reset)