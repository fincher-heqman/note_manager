"""
Grade 1. Этап 3: Задание 3
Задание: Функция отображения заметок
display_notes(notes):
Принимает список заметок (каждая заметка — это словарь).
Отображает каждую заметку в удобном и понятном формате.
"""
from textwrap import dedent


# Вспомогательная функция
def display_note(note: dict, num_note: int = None) -> None:
    # Переменная num_note используется если нужно отобразить несколько заметок
    username = note.get('username')
    title = note.get('title')
    content = note.get('content')
    status = note.get('status')
    created_date = note.get('created_date')
    issue_date = note.get('issue_date')

    print ('-' * 8)
    if not num_note is None:
        print(f'Заметка №{num_note}')

    print(f'Имя пользователя: {username}')
    print(f'Заголовок заметки: {title}')
    print(f'Описание заметки: {content}')
    print(f'Статус заметки: {status}')
    print(f'Дата создания заметки: {created_date}')
    print(f'Дата истечения (дедлайна): {issue_date}')

### Основная функция вывода заметок по заданию ###

def display_notes(notes_pool: list) -> None:
    if not notes_pool:
        message = dedent("""
            У вас нет сохранённых заметок.
            Каждая заметка должна быть выведена в формате:
            Заметка №1:
            Имя пользователя: Алексей
            Заголовок: Список покупок
            Описание: Купить продукты на неделю
            Статус: новая
            Дата создания: 27-11-2024
            Дедлайн: 30-11-2024
            ------------------------------
        """)
        print(message)
        return

    notes_pool = tuple(notes_pool)
    count = 0

    # Для интерактивности при количестве заметок больше 4
    length = len(notes_pool)
    print('Список заметок: ')
    if length < 4:
        for note in notes_pool:
            count += 1
            display_note(note, count)
    else:
        for note in notes_pool:
            count += 1
            display_note(note, count)
            remainder = length - count
            if remainder:
                message = 'Нажмите "Enter" для вывода следующей заметки '
                message += f'(Остаток - {remainder}): '
                input(message)
            else:
                print(f'Был выведен список из {length} заметок')
    print('*' * 8)

### Блок вспомогательных функций для демонстрации основной функции ###
def demo1() -> None:
    """
    Демонстрируем функцию с пустым списком заметок
    """
    notes = []
    display_notes(notes)

def demo2() -> None:
    """
    Демонстрируем функцию с одной заметкой
    """
    note1 = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.12.2024',
        'issue_date': '30.12.2024'
    }
    notes = [note1]
    display_notes(notes)

def demo3() -> None:
    """
    Демонстрируем функцию с парой заметок
    """
    note1 = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.12.2024',
        'issue_date': '30.12.2024'
    }
    note2 = {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '12.12.2024',
        'issue_date': '15.12.2024'
    }
    notes = [note1, note2]
    display_notes(notes)

# Функция для демонстрации интерактивности
def demo4() -> None:
    """
    Демонстрируем функцию с парой заметок
    """
    note1 = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.12.2024',
        'issue_date': '30.12.2024'
    }
    note2 = {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'created_date': '12.12.2024',
        'issue_date': '15.12.2024'
    }
    note3 = {
        'username': 'Александр',
        'title': 'Сдача задания',
        'content': 'Сделать и сдать задание',
        'status': 'в процессе',
        'created_date': '25.01.2025',
        'issue_date': '27.01.2025'
    }
    note4 = {
        'username': 'Михаил',
        'title': 'Проверка задания',
        'content': 'Проверить задание ученика python-курса',
        'status': 'в процессе',
        'created_date': '27.01.2025',
        'issue_date': '12.12.2025'
    }
    notes = [note1, note2, note3, note4]
    display_notes(notes)


### Функция для демонстрации задания ###
def main() -> None:
    demo1()
    demo2()
    demo3()
    demo4()

if __name__ == '__main__':
    # Через main() вызываем create_note()
    main()