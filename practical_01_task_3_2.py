def calculator():
    """Інтерактивний калькулятор з підтримкою +, -, *, /, //, %, **."""
    print(" Калькулятор ")
    print("Введіть вираз у форматі: число оператор число")
    print("Введіть 'quit' для виходу, 'history' для історії")

    history = []

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'history':
            if not history:
                print("Історія порожня")
            else:
                for item in history:
                    print(item)
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Помилка: неправильний формат. Потрібно 'число оператор число'")
            continue

        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("Помилка: операнди мають бути числами")
            continue

        if operator not in ('+', '-', '*', '/', '//', '%', '**'):
            print("Помилка: невідомий оператор")
            continue

        if operator in ('/', '//', '%') and num2 == 0:
            print("Помилка: ділення на нуль!")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '//':
            result = num1 // num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2

        calc_str = f"{num1} {operator} {num2} = {result}"
        print(result)
        history.append(calc_str)

if __name__ == "__main__":
    calculator()