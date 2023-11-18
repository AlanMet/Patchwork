from graphics import * 

def drawPatchwork(win, coords, patterns, colours):
    for x in range(0, len(coords)):
        colour = colours[x]
        coord = coords[x]
        pattern = patterns[x]
        print(coord)
        if pattern is None:
            drawBox(win, Point(coord[0], coord[1]), Point(coord[0]+100, coord[1]+100), colour)
        elif pattern == "corner":
            drawCorner(win, coord, colour)
        else:
            drawTile(win, coord, colour)

        win.getMouse()


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

def drawTile(win, point, colour):
    objects = []
    for y in range(5):
        for x in range(5):
            middle = Point(point[0]+(x*20)+10, point[1]+(y*20)+10)
            if y%2==0:
                if x%2==0:
                    drawArrowsDown(win, middle, colour)
                else:
                    drawCircle(win, middle, 10, colour)
            else:
                if x%2==0:
                    drawCircle(win, middle, 10, colour)
                else:
                    drawArrowsRight(win, middle, colour)
    return objects

def drawArrowsRight(win, middle, colour):
    objects = []
    topLeft = Point(middle.getX()-10, middle.getY()-10)
    bottomLeft = Point(middle.getX()-10, middle.getY()+10)
    Triangle1 = Polygon(middle, topLeft, bottomLeft)
    Triangle1.setFill(colour)
    Triangle2 = Triangle1.clone()
    Triangle2.move(10, 0)
    Triangle1.draw(win)
    Triangle2.draw(win)
    objects.append(Triangle1)
    objects.append(Triangle2)
    return objects 

def drawArrowsDown(win, middle, colour):
    objects = []
    topLeft = Point(middle.getX()-10, middle.getY()-10)
    topRight = Point(middle.getX()+10, middle.getY()-10)
    Triangle1 = Polygon(middle, topLeft, topRight)
    Triangle1.setFill(colour)
    Triangle2 = Triangle1.clone()
    Triangle2.move(0, 10)
    Triangle1.draw(win)
    Triangle2.draw(win)
    objects.append(Triangle1)
    objects.append(Triangle2)
    return objects 

def drawCircle(win, point, radius, colour):
    circle = Circle(point, radius)
    circle.setFill(colour)
    circle.draw(win)
    return circle

#draws box and returns object
def drawBox(win, point1, point2, colour):
    box = Rectangle(point1, point2)
    box.setFill(colour)
    box.draw(win)
    return box

#returns all top left coords in order
def getCoord(size):
    coords = []
    for y in range(size):
        for x in range(size):
            coord = []
            coord.append(x*100)
            coord.append(y*100)
            coords.append(coord)
    return coords

#returns pattern name based on top left coord
def getPattern(size):
    patterns = []
    for y in range(size):
        for x in range(size):
            if x == y:
                patterns.append("corner")
            elif y%2==0:
                patterns.append("tile")
            else:
                patterns.append(None)
    return patterns

#returns colours for all tiles in order
def getColour(size, choices):
    colours = []
    for y in range(size):
        for x in range(size):
            if size-1>y>0 and size-1>x>0:
                colours.append(choices[2])
            elif y%2 == 0:
                if x%2==0:
                    colours.append(choices[0])
                else:
                    colours.append(choices[1])
            else:
                if x%2==0:
                    colours.append(choices[1])
                else:
                    colours.append(choices[0])
    return colours


def createWin(name, size):
    return GraphWin(name, size, size)

def isInteger(num):
    for x in num:
        if not x.isdigit():
            return False
    return True
            
def getSizeColour(sizes, colours):
    size = 0
    choices = []
    while size not in sizes:
        size = input("Please enter a patchwork size: ")
        if isInteger(size):
            size = int(size)
        else:
            print("Please enter a valid size.")
            size = 0

    for x in range(1, 4):
        colour = ""
        while colour not in colours:
            colour = input("Please enter a colour ")
            colour.lower()
            if colour not in colours:
                print("This is not a valid colour. Try again.")
            else:
                choices.append(colour)
                
                
    return size, choices

def main():
    sizes = [5, 7, 9]
    colours = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    patterns = ["tile", "corner"]
    #size, choices = getSizeColour(sizes, colours)
    #getColour(5, ["blue", "orange", "red"])
    #getPattern(5)
    win = createWin("Patchwork", 900)
    #drawTile(win, [0, 0], "red")
    drawPatchwork(win, getCoord(9), getPattern(9), getColour(9, ["blue", "orange", "red"]))
    win.getMouse()


main()