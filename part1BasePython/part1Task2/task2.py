def from_cm_to_m(cm):
    return cm // 100


def from_kg_to_tonn(kg):
    return kg // 1000


def from_b_to_kb(b):
    return b // 1024


def b_in_a(a, b):
    return a // b


def remain_a(a, b):
    return a % b


def print_double_digit(n):
    return n // 10, n % 10


def count_double_digit(n):
    digits = n // 10
    units = n % 10
    return digits + units, digits * units


def swap_double_digit(n):
    digits = n // 10
    units = n % 10
    return units, digits


def first_triple_digit(n):
    return n // 100


def change_triple_digit(n):
    units = n % 10
    digits = n // 10 % 10
    return units, digits


# task1
print("Metres: ", from_cm_to_m(154))

# task2
print("Tonn: ", from_kg_to_tonn(2453))

# task3
print("KB: ", from_b_to_kb(1234))

# task4
print(f"B in A occurs {b_in_a(12, 2)} times")

# task5
print("In A remains: ", remain_a(14, 3))

# task6
digits, units = print_double_digit(24)
print(f"In number {digits} dozens and {units} units")

# task7
summary, multi = count_double_digit(24)
print(f"SUM: {summary}, MULTI: {multi}")

# task8
digits, units = swap_double_digit(24)
print(f"Swapped number: {digits}{units}")

# task9
print("First numeral: ", first_triple_digit(123))

# task10
units, digits = change_triple_digit(531)
print(f"Units: {units}, Dozens: {digits}")
