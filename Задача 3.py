import math

x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))
z = int(input("Введите значение Z: "))

# Вычисляем остаток от деления z на y с помощью оператора %
z_mod_y = z % y

# Вычисляем значение F
f = float(((x ** 5 + 7) / abs(-6) * y) / (7 - z_mod_y) ** (1 / 3))

# Выводим результат с округлением до 3 знаков после запятой
print(f"Значение F равно {round(f, 3)}")
