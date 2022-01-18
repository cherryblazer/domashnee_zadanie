class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Zapis otrisovki", self.title)


class Pen(Stationery):
    def __init__(self, title="Pen"):
        self.title = title


class Pencil(Stationery):
    def __init__(self, title="Pencil"):
        self.title = title


class Handle(Stationery):
    def __init__(self, title="Handle"):
        self.title = title


p = Pencil()

p.draw()