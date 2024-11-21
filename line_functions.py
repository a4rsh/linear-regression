import math

def apply_function(x, a, b):
    return a * x + b

def apply_regression(a, b, array):
    for i in range(len(array)):
        array[i] = apply_function(array[i], a, b)

def SSE(a, b, x, y):
    sse = 0
    for i in range(len(x)):
        sse += (apply_function(x[i], a, b) - y[i]) ** 2
    return sse

def travel(a, b, distance, angle):
    if angle == -1:
        return a, b
    return a + distance * math.cos(angle), b + distance * math.sin(angle)

def findAngle(a, b, x, y, distance, angles):
    min_angle = -1
    minSSE = SSE(a, b, x, y)
    for i in range(angles - 1):
        a1, b1 = travel(a, b, distance, i * 2 * math.pi / angles)
        sse = SSE(a1, b1, x, y)
        if sse < minSSE:
            minSSE = sse
            min_angle = i * 2 * math.pi / angles
    return min_angle

def findDistance(a, b, x, y, angle, startingDistance, increment):
    if angle == -1:
        return 0

    d = startingDistance

    while True:
        a1, b1 = travel(a, b, d, angle)
        v1 = SSE(a1, b1, x, y)

        a2, b2 = travel(a, b, d + increment, angle)
        v2 = SSE(a2, b2, x, y)

        a3, b3 = travel(a, b, d + 2 * increment, angle)
        v3 = SSE(a3, b3, x, y)

        if v2 > v1 or v3 > v2:
            if math.fabs(v3 - v1) < 10 ** -10:
                return d + increment
            else:
                return findDistance(a, b, x, y, angle, d, increment / 2)
        d += increment