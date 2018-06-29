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
    global i
    if i == 0:
        i = 1
    else:
        i = 0

def drawCanvas(canvas):
    global i
    drawGrid(canvas)
    drawCell(canvas, "white" if i == 1 else "blue" , 200, 200)
    print("${0} during drawCanvas".format(i))

def update():
    advanceState()
    drawCanvas(canvas)
    print("${0} during update".format(i))
    root.after(1000,update)

def main():
    update()
    print("${0} in main".format(i))
    root.mainloop()

#Globals
i = 0
print("${0} after declaration".format(i))
root = tk.Tk()
button1 = tk.Button(root, text = "Taxation is Theft. click to close.")
canvas = tk.Canvas(root, width=500, height = 500, bg = 'white')

#Button seems to be broken.  "name 'root' is not defined"
button1.pack()
button1.bind('<Button-1>', stopProg)
canvas.pack()

if __name__ == "__main__":
    main()
