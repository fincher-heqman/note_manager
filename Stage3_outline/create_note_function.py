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

# Функция создания заметки
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

# Функция для структурированного отображения заметки
def print_note(note: dict) -> None:
    username = note.get('username')
    title = note.get('title')
    content = note.get('content')
    status = note.get('status')
    created_date = note.get('created_date')
    issue_date = note.get('issue_date')

    print(f'Имя пользователя: {username}')
    print(f'Заголовок заметки: {title}')
    print(f'Описание заметки: {content}')
    print(f'Статус заметки: {status}')
    print(f'Дата создания заметки: {created_date}')
    print(f'Дата истечения (дедлайна): {issue_date}')

### Основная функция задания ###
def main() -> None:
    current_note = create_note()
    print_note(current_note)

if __name__ == '__main__':
    main()