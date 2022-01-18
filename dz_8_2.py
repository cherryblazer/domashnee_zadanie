from calendar import c


def type_logger(func):
    def wrap(x):
        return f"{x}: {type(func(x))}"

    return wrap


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)

print(a)