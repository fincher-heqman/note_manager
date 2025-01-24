"""
Grade 1. Этап 1: Задание 5
"""

### Инициализация переменных ###
# пустой list для хранения информации о заметке
information = []
# пустой list для последующего добавления заголовков
titles = []
# устанавливаем переменные для использования текста при запросе ввода у пользователя
prompt_username = 'Пожалуйста, введите имя пользователя: '
prompt_content = 'Пожалуйста, введите описание заметки: '
prompt_status = 'Пожалуйста, введите статус заметки: '
prompt_created_date = (
    'Пожалуйста, введите дату создания заметки в формате "день-месяц-год", например "10-11-2024": '
)
prompt_issue_date = (
    'Пожалуйста, введите дату истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": '
)

### Ввод пользователя ###
# запрашиваем ввод у пользователя
username = input(prompt_username)
content = input(prompt_content)
status = input(prompt_status)
created_date = input(prompt_created_date)
issue_date = input(prompt_issue_date)
# запрашиваем у пользователя названия заголовков и сохраняем их в переменные
title1 = input('Пожалуйста, введите заголовок №1: ')
title2 = input('Пожалуйста, введите заголовок №2: ')
title3 = input('Пожалуйста, введите заголовок №3: ')

### Работа со списками ###
# добавляем заголовки в список
titles.append(title1)
titles.append(title2)
titles.append(title3)
# добавляем все данные в список с информацией
information.append(username)
information.append(content)
information.append(status)
information.append(created_date)
information.append(issue_date)
information.append(titles)

### Вывод информации пользователю ###
# выводим собранные данные (структурировано)
print('Имя пользователя: ', information[0])
print('Содержание заметки: ', information[1])
print('Статус: ', information[2])
print('Дата создания заметки: ', information[3])
print('Дата истечения (дедлайна): ', information[4])
print(f'Заголовки: "{information[5][0]}", "{information[5][1]}", "{information[5][2]}"')

