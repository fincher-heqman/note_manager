"""
Grade 1. Этап 2: Задание 5
"""


### Блок функций ###
# Запрашивает у пользователя значение для удаления
def get_value_to_delete(prompt_for_user: str) -> str:
    value = input(prompt_for_user)
    return value

# Функция для отображения пользователю списка заметок
def represent_notes(notes_pool: list) -> None:
    notes_pool_temp = tuple(notes_pool)
    # Если пустой список нужно указать это пользователю
    if not notes_pool_temp:
        print('Список с заметками пуст!')
        return
    for note in notes_pool_temp:
        print('_' * 8)
        print(f'Имя: {note.get("Имя")}')
        print(f'Заголовок: {note.get("Заголовок")}')
        print(f'Описание: {note.get("Описание")}')

# Проверка, есть ли заметка в списке
def check_note_exist(notes_pool: list, note: dict) -> bool:
    status_exist = False
    if note in notes_pool:
        status_exist = True
    return status_exist

# Удаляет заметки по заданному значению. Возвращает True если успешно, иначе False.
def delete_note_by_value(notes_pool: list, value: str, criteria_delete: tuple = ('Имя', 'Заголовок')) -> tuple:
    # Создаем переменные для определения было ли удаление и кортеж для оптимизации цикла
    delete_status = False
    temp_notes_pool = tuple(notes_pool)
    for note in temp_notes_pool:
        # Реализуется проверка существования заметки перед удалением. (но она тут вроде не нужна)
        if not check_note_exist(notes_pool, note):
            continue
        # Указывается индекс для удаления при соответствии и вспомогательная переменная для удаления
        current_index = notes_pool.index(note)
        delete_current = False
        # Реализация проверки на критерий для удаления
        for criterion in criteria_delete:
            # Реализация нечувствительного регистра через 2 форматированные переменные
            criterion_value = note.get(criterion).lower().strip()
            user_value = value.lower().strip()
            if criterion_value == user_value:
                delete_current = True
                delete_status = True
                break
        if delete_current:
            notes_pool.pop(current_index)

    return notes_pool, delete_status

def update_list(notes_pool: list, value: str):
    result = delete_note_by_value(notes_pool, value)
    returning_list = result[0]
    delete_status = result[1]
    if delete_status:
        print('Удаление заметки (заметок) по заданному значению произошло успешно. ')
        print('Остались следующие заметки: ')
        represent_notes(returning_list)
    else:
        print('Заметок по указанному значению не найдено. ')
    return returning_list

def choice_insurance(value: str) -> bool:
    prompt = (f'Вы уверены что хотите удалить заметки по значению "{value}"? '
              f'Пожалуйста, введите да/нет соответственно: ')
    while True:
        user_answer = input(prompt)
        user_answer = user_answer.lower().strip()
        if user_answer == 'да':
            return True
        elif user_answer == 'нет':
            return False
        else:
            prompt = 'Было введен некорректный ответ. Пожалуйста, введите да/нет соответственно: '

### Основная функция скрипта ###
def main() -> None:
    # Инициализируем переменную с заметками
    note1 = {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'}
    note2 = {'Имя': 'Алексей', 'Заголовок': 'Отдых на гавайях', 'Описание': 'Отдохнуть'}
    note3 = {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}
    note4 = {'Имя': 'Михаил', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}
    notes = [note1, note2, note3, note4]
    # Инициализируем вспомогательные переменные
    prompt_delete_note = 'Введите имя пользователя или заголовок для удаления заметки \n'
    prompt_delete_note += '(Если хотите выйти из программы введите пустое значение): '

    # Отображаем имеющиеся заметки на старте
    print('Текущие заметки: ')
    represent_notes(notes)
    print('*' * 8)

    while True:
        # Запрашиваем значение у пользователя для удаления
        value_to_delete = get_value_to_delete(prompt_delete_note)
        if not value_to_delete:
            print('Программа завершает свое действие')
            return
        # Обновляем список по значению
        if choice_insurance(value_to_delete):
            notes = update_list(notes, value_to_delete)
        else:
            print(f'Вы отказались удалять заметки по значению {value_to_delete}')
        print('*' * 8)

if __name__ == '__main__':
    main()
