"""
Grade 1. Этап 3: Задание 1
Общее описание: Введение функций для упрощения кода и организации логики.
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

# Запрашивает у пользователя информацию для создания заметки.
# Возвращает данные заметки в виде словаря.
def create_note() -> dict:
    username = input_valid_str('Введите имя пользователя: ')
    title = input_valid_str('Введите заголовок заметки: ')
    content = input_valid_str('Введите описание заметки: ')
    status = input_valid_status('Введите статус заметки (новая, в процессе, выполнено): ')
    created_date = datetime.date.today().strftime('%d-%m-%Y')
    issue_date = input_valid_date('Введите дедлайн (день-месяц-год): ').strftime('%d-%m-%Y')
    result = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }
    return result

if __name__ == '__main__':
    current_note = create_note()
    print(current_note)