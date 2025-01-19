"""
Grade 1. Этап 1: Задание 5
"""

# список для хранения информации о заметке
information = []

# сбор информации
name = input('Введите имя заметки: ')
content = input('Введите содержание заметки: ')
status = input('Введите статус заметки: ')
date = input('Введите дату заметки в формате "день-месяц-год", например "10-12-2024: ')
titles = []

# Запрашиваем у пользователя названия заголовков и сохраняем их в переменные
title1 = input('Введите заголовок №1: ')
title2 = input('Введите заголовок №2: ')
title3 = input('Введите заголовок №3: ')
# Добавляем заголовки в список
titles.append(title1)
titles.append(title2)
titles.append(title3)

# Добавляем все данные в список с информацией
information.append(name)
information.append(content)
information.append(status)
information.append(date)
information.append(titles)

# Выводим собранные данные
print(information)
