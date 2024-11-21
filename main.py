import numpy as np
import line_functions as lf
import random_points as rp
import matplotlib.pyplot as plt

minimum = 1
maximum = 10
points = 10

x = [0] * points
y = [0] * points

rp.populate_randomly(x, y, minimum, maximum)

a = 0
b = 0
angle = 0

while angle != -1:
    angle = lf.findAngle(a, b, x, y, 10 ** -5, 10 ** 3)
    distance = lf.findDistance(a, b, x, y, angle, 0,10 ** 3)
    a, b = lf.travel(a, b, distance, angle)
    print("a: " + str(a) + " b: " + str(b))

line_x = np.linspace(minimum, maximum, (maximum - minimum) * 2)
line_y = line_x.copy()
lf.apply_regression(a, b, line_y)

plt.scatter(x, y)
plt.plot(line_x, line_y)
plt.title("Linear Regression")

plt.show()