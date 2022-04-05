from tkinter import *
from random import randint
from t_cell import *
from cancer_cell import *


class Field:
    def __init__(self, c, n, m, width, height, t_cell, cancer):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       walls - if True matrix should have 0's surrounded by 1's (walls)
       example
       1 1 1 1
       1 0 0 1
       1 1 1 1
       '''
        self.c = c
        self.a = []
        self.a
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.cancer = cancer
        self.t_cell = t_cell
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)
        self.a = [[randint(0, 1) for i in range(width)]
                  for j in range(height)]  # random cell generator
        self.draw()

    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j]
                + self.a[i - 1][j + 1] + self.a[i][j - 1]
                + self.a[i - 1][j + 1] + self.a[i + 1][j - 1]
                + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neib_sum == 2:
                    if (self.a[i][j] == 1):
                        b[i][j] = 2
                elif neib_sum < 1 or neib_sum > 6:
                    b[i][j] = 0
                elif neib_sum == 3:
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
        try:
            self.a = b
        except:
            print("something is wrong")

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        '''
       draw each element of matrix as
       a rectangle with white
       background and wall rectangle
       should have dark grey background
       '''
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        c = [[randint(0, 1) for i in range(self.width)]
             for j in range(self.height)]
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = self.cancer.get_color()   # cancer cells (bad ones)
                elif (self.a[i][j] == 2):
                    color = self.t_cell.get_color()    # T cells (good ones)
                else:
                    color = "brown"  # dead cells
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem,
                                        (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
t_cell = Tcell()
cancer = Cancer()
f = Field(c, 20, 20, 800, 800, t_cell, cancer)
f.print_field()
root.mainloop()
