class Cell:
    def __init__(self, c):
        self.c = c
        self.ch = '*'

    def __str__(self):
        return str(f'Number of cells: {self.c}')

    def __sub__(self, cell2):
        return Cell(abs(self.c - cell2.c))

    def __mul__(self, cell2):
        return Cell(self.c * cell2.c)

    def __truediv__(self, cell2):
        return Cell(self.c // cell2.c)

    def __add__(self, cell2):
        return Cell(abs(self.c + cell2.c))

    def make_order(self, count):
        x = self.c
        while x > 0:
            for k in range(1,count+1):
                print(self.ch, end ='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')



a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)