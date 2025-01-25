"""
Grade 1. Этап 3: Задание 2
Задание: Функция обновления заметки

"""
import datetime
from textwrap import dedent


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

### Основная функция по заданию ###

def update_note(note: dict) -> dict:
    """
    Принимает заметку (словарь) в качестве аргумента.
    Позволяет пользователю выбрать, какое поле заметки нужно обновить.
    Запрашивает новое значение для выбранного поля.
    Обновляет указанное поле заметки.
    """
    # Делаем копию словаря, чтобы не было непредвиденного неявного изменения словаря
    note = note.copy()
    prompt = dedent("""
        Вы можете обновить следующие данные заметки, введите название, или номер для изменения (например "1"):
        1. username
        2. title
        3. content
        4. status
        5. issue_date
        """)
    prompt += 'Ввод: '

    while True:
        # Запрашиваем выбор данных для изменения у пользователя
        user_choice = input(prompt)
        user_choice = user_choice.lower().strip()
        # Устанавливаем соответствие выбора пользователя и запрашиваем данные для изменения
        if user_choice == '1' or user_choice == 'username':
            note['username'] = input_valid_str('Введите новое значение username (Имя пользователя): ')
        elif user_choice == '2' or user_choice == 'title':
            note['title'] = input_valid_str('Введите новое значение title (Заголовок): ')
        elif user_choice == '3' or user_choice == 'content':
            note['content'] = input_valid_str('Введите новое значение content (Описание): ')
        elif user_choice == '4' or user_choice == 'status':
            note['status'] = input_valid_status(
                'Введите новое значение status (Статус), (выполнено, в процессе, отложено): '
            )
        elif user_choice == '5' or user_choice == 'issue_date':
            note['issue_date'] = input_valid_date(
                'Введите новое значение issue_date (Дату дедлайна) в формате "день.месяц.год", например "10.12.2024": '
            )
        else:
            # В случае если значение не соответствует предложенному выбору сообщаем об этом и запрашиваем снова
            print('Было введено некорректное значение, введите пожалуйста один из предложенных вариантов! ')
            print('*' * 8)
            continue

        return note

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

### Функция для демонстрации функционала модуля ###
def main():
    note = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.12.2024',
        'issue_date': '30.12.2024'
    }
    print('Текущие данные заметки: ')
    print_note(note)
    print('Какие данные вы хотите обновить?')
    current_note = update_note(note)
    print('Заметка обновлена: ')
    print_note(note)

if __name__ == "__main__":
    main()
