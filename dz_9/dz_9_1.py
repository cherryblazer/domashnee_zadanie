class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        return f"{self.length * self.width * 25 * 5 / 1000} T"


r = Road(20, 5000)

print(r.calc())