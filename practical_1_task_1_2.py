# practical_01_task_1_2.py

def main():
    # TODO: Зчитати рядок від користувача
    raw_input = input("Введіть число: ")

    # TODO: Перетворити в int, float, bool та вивести тип кожного
    try:
        val_int = int(raw_input)
        val_float = float(raw_input)
        val_bool = bool(raw_input)
        val_str = str(raw_input) 

        print("\nРезультати конвертації")
        print(f"int: {val_int}, тип: {type(val_int)}, чи є int? {isinstance(val_int, int)}")
        print(f"float: {val_float}, тип: {type(val_float)}, чи є float? {isinstance(val_float, float)}")
        print(f"bool: {val_bool}, тип: {type(val_bool)}, чи є bool? {isinstance(val_bool, bool)}")
        print(f"str: {val_str}, тип: {type(val_str)}")
        
    except ValueError:
        print("\nПомилка: введено не число! Неможливо перетворити на int або float.")

    # TODO: 
    print("\nФорматоване виведення")
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")

    try:
        age_int = int(age)
        print(f"Привіт, |{name:>15}|! Твій вік: {age_int:03d} років.")
    except ValueError:
        print("Помилка: вік має бути числом!")

    # TODO: 
    print("\nДодаткові функції")
    my_list = list(range(1, 6))
    print(f"Список з range(1, 6): {my_list}")
    print(f"Довжина списку (len): {len(my_list)}")
    print(f"ID списку в пам'яті (id): {id(my_list)}")


if __name__ == "__main__":
    main()