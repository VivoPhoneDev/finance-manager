from actions import actions_print
from expenses import add_expense, total_expenses
from loading import load
from storage import load_data, save_data
import time


_action = 0
data = load_data()


while _action != 4:
    actions_print()
    try:
        _action = int(input("Поле ввода: "))
        if _action == 1:
            data.append(add_expense())
            save_data(data)
            print("--- Успешно добавлено ---")
        
        elif _action == 2:
            load()
            print(f"--- Сумма расходов: {total_expenses(data)} ---")
            
        elif _action == 3:
            load()
            if not data:
                print("Пока нет расходов !")

            else:
                print("--- Траты ---")
                for expense_ in data:
                    print(f"{expense_['name']} - {expense_['amount']} ₽")
                    time.sleep(0.1)
                print(f"====================\nИтого: {total_expenses(data)}")

        elif _action == 4:
            break
        
        else:
            print('--- Такого действия нет! ---')
            
    except ValueError:
        print("Неверный ввод!")
