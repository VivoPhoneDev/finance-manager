def add_expense():
    name = input("Введите название расхода: ").strip()
    while True:
        try:
            amount = float(input("Сколько было потрачено(Без -): "))

            if amount < 0:
                print("Вводите положительные числа!")
                continue

            break

        except ValueError:
            print("Вводите число!")


    expense = {
        "type": "expenses",
        "name": name,
        "amount": amount
    }

    return expense

def total_expenses(data):
    total = 0
    for expense in data:
        total += expense["amount"]

    return total
