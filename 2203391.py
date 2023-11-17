from graphics import * 

def getCoord(size):
    coords = []
    for y in range(size):
        for x in range(size):
            coord = []
            coord.append(x*100)
            coord.append(y*100)
            coords.append(coord)

    return coords

def getColour(size, choices):
    colours = []
    for y in range(size):
        for x in range(size):
            if y%2==0:
                if x%2 == 0:
                    colours.append(choices[0])
                else:
                    colours.append(choices[1])
            if y%1==0:
                if x%2==0:
                    colours.append(choices[1])
                else:
                    colours.append(choices[0])
            print(x, y, colours[len(colours)-1])

    print(colours)


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
    #size, choices = getSizeColour(sizes, colours)
    getColour(5, ["blue", "orange", "red"])

    

main()