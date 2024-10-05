import math

def perimeter(a):
    return 4 * a


def area(a):
    return a ** 2


def rect(a, b):
    area = a * b
    perimeter = (a + b) * 2
    return area, perimeter


def len_circle(d):
    return math.pi * d


def cube(a):
    scope = a ** 3
    area = 6 * a ** 2
    return scope, area


def paralel_cube(a, b, c):
    scope = a * b * c
    area = 2 * (a * b + b * c + a * c)
    return scope, area


def circle_calculate(r):
    length = math.pi * 2 * r
    area = math.pi * r * r
    return length, area


def average(a, b):
    return (a + b) / 2


def average_geometric(a, b):
    return (a * b) ** 0.5


def mini_calc(a, b):
    square_a = a ** 2
    square_b = b ** 2
    return square_a + square_b, square_a - square_b, square_a * square_b, square_a / square_b


# task1
print("Square perimeter:", perimeter(4))

# task2
print("Square area:", area(4))

# task3
area, per = rect(4, 3)
print(f"Rectangle perimeter: {per}, Rectangle area: {area}")

# task4
print("Len Circle:", len_circle(4))

# task5
scope, area = cube(4)
print(f"Cube Scope: {scope}, Cube area: {area}")

# task6
scope, area = paralel_cube(4, 3, 2)
print(f"Paralel_Cube Scope: {scope}, Paralel_cube area: {area}")

# task7
length, area = circle_calculate(4)
print(f"Circle Length: {length}, Circle area: {area}")

# task8
print("Average:", average(4, 5))

# task9
print("Average Geometric:", average_geometric(8, 2))

# task10
square_sum, square_diff, square_mult, square_div = mini_calc(6, 3)
print(f"Sum: {square_sum}, Diff: {square_diff}, Multi: {square_mult}, Div: {square_div}")
