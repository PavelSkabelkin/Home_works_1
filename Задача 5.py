
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
m = float(input("Введите начало отрезка m: "))
n = float(input("Введите конец отрезка n: "))


if a == 0:
    print("Уравнение не является линейным.")
else:

    x = -b / a
    
    if m <= x <= n:
        print(f"Решение уравнения попадает в отрезок [{m}, {n}].")
    else:
        print(f"Решение уравнения не попадает в отрезок [{m}, {n}].")