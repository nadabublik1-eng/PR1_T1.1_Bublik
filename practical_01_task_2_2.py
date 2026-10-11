

import math

def triangle_type(a: float, b: float, c: float) -> str:
    """Визначає тип трикутника за сторонами."""
    if not (a + b > c and a + c > b and b + c > a):
        return 'не є трикутником'

    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]

    if a == b == c:
        return 'рівносторонній'
    elif a == b or b == c or a == c:
        if abs(x**2 + y**2 - z**2) < 1e-9:
            return 'рівнобедрений прямокутний'
        return 'рівнобедрений'
    else:
        if abs(x**2 + y**2 - z**2) < 1e-9:
            return 'прямокутний'
        return 'різносторонній'

def triangle_area(a: float, b: float, c: float) -> float:
    """Обчислює площу трикутника за формулою Герона."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    try:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Помилка: сторони мають бути додатними числами")
            return

        t_type = triangle_type(a, b, c)
        print(f"Тип: {t_type}")

        if t_type != 'не є трикутником':
            area = triangle_area(a, b, c)
            print(f"Площа: {area:.2f}")

    except ValueError:
        print("Помилка: введіть числа")

if __name__ == "__main__":
    main()