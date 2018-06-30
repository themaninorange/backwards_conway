# Conway's game of life, forward.
# After all, we need to test this.

import tkinter as tk
import time


def drawCell(e, color, cellx, celly, cellsizex = 100, cellsizey = 100):
    e.create_rectangle(cellx, celly, cellx + cellsizex,  celly + cellsizey, fill = color)
    #e.create_rectangle(cellx, cellx + cellsizex, celly, celly + cellsizey, fill = color)
    return 0

def stopProg(e):
    root.destroy()

def drawGrid(e, gapx = 100, gapy = 100, sizex =1000, sizey = 1000):
    #Verticals
    for i in range(0, sizex, gapx):
        e.create_line([(i, 0), (i,sizex)], tag = 'grid_line')

    #Horizontals
    for i in range(0, sizex, gapx):
        e.create_line([(0, i), (sizey, i)], tag = 'grid_line')

    return 0


def advanceState():
    #Nodes that were alive that die
    #Need an efficient way to couple items in a list that are only 1 off from each other.
    [[]]
    x - y  = 0, 1, -1
    return 0

def drawCanvas(canvas):
    global i
    drawGrid(canvas)
    for cell in livingCells:
        drawCell(canvas, "blue" , 100*cell[0], 100*cell[1])
    #print("${0} during drawCanvas".format(i))

def update():
    advanceState()
    drawCanvas(canvas)
    #print("${0} during update".format(i))
    root.after(1000,update)

def findNewLife():
    neighborToLife = set([*[(x-1, y-1), (x-1, y), (x-1, y+1), \
                            (x,   y-1),           (x,   y+1), \
                            (x+1, y-1), (x+1, y), (x+1, y+1)] for x, y in livingCells])
    # ^ This is broken.  I want to find all cells adjacent to living cells
    # I will use that list, once made, to check all of the dead cells to see if
    #    they come [back] to life.
        pass
    setx = set([point[0] for point in livingCells])
    sety = set([point[1] for point in livingCells])
    locationLookupx = {x: set([point for point in livingCells if abs(point[0] - x) <= 1]) for x in setx}
    locationLookupy = {y: set([point for point in livingCells if abs(point[1] - y) <= 1]) for y in sety}

    # Now we want to find the intersection.
    locationLookupFull = {(x,y): locationLookupx[x].intersection(locationLookupy[y]) for x in setx for y in sety}

    #





def main():
    update()
    #print("${0} in main".format(i))
    root.mainloop()

#Globals
i = 0
livingCells = {(0,0), (1,1), (1, 0), (0, 1)} #type: set
knownDead = set()
#cellSize =
#print("${0} after declaration".format(i))
root = tk.Tk()
button1 = tk.Button(root, text = "Taxation is Theft. click to close.")
canvas = tk.Canvas(root, width=500, height = 500, bg = 'white')

#Button seems to be broken.  "name 'root' is not defined"
button1.pack()
button1.bind('<Button-1>', stopProg)
canvas.pack()

if __name__ == "__main__":
    main()
