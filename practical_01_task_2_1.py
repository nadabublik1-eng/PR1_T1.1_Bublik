def main():
    user_input = input("Введіть вашу оцінку (від 0 до 100): ")

    try:
        score = int(user_input)

        if score < 0 or score > 100:
            print("Помилка: оцінка має бути в межах від 0 до 100!")
        else:
            if score >= 90:
                grade = "A"
            elif score >= 82:
                grade = "B"
            elif score >= 74:
                grade = "C"
            elif score >= 64:
                grade = "D"
            elif score >= 60:
                grade = "E"
            elif score >= 35:
                grade = "FX"
            else:
                grade = "F"

            print(f"Ваша оцінка {score} за шкалою ЄКТС: {grade}")

            if grade in ["A", "B", "C", "D", "E"]:
                print("Результат: Зараховано")
            else:
                print("Результат: Не зараховано")

    except ValueError:
        print("Помилка: введіть ціле число!")

if __name__ == "__main__":
    main()