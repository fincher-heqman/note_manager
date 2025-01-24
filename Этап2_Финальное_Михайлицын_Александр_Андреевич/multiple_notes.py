"""
Grade 1. Этап 2: Задание 4
"""
import datetime


def is_valid_str(user_input: str) -> bool:
    # проверка строки на валидную в том, что строка не должна быть пустой
    if not user_input:
        return False
    return True

def input_valid_str(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if not is_valid_str(user_input):
            print('Ошибка при введении значения, введите пожалуйста не пустое значение')
            continue
        user_input = user_input.capitalize()
        return user_input

def is_valid_status_choice(user_input: str) -> bool:
    # проверка на соответствие допустимым значениям
    available_values = ('выполнено', 'в процессе', 'отложено')
    if user_input not in available_values:
        return False
    return True

def input_valid_status(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if not is_valid_status_choice(user_input):
            print('Ошибка при введении значения статуса, введите пожалуйста допустимое значение')
            continue
        return user_input

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

def input_valid_date(prompt: str) -> datetime.date:
    while True:
        user_input = input(prompt)
        if not is_valid_date(user_input):
            print('Ошибка при введении даты, введите пожалуйста дату в соответствии с указанным форматом')
            continue
        user_input_temp = user_input.split('.')
        day = int(user_input_temp[0])
        month = int(user_input_temp[1])
        year = int(user_input_temp[2])
        user_input = datetime.date(year, month, day)
        return user_input

# функция для создания заметки
def create_note() -> dict:
    # переменные для передачи в input()
    prompt_username = 'Пожалуйста, введите имя пользователя: '
    prompt_title = 'Пожалуйста, введите заголовок заметки: '
    prompt_content = 'Пожалуйста, введите описание заметки: '
    prompt_status = 'Пожалуйста, введите статус заметки: '
    prompt_created_date = (
        'Пожалуйста, введите дату создания заметки в формате "день-месяц-год", например "10-11-2024": '
    )
    prompt_issue_date = (
        'Пожалуйста, введите дату истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": '
    )

    username = input_valid_str(prompt_username)
    title = input_valid_str(prompt_title)
    content = input_valid_str(prompt_content)
    status = input_valid_status(prompt_status)
    created_date = input_valid_date(prompt_created_date)
    issue_date = input_valid_date(prompt_issue_date)

    result = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }
    return result

# функция для сохранения заметки
def save_note(new_note: dict, database: list) -> None:
    database.append(new_note)
    print(f'Заметка с именем {new_note["username"]} была успешно добавлена в список')

# функция для вывода списка заметок
def print_notes(database: list) -> None:
    # преобразуем в кортеж для оптимизации
    database = tuple(database)
    if not database:
        print('Список заметок пуст!')
        return None
    print('Список заметок:')
    # основной цикл вывода заметок из списка
    for i in database:
        print('_' * 7)
        print(f'Имя: {i["username"]}')
        print(f'Заголовок: {i["title"]}')
        print(f'Описание: {i["content"]}')
        print(f'Статус: {i["status"]}')
        print(f'Дата создания: {i["created_date"].strftime("%d-%m-%Y")}')
        print(f'Дедлайн: {i["issue_date"].strftime("%d-%m-%Y")}')
        print('_' * 7)

### Основная функция задания ###
def main() -> None:
    user_choice = 'да'
    notes = []
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
        # проверяем нужно ли создавать заметку или вывести список заметок
        if user_choice == 'да':
            print('Запускается создаение заметки')
        elif user_choice == 'нет':
            print_notes(notes)
            break
        else:
            print('Пожалуйста, введите корректное значение, предложенное в скобках')
            user_choice = input('Хотите добавить ещё одну заметку? (да/нет):')
            user_choice = user_choice.lower().strip()
            continue
        current_note = create_note()
        save_note(current_note, notes)
        # Получаем ответ от пользователя, для принятия решения о дальнейшем продолжении создания заметок
        user_choice = input('Хотите добавить ещё одну заметку? (да/нет):')
        # Форматируем для дальнейшей проверки
        user_choice = user_choice.lower().strip()

if __name__ == '__main__':
    main()

