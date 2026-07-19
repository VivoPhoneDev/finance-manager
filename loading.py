import time
import sys

def load():
    spinner = ['|', '/', '-', '\\']
    for i in range(20):

        # Выводим символ и возвращаем курсор в начало строки
        sys.stdout.write(f'\rЗагрузка... {spinner[i % len(spinner)]}')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\rГотово!   ')


