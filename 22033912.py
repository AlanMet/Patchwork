from graphics import * 

#draws box and returns object
def drawBox(win, point1, point2, colour):
    box = Rectangle(point1, point2)
    box.setFill(colour)
    box.draw(win)
    return box


#draws corner patch and returns all objetcs for later use
def drawCorner(win, point, colour):
    objects = []
    y = point[1]
    bottomLeft = Point(point[0], point[1]+100)
    for x in range(10):
        topRight = Point(point[0]+100-x*10, y+x*10)
        if x%2==0:
            box = drawBox(win, bottomLeft, topRight, colour)
        else:
            box = drawBox(win, bottomLeft, topRight, "white")
        objects.append(box)
    return objects




win = GraphWin("window", 500, 500)
changeColour(drawCorner(win, [0, 0], "red"))
win.getMouse()