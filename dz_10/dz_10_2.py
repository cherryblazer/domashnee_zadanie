from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, params: int):
        self.params = params

    @abstractmethod
    def getCost(self):
        pass

    def __str__(self):
        return str(self.params)


class Coat(Clothes):

    @property
    def getCost(self):
        return self.params / 6.5 + 0.5


class Suit(Clothes):

    @property
    def getCost(self):
        return self.params * 2 + 0.2


a = Coat(52)
b = Suit(2)
print(a)
print(b.getCost)