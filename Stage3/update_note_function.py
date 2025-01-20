"""
Grade 1. Этап 3: Задание 2
Задание: Функция обновления заметки

"""
import datetime


# Добавляем дополнительно проверку к вводу пользователем на пустую строку
def input_valid_str(text_for_user: str) -> str:
    try:
        result = input(text_for_user)
        result = result.strip()
        if not result: raise ValueError
    except ValueError:
        print('Ошибка ввода, не допускайте пожалуйста пустых значений')
        result = input_valid_str(text_for_user)
    result = result.capitalize()
    return result

# Добавляем дополнительно проверку к вводу пользователем на валидность статуса
def input_valid_status(text_for_user: str) -> str:
    try:
        result = input(text_for_user)
        acceptable_values = [
            'новая',
            'в процессе',
            'выполнено'
        ]
        result = result.strip().lower()
        if result not in acceptable_values:
            raise ValueError
    except ValueError:
        print('Ошибка ввода, введите пожалуйста одно из предложенных значений')
        result = input_valid_status(text_for_user)
    return result

# Добавляем дополнительно проверку к вводу пользователем на валидность даты
def input_valid_date(text_for_user: str) -> datetime.date:
    try:
        result = input(text_for_user)
        result =  datetime.datetime.strptime(result, '%d-%m-%Y').date()
    except ValueError:
        print('Ошибка ввода, соблюдайте пожалуйста формат ввода даты')
        result = input_valid_date(text_for_user)
    return result

# Принимает заметку (словарь) в качестве аргумента.
# Позволяет пользователю выбрать, какое поле заметки нужно обновить.
# Запрашивает новое значение для выбранного поля.
# Обновляет указанное поле заметки.
def update_note(note: dict):
    user_choice = input("""
    Вы можете обновить следующие заметки, введите название, или номер для изменения:
    1. username
    2. title
    3. content
    4. status
    5. issue_date
    """)
    user_choice = user_choice.lower().strip()
    if user_choice == '1' or user_choice == 'username':
        note['username'] = input_valid_str('Введите username')
    elif user_choice == '2' or user_choice == 'title':
        note['title'] = input_valid_str('Введите title')
    elif user_choice == '3' or user_choice == 'content':
        note['content'] = input_valid_str('Введите content')
    elif user_choice == '4' or user_choice == 'status':
        note['status'] = input_valid_status('Введите status')
    elif user_choice == '5' or user_choice == 'issue_date':
        note['issue_date'] = input_valid_date('Введите issue_date')

def main():
    # Текущие данные заметки:
    pass
    # Программа предлагает выбрать поле для обновления:
    # Пользователь вводит новое значение:

    # Программа обновляет поле и выводит обновлённую заметку:



