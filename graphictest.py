from tkinter import *
import math
import time

width = 500
height = 500
angle = 0
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
tk.title("Test")
canvas.pack()

class circle():
    def __init__(self, center, radius, color):
        self.radius = radius
        self.shape = canvas.create_oval(center[0] - self.radius / 2, center[1] - self.radius / 2, center[0] + self.radius / 2, center[1] + self.radius / 2, fill = color)
        self.coords = canvas.coords(self.shape)
    

ball = circle((width / 2, height / 2), 100, "red")


for i in range(100):
    ball.coords = [ball.coords[0] - 10, ball.coords[1] - 10, ball.coords[2] - 10, ball.coords[3] - 10]
    tk.update()
    time.sleep(0.01)

tk.mainloop()
