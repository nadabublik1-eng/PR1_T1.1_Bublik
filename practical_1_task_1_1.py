import math

def main():
    # Зчитати три числа від користувача
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))


    # 1. Сума квадратів: a² + b² + c²
    sum_squares = a**2 + b**2 + c**2

    # 2. Середнє арифметичне
    average = (a + b + c) / 3

    # 3. Дискримінант квадратного рівняння ax² + bx + c = 0
    discriminant = b**2 - 4 * a * c

    # 4. Гіпотенуза прямокутного трикутника з катетами a, b
    hypotenuse = math.sqrt(a**2 + b**2)

    # 5. Чи утворюють a, b, c сторони трикутника (нерівність трикутника)
    is_triangle = (a + b > c) and (a + c > b) and (b + c > a)

    # Вивести всі результати з підписами за допомогою f-рядків
    print("\n--- Результати ---")
    print(f"Сума квадратів: {sum_squares:.2f}")
    print(f"Середнє арифметичне: {average:.2f}")
    print(f"Дискримінант: {discriminant:.2f}")
    print(f"Гіпотенуза: {hypotenuse:.2f}")
    print(f"Чи утворюють сторони трикутник: {is_triangle}")


if __name__ == "__main__":
    main()