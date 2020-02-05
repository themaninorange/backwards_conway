#!/usr/bin/python

"""Conway's game of life, forward.  After all, we need to test this.
"""

import Tkinter as tk
import time
import collections as col

class Ecosystem:
    @staticmethod
    def cellNeighbors(c):
        return [(c[0]-1, c[1]-1), (c[0]  , c[1]-1), (c[0]+1, c[1]-1),  # Shaped like this: n n n
                (c[0]-1, c[1]  ),                   (c[0]+1, c[1]  ),  #                   n   n
                (c[0]-1, c[1]+1), (c[0]  , c[1]+1), (c[0]+1, c[1]+1)]  #                   n n n
    
    @staticmethod
    def neighbors(cells):
        return col.Counter([x for y in [Ecosystem.cellNeighbors(cell) for cell in list(cells)] for x in y])
    
    @staticmethod
    def spawn(neighborhood):
        return frozenset([key for key, value in neighborhood.items() if value == 3])
    
    @staticmethod
    def survivors(cells, neighborhood):
        return frozenset([key for key, value in neighborhood.items() if value == 2]).intersection(cells)
    
    @staticmethod
    def nextGeneration(cells):
        neighborhood = Ecosystem.neighbors(cells)
        return frozenset().union(Ecosystem.spawn(neighborhood), Ecosystem.survivors(cells, neighborhood))
    
    def __init__(self, canvas, starterPopulation = frozenset(), cellSize = 100, color = "blue"):
        self.canvas = canvas
        self.cellSize = cellSize
        self.color = "blue"
        self.livingCells = starterPopulation
        self.neighborhood = self.neighbors(livingCells)

    def draw(self):
        self.canvas.after(1, self.draw)  #(time_delay, method_to_execute)


    def drawCell(self, color, cellx, celly):
        self.canvas.create_rectangle(cellx, celly, cellx + self.cellSize,  celly + self.cellSize, fill = color)
        #e.create_rectangle(cellx, cellx + cellsizex, celly, celly + cellsizey, fill = color)
        return 0
    
    def drawGrid(self):
        #Verticals
        for i in range(0, self.canvas.winfo_width(), self.cellSize):
            self.canvas.create_line([(i, 0), (i,self.canvas.winfo_height())], tag = 'grid_line')
    
        #Horizontals
        for i in range(0, self.canvas.winfo_height(), self.cellSize):
            self.canvas.create_line([(0, i), (self.canvas.winfo_width(), i)], tag = 'grid_line')
    
        return 0
    
    def drawCanvas(self):
        self.canvas.delete('all')
        self.drawGrid()
        for cell in list(self.livingCells):
            self.drawCell("blue" , self.cellSize*cell[0], self.cellSize*cell[1])
        #print("${0} during drawCanvas".format(i))
        return 0
    
    def generate(self):
        self.livingCells = Ecosystem.nextGeneration(self.livingCells)
    
def update():
    
    esys.drawCanvas()
    esys.generate()
    
    root.after(10,update)
    
    return 0


def stopProg(e):
    root.destroy()
    return 0


def main():
    update()
    print('LIFE: ' + str(livingCells))
    #print("${0} in main".format(i))
    root.mainloop()
    
    return 0

#Globals
i = 0

#livingCells = {(1,1), (1,2), (1, 3)} #spinner
#livingCells = {(0,0), (1,1), (1, 0), (0, 1)} #box
#livingCells = frozenset({(0,2), (0,1), (1, 2), (2, 0), (2,1), (2,2)}) #lower-case r
livingCells = frozenset({(50,52), (50,51), (51, 52), (52, 50), (52,51), (52,52)}) #lower-case r

root = tk.Tk()
button1 = tk.Button(root, text = "Taxation is Theft. click to close.")
canvas = tk.Canvas(root, width=1000, height = 1000, bg = 'white')


esys = Ecosystem(canvas, livingCells, cellSize = 4)

#Button seems to be broken.  "name 'root' is not defined"
button1.pack()
button1.bind('<Button-1>', stopProg)
canvas.pack()


if __name__ == "__main__":
    main()
