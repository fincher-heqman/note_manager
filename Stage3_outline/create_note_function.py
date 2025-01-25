"""
Grade 1. Этап 3: Задание 1
Общее описание для Этапа 3: Введение функций для упрощения кода и организации логики.

Настоящая create_note() функция: для создания новой заметки и возврата словаря.
"""
import datetime


### Блок функций ###
## Вспомогательные функции для отсеивания некорректных значений ##
# Для проверки на валидность строки после ввода
def is_valid_str(user_input: str) -> bool:
    # проверка строки на валидную в том, что строка не должна быть пустой
    if not user_input:
        return False
    return True

# Для запроса у пользователя валидной строки
def input_valid_str(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if not is_valid_str(user_input):
            print('Ошибка при введении значения, введите пожалуйста не пустое значение')
            continue
        user_input = user_input.capitalize()
        return user_input

# Для проверки на валидность значения изменения статуса
def is_valid_status_choice(user_input: str) -> bool:
    # проверка на соответствие допустимым значениям
    available_values = ('выполнено', 'в процессе', 'отложено')
    if user_input not in available_values:
        return False
    return True
# Для запроса у пользователя значения изменения статуса
def input_valid_status(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if not is_valid_status_choice(user_input):
            print('Ошибка при введении значения статуса, введите пожалуйста допустимое значение')
            continue
        return user_input

# Для проверки на валидность значения даты
def is_valid_date(user_input: str) -> bool:
    # проверка на возможность преобразования указанной даты в объект
    try:
        user_input_temp = user_input.split('.')
        day = int(user_input_temp[0])
        month = int(user_input_temp[1])
        year = int(user_input_temp[2])
        datetime.date(year, month, day)
        return True
    except ValueError:
        print(f'Ошибка в набранной дате {ValueError}. Пожалуйста, введите дату в соответствии с указанным форматом')
        return False
    except Exception as e:
        print(f'Ошибка в набранной дате {e}. Пожалуйста, введите дату в соответствии с указанным форматом')
        return False

# Для запроса у пользователя значения даты
def input_valid_date(prompt: str) -> str:
    while True:
        user_input = input(prompt)
        if not is_valid_date(user_input):
            print('Ошибка при введении даты, введите пожалуйста дату в соответствии с указанным форматом')
            continue
        user_input_temp = user_input.split('.')
        day = int(user_input_temp[0])
        month = int(user_input_temp[1])
        year = int(user_input_temp[2])
        user_input = datetime.date(year, month, day).strftime('%d.%m.%Y')
        return user_input

## Функция для непосредственного создания заметки ##
# Запрашивает значения у пользователя через вспомогательные функции (указанные выше)
def create_note() -> dict:
    # переменные для передачи в input()
    prompt_username = 'Пожалуйста, введите имя пользователя: '
    prompt_title = 'Пожалуйста, введите заголовок заметки: '
    prompt_content = 'Пожалуйста, введите описание заметки: '
    prompt_status = 'Пожалуйста, введите статус заметки из предложенных (выполнено, в процессе, отложено): '
    prompt_issue_date = (
        'Пожалуйста, введите дату истечения заметки (дедлайн) в формате "день.месяц.год", например "10.12.2024": '
    )

    # Запрашиваем все необходимые данные у пользователя и сохраняем в переменные
    username = input_valid_str(prompt_username)
    title = input_valid_str(prompt_title)
    content = input_valid_str(prompt_content)
    status = input_valid_status(prompt_status)
    issue_date = input_valid_date(prompt_issue_date)
    # Дата создания заполняется автоматически
    created_date = datetime.date.today().strftime('%d.%m.%Y')

    # Формируется словарь из полученных значений
    result = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }
    return result

## Функции для отображения пользователю информации о заметке и управления списком ##

# Функция для структурированного отображения заметки
def print_note(note: dict, num_note: int = None) -> None:
    # Переменная num_note используется если нужно отобразить несколько заметок
    username = note.get('username')
    title = note.get('title')
    content = note.get('content')
    status = note.get('status')
    created_date = note.get('created_date')
    issue_date = note.get('issue_date')

    print ('_' * 8)
    if not num_note is None:
        print(f'Заметка №{num_note}')

    print(f'Имя пользователя: {username}')
    print(f'Заголовок заметки: {title}')
    print(f'Описание заметки: {content}')
    print(f'Статус заметки: {status}')
    print(f'Дата создания заметки: {created_date}')
    print(f'Дата истечения (дедлайна): {issue_date}')

### Функция для демонстрации задания ###
def main() -> None:
    current_note = create_note()
    print_note(current_note)

if __name__ == '__main__':
    # Через main() вызываем create_note()
    main()