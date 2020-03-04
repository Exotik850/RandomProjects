from graphics import *

width = 500
height = 500

def line(x1, y1, x2, y2):
    return Line(Point(x1, y1), Point(x2, y2))

def rect(x1, y1, x2, y2):
    return Rectangle(Point(x1, y1), Point(x2, y2))

def main():
    win = GraphWin("New Window", width, height)
    win.setBackground('black')

    pt = Point(250, 250)
    pt2 = Point(150, 250)
    rect = Rectangle(Point(230, 100), Point(130, 200))
    rect.setOutline('green')
    rect.draw(win)

    win.getMouse()
    win.close()


main()