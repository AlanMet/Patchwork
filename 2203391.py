from graphics import * 
import random

def drawPatchwork(win, coords, patterns, colours):
    objects = []
    for x in range(0, len(coords)):
        colour = colours[x]
        coord = coords[x]
        pattern = patterns[x]
        if pattern == "tile":
            objects.append(drawTile(win, coord, colour))
        elif pattern == "corner":
            objects.append(drawCorner(win, coord, colour))
        else:
            objects.append(drawBox(win, Point(coord[0], coord[1]), Point(coord[0]+100, coord[1]+100), colour))

    win.update()
    return objects

def drawOutline(win, point, colour):
    square = Rectangle(point, Point(point.getX()+100, point.getY()+100))
    square.setOutline(colour)
    square.setWidth(4)
    square.draw(win)
    return square

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
    [coords.append([x*100, y*100]) for y in range(size) for x in range(size)]
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
    return GraphWin(name, size, size, autoflush=False)

def isInteger(num):
    for x in num:
        if not x.isdigit():
            return False
    return True

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

#https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
def clear(win):
    for item in win.items[:]:
        item.undraw()

#no need to return pattern as the objects gets referenced through the function
def changePattern(point, pattern, patternName, size):
    coords = getCoord(size)
    Xpoint = point.getX()
    Ypoint = point.getY()
    for x in range(0, len(coords)):
        if coords[x][0]<=Xpoint<=coords[x][0]+99 and coords[x][1]<=Ypoint<=coords[x][1]+99:
            pattern[x] = patternName

def changeColour(point, colours, colourName, size):
    coords = getCoord(size)
    Xpoint = point.getX()
    Ypoint = point.getY()
    for x in range(0, len(coords)):
        if coords[x][0]<=Xpoint<=coords[x][0]+99 and coords[x][1]<=Ypoint<=coords[x][1]+99:
            colours[x] = colourName

def animateButton(win, button, colour):
    button[0].setFill(colour)
    win.update()
    time.sleep(0.1)
    button[0].setFill("black")
    win.update()

def selectionMode(win, slected, objects):
    pass

def randomChange(win, coordinates, pattern, colours, size):
    patterns = ["tile", "corner", None]
    colourChoices = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    clear(win)
    for _ in range(0, random.randint(0, 10)):
        point = Point(random.choice(coordinates)[0], random.choice(coordinates)[1])
        changePattern(point, pattern, random.choice(patterns), size)
        changeColour(point, colours, random.choice(colourChoices), size)
    drawPatchwork(win, coordinates, pattern, colours)

    
def getSizeColour():
    sizes = [5, 7, 9]
    colours = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
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

def getPatchIndex(mouse, size):
    coordinates = getCoord(size)
    pointX = mouse.getX()
    pointY = mouse.getY()
    for i in range(0, len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        if x<=pointX<=x+99 and y<=pointY<=y+99:
            return i


def selectionMode(win, size, patchCoords, outlines):
    coordinates = getCoord(size)
    point = Point(size*50, size*50)
    buttons = drawButtons(win, size)
    while True:
        point = win.getMouse()
        button = buttonClicked(point, buttons)
        if button is not None:
            animateButton(win, button, "grey")
            if button[1].getText() == "CLOSE":
                win.close()
            if button[1].getText() == "OK":
                [x.undraw() for x in buttons[0]]
                win.update()
                return buttons
        else:
            index = getPatchIndex(point, size)
            if coordinates[index] in patchCoords:
                for x in range(0, len(patchCoords)):
                    if patchCoords[x] == coordinates[index]:
                        del patchCoords[x]
                        outlines[x].undraw()
                        del outlines[x]
                        break
            else:
                patchCoords.append(coordinates[index])
                outlines.append(drawOutline(win, Point(patchCoords[-1][0], patchCoords[-1][1]), "black"))


def changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, colour):
    clear(win)
    for i in patchCoords:
        point = Point(i[0], i[1])
        changeColour(point, colours, colour, size)
    drawPatchwork(win, getCoord(size), pattern, colours)
    [x.draw(win) for x in outlines]
    [x.draw(win) for x in buttons[1]]
    win.update()

def changeTilepattern(win, patchCoords, colours, pattern, size, outlines, buttons, patternName):
    clear(win)
    for i in patchCoords:
        point = Point(i[0], i[1])
        changePattern(point, pattern, patternName, size)
    drawPatchwork(win, getCoord(size), pattern, colours)
    [x.draw(win) for x in outlines]
    [x.draw(win) for x in buttons[1]]
    win.update()


def editMode(win, size, pattern, colours):
    close = False
    patchCoords=[]
    outlines=[]
    buttons = selectionMode(win, size, patchCoords, outlines)
    while True:
        point = win.checkMouse()
        key = win.checkKey()
        if point is not None:
            button = buttonClicked(point, buttons)
            if button is not None:
                animateButton(win, button, "grey")
                if button[1].getText() == "CLOSE":
                    win.close()
                    return
        if key is not None:
            if key == "s":
                buttons = selectionMode(win, size, patchCoords, outlines)
            if key == "d":
                patchCoords = []
                [x.undraw() for x in outlines]
                win.update()
                #fixes issue where unselected outlines would be drawn as the object still existed in the outlines list
                outlines = []
            if key == "p":
                changeTilepattern(win, patchCoords, colours, pattern, size, outlines, buttons, "tile")
            if key == "f":
                changeTilepattern(win, patchCoords, colours, pattern, size, outlines, buttons, "corner")
            if key == "q":
                changeTilepattern(win, patchCoords, colours, pattern, size, outlines, buttons, None)
            if key == "r":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "red")
            if key == "g":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "green")
            if key == "b":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "blue")
            if key == "m":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "magenta")
            if key == "o":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "orange")
            if key == "y":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "yellow")
            if key == "c":
                changeTileColour(win, patchCoords, colours, pattern, size, outlines, buttons, "cyan")
            if key == "x":
                randomChange(win, getCoord(size), pattern, colours, size)
                [x.draw(win) for x in outlines]
                [x.draw(win) for x in buttons[1]]
def main():
    size, choices = getSizeColour()
    win = createWin("Patchwork", size*100)
    pattern = getPattern(size)
    coordinates = getCoord(size)
    colours = getColour(size, choices)
    drawPatchwork(win, coordinates, pattern, colours)
    editMode(win, size, pattern, colours)
                
main()