from graphics import * 

def drawPatchwork(win, coords, patterns, colours):
    objects = []
    for x in range(0, len(coords)):
        colour = colours[x]
        coord = coords[x]
        pattern = patterns[x]
        if pattern is None:
            objects.append(drawBox(win, Point(coord[0], coord[1]), Point(coord[0]+100, coord[1]+100), colour))
        elif pattern == "corner":
            objects.append(drawCorner(win, coord, colour))
        else:
            objects.append(drawTile(win, coord, colour))

    return objects

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
                    objects.append(drawArrows(win, middle, colour, "down"))
                else:
                    objects.append(drawCircle(win, middle, 10, colour))
            else:
                if x%2==0:
                    objects.append(drawCircle(win, middle, 10, colour))
                else:
                    objects.append(drawArrows(win, middle, colour, "right"))
    return objects

def drawArrows(win, middle, colour, direction):
    objects = []
    topLeft = Point(middle.getX()-10, middle.getY()-10)
    if direction == "down":
        point2 = Point(middle.getX()+10, middle.getY()-10)
    if direction == "right":
        point2 = Point(middle.getX()-10, middle.getY()+10)
    Triangle1 = Polygon(middle, topLeft, point2)
    Triangle1.setFill(colour)
    Triangle2 = Triangle1.clone()
    if direction == "right":
        Triangle2.move(10, 0)
    else:
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

def drawText(win, point, text, colour):
    text = Text(point, text)
    text.setFill(colour)
    text.draw(win)
    return text

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
        size = input("Please enter a patchwork size (5 or 7 or 9): ")
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

def drawButton(win, point1, point2, text, boxcolour, Textcolour):
    objects = []
    objects.append(drawBox(win, point1, point2, boxcolour))
    objects.append(drawText(win, Point((point2.getX()+point1.getX())/2, (point2.getY()+point1.getY())/2), text, Textcolour))
    return objects

def drawButtons(win, size):
    objects = []
    objects.append(drawButton(win,  Point(0, 0), Point(30, 30), "OK", "black", "white"))
    objects.append(drawButton(win,  Point((size*100)-60, 0), Point(size*100, 30), "CLOSE", "black", "white"))
    return objects 
    

def buttonClicked(point, buttons):
    #method and float error <= 
    for button in buttons:
        p1 = button[0].getP1()
        p2 = button[0].getP2()
        if (p1.getX()<=point.getX()<=p2.getX()) and (p1.getY()<=point.getY()<=p2.getY()):
            return button
    return None

#recursive algorithm
def hideObjects(objects):
    #print(objects)
    for x in objects:
        if type(x) is list:
            hideObjects(x)
        else:
            x.undraw()

def changePattern(point, pattern, newPattern, size):
    coords = getCoord(size)
    Xpoint = point.getX()
    Ypoint = point.getY()
    for x in range(0, len(coords)):
        if coords[x][0]<=Xpoint<=coords[x][0]+99 and coords[x][1]<=Ypoint<=coords[x][1]+99:
            pattern[x] = newPattern

    return pattern

def swapPatch(win, size, point, objects):
    pass

def animateButton(button, colour):
    button[0].setFill(colour)
    time.sleep(0.1)
    button[0].setFill("black")
    
def run(win, size):
    buttons = drawButtons(win, size)
    close = False 
    while not close:
        mouse = win.getMouse()
        button = buttonClicked(mouse, buttons)
        if button is not None:
            animateButton(button, "grey")
            #button[1] is the text object
            if button[1].getText() == "CLOSE":
                close = True
            if button[1].getText() == "OK":
                hideObjects(button)

def main():
    sizes = [5, 7, 9]
    #size, choices = getSizeColour(sizes, colours)
    size = 5
    choices = ["red", "blue", "green"]
    win = createWin("Patchwork", size*100)
    pattern = getPattern(size)
    coordinates = getCoord(size)
    colours = getColour(size, choices)
    drawPatchwork(win, coordinates, pattern, colours)
    run(win, size)
    
                
main()