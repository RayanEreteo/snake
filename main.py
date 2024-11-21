import tkinter as tk

# Variables de jeu
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

root = tk.Tk()

root.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))
root.title("Snake")

canvas = tk.Canvas(root, width=500, height=500, bg='ivory')
canvas.pack()

root.mainloop()