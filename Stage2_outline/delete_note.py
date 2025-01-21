"""
Grade 1. Этап 2: Задание 5
"""
from typing import Any


# Запрос у пользователя ввод критерия для удаления
def user_input() -> str:
    result = input('Введите имя пользователя или заголовок для удаления заметки: ')
    result = result.strip().lower()
    return result

def create_delete_list(user_choice: str, database: list):
    delete_list = []
    for i in database:
        current_name = i.get('Имя').lower().strip()
        current_title = i.get('Заголовок').lower().strip()
        if current_name == user_choice:
            delete_list.append(i)
        elif current_title == user_choice:
            delete_list.append(i)
    delete_list = tuple(delete_list)
    print(delete_list)
    return delete_list

def delete_choice(delete_list: tuple, database: list):
    delete_count = 0
    for i in delete_list:
        if i in database:
            database.remove(i)
            delete_count += 1
    if delete_count:
        return True
    else:
        return False

def present_list(database: list):
    if not database:
        print('Список заметок пуст!')
    for i in database:
        print('_' * 7)
        print(f"Имя: {i.get('Имя')}")
        print(f"Заголовок: {i.get('Заголовок')}")
        print(f"Описание: {i.get('Описание')}")
        print('_' * 7)

if __name__ == '__main__':
    test_list = [
        {
            'Имя': 'Алексей',
            'Заголовок': 'Список покупок',
            'Описание': 'Купить продукты на неделю'
        },
        {
            'Имя': 'Мария',
            'Заголовок': 'Учеба',
            'Описание': 'Подготовиться к экзамену'
        }
    ]
    while True:
        result = False
        current_input = user_input()
        delete_list = create_delete_list(current_input, test_list)
        if delete_list:
            result = delete_choice(delete_list, test_list)
        else:
            print('Заметок с таким именем пользователя или заголовком не найдено.')
        if result:
            print('Успешно удалено. Остались следующие заметки:')
            present_list(test_list)
        else:
            print('Что то пошло не так, удаление не было завершено')
            present_list(test_list)




