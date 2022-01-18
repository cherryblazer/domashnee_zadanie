class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("driving")

    def stop(self):
        print("stopped")

    def turn(direction):
        print("turned", direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if (self.speed > 60):
            print("speed limit!")
        else:
            print(self.speed)


class Work(Car):
    def show_speed(self):
        if (self.speed > 40):
            print("speed limit!")
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)