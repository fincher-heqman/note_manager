"""
Grade 1. Этап 3: Задание 4
Задание: Функция поиска заметок.
Возвращает список заметок, которые соответствуют заданным критериям поиска.
Функция возвращает список заметок, которые соответствуют заданным критериям поиска.
Поиск по ключевым словам:
Заметки отбираются, если заданное ключевое слово встречается в любом из полей: title, content, или username.
Поиск по статусу:
Заметки отбираются, если их поле status совпадает с указанным.
Если указаны оба параметра (keyword и status), выполняйте поиск с учётом обоих условий.
Программа должна выводить найденные заметки в удобном формате. Если заметки не найдены, выведите сообщение:
"""
# Импортируем функцию из уже готового задания, надеюсь так можно
from display_notes_function import display_notes


### Блок функций ###
# Поиск по ключевому слову
def search_by_keyword(notes_pool: tuple, keyword: str) -> list:
    result = []
    keyword = keyword.lower().strip()
    for note in notes_pool:
        note_text = note.get('username').lower()
        note_text += note.get('title').lower()
        note_text += note.get('content').lower()
        is_condition_met = keyword in note_text
        if is_condition_met:
            result.append(note)
    return result

# Поиск по статусу
def search_by_status(notes_pool: tuple, status: str) -> list:
    result = []
    status = status.lower().strip()
    for note in notes_pool:
        note_status = note.get('status').lower()
        is_condition_met = status == note_status
        if is_condition_met:
            result.append(note)
    return result

# Поиск по ключевому слову и статусу
def search_by_keyword_and_status(notes_pool: tuple, keyword: str, status: str) -> list:
    result = []
    keyword = keyword.lower().strip()
    status = status.lower().strip()
    for note in notes_pool:
        note_text = note.get('username').lower()
        note_text += note.get('title').lower()
        note_text += note.get('content').lower()
        condition_keyword = keyword in note_text
        note_status = note.get('status').lower()
        condition_status = status == note_status
        is_condition_met = condition_keyword and condition_status
        if is_condition_met:
            result.append(note)
    return result

# Главная функция задания
def search_notes(notes_pool: list, keyword: str=None, status: str=None) -> list:
    if not notes_pool:
        print('Список заметок пуст!')
        return []
    result_list = []
    notes_pool = tuple(notes_pool)
    if keyword and status:
        result_list = search_by_keyword_and_status(notes_pool, keyword, status)
    elif keyword:
        result_list = search_by_keyword(notes_pool, keyword)
    elif status:
        result_list = search_by_status(notes_pool, status)
    return result_list

def display_result(result: list) -> None:
    if not result:
        print('Заметки, соответствующие запросу, не найдены.')
        print('*' * 8)
    else:
        display_notes(result)

### Блок функций для демонстрации результата

# Поиск с пустым исходным списком
def demo1() -> None:
    print('demo1, Демонстрация результата с пустым списком на входе: ')
    notes = []
    result = search_notes(notes, status='работы')
    # Выводим результат
    display_result(result)

# Поиск по ключевому слову
def demo2(notes: list) -> None:
    print('demo2, Демонстрация результата по ключевому слову: ')
    result = search_notes(notes, keyword='работы')
    # Выводим результат
    display_result(result)

# Поиск по статусу
def demo3(notes: list) -> None:
    print('demo3, Демонстрация результата по статусу: ')
    result = search_notes(notes, status='НОВАЯ')
    # Выводим результат
    display_result(result)

# Поиск по ключевому слову и статусу
def demo4(notes: list) -> None:
    print('demo4, Демонстрация результата по ключевому слову и статусу: ')
    result = search_notes(notes, keyword='мария', status='в процессе')
    # Выводим результат
    display_result(result)

# Поиск по результату, которого быть не может
def demo5(notes: list) -> None:
    print('demo5, Демонстрация результата, если ничего не нашлось: ')
    result = search_notes(notes, status='вася')
    # Выводим результат
    display_result(result)

def main():
    # Исходный список заметок
    original_list = notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'
        },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '25-11-2024',
            'issue_date': '01-12-2024'
        },
        {
            'username': 'Иван',
            'title': 'План работы',
            'content': 'Завершить проект',
            'status': 'выполнено',
            'created_date': '20-11-2024',
            'issue_date': '26-11-2024'
        },
        {
            'username': 'Михаил',
            'title': 'Проверить задание',
            'content': 'Пожалуйста, прошу проверить задание студента по python',
            'status': 'новая',
            'created_date': '27-01-2025',
            'issue_date': '12-12-2025'
        }
    ]
    demo1()
    demo2(original_list)
    demo3(original_list)
    demo4(original_list)
    demo5(original_list)

if __name__ == "__main__":
    main()