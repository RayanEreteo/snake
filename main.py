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
direction = "Right"
snake_pos = [(200, 200), (190, 200), (180, 200)]

root = tk.Tk()
root.title("Snake")
root.geometry("{}x{}".format(GAME_WIDTH, GAME_HEIGHT))
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, background=BACKGROUND_COLOR)
canvas.pack()

for x,y in snake_pos:
    snake = canvas.create_rectangle(x,y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill="blue")

def move_snake():
    print("Move")

def update():
    move_snake()
    root.after(GAME_SPEED, update)

root.after(GAME_SPEED, update)

root.mainloop()