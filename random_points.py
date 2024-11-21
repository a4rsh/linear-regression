import random

def populate_randomly(x, y, minimum, maximum):
    for i in range(len(x)):
        x[i] = random.randint(minimum, maximum)
        y[i] = random.randint(minimum, maximum)