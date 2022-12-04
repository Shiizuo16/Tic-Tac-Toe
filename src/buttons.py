from src.const import *
from src.button import Button

buttons = list()
side = 64

# Play/Pause
menu = Button(side, side, menuLength - side)
menu.setButton("assets\\buttons-48px\play.png")
buttons.append(menu)