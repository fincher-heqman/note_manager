Репозиторий содержит готовые задания:

Этап 1:
greetings.py (Задание 1)
Созданы базовые переменные для заметки: username, title, content, status, created_date, issue_date.
Вывод значений организован через print.
date_changer.py (Задание 2)
Реализовано преобразование формата отображения дат для пользователя, 
исключив год при выводе переменных created_date и issue_date.
add_input.py (Задание 3)
Переменные инициализируются через пользовательский ввод (input).
Реализованы подсказки для пользователя о том, как вводить данные, включая формат дат.
add_list.py (Задание 4)
Пользователь вводит три заголовка, которые сохраняются в список.
Введенные данные отображаются, включая список заголовков.
final.py (Задание 5)
Все данные организованы в словарь для заметки, включая:
Поля: username, content, status, created_date, issue_date.
Список заголовков как значение ключа titles.
Все данные выводятся на экран в структурированном виде.

Этап 2:
add_titles_loop.py (Задание 1)
Запрашивает у пользователя заголовки.
Позволяет завершить ввод специальной командой или пустым вводом.
Выводит итоговый список добавленных заголовков.
update_status.py (Задание 2)
Показывает текущий статус заметки.
Предлагает изменить статус на один из предложенных.
Обрабатывает некорректный ввод.
check_deadline.py (Задание 3)
Запрашивает дату дедлайна и сравнивает её с текущей датой.
Сообщает, истёк ли дедлайн или сколько дней осталось.
Проверяет корректность формата ввода.
multiple_notes.py (Задание 4)
Создаёт несколько заметок через ввод данных (имя, заголовок, описание, статус, дату создания, дедлайн).
Хранит заметки в списке словарей.
Выводит список всех заметок.
delete_note.py (Задание 5)
Удаляет заметку по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.