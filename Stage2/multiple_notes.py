"""
Grade 1. Этап 2: Задание 4
"""
import datetime

# Добавляем дополнительно проверку на пустую строку
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

# Добавляем дополнительно проверку на валидность статуса
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

# Добавляем дополнительно проверку на валидность даты
def input_valid_date(text_for_user: str) -> datetime.date:
    try:
        result = input(text_for_user)
        result =  datetime.datetime.strptime(result, '%d-%m-%Y').date()
    except ValueError:
        print('Ошибка ввода, соблюдайте пожалуйста формат ввода даты')
        result = input_valid_date(text_for_user)
    return result



# Можно, пожалуйста, не писать что делает функция если по названию понятно? :)
def create_note() -> dict:
    username = input_valid_str('Введите имя пользователя: ')
    title = input_valid_str('Введите заголовок заметки: ')
    content = input_valid_str('Введите описание заметки: ')
    status = input_valid_status('Введите статус заметки (новая, в процессе, выполнено): ')
    created_date = input_valid_date('Введите дату создания (день-месяц-год): ')
    issue_date = input_valid_date('Введите дедлайн (день-месяц-год): ')
    result = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }
    return result

def save_note(new_note: dict, database: list) -> None:
    database.append(new_note)
    print(f'Заметка с именем {new_note["username"]} была успешно добавлена в список')

def print_notes(database: list) -> None:
    if not database:
        print('Список заметок пуст!')
        return None
    print('Список заметок:')
    for i in database:
        print('_' * 7)
        print(f'Имя: {i["username"]}')
        print(f'Заголовок: {i["title"]}')
        print(f'Описание: {i["content"]}')
        print(f'Статус: {i["status"]}')
        print(f'Дата создания: {i["created_date"].strftime("%d-%m-%Y")}')
        print(f'Дедлайн: {i["issue_date"].strftime("%d-%m-%Y")}')
        print('_' * 7)

if __name__ == '__main__':
    user_choice = 'да'
    notes = []
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    while True:
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

