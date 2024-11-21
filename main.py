import tkinter as tk
import random

# Game configurations
GAME_WIDTH = 600
GAME_HEIGHT = 400
SQUARE_SIZE = 20
GAME_SPEED = 100
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

root = tk.Tk()
root.title("Snake")
root.geometry("{}x{}".format(GAME_WIDTH, GAME_HEIGHT))
root.resizable(width=False, height=False)

root.mainloop()