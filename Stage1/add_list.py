"""
Grade 1. Этап 1: Задание 4
"""

# Создаем список для последующего добавления в него заголовков
titles = []

# Запрашиваем у пользователя названия заголовков и сохраняем их в переменные
title1 = input('Введите заголовок №1: ')
title2 = input('Введите заголовок №2: ')
title3 = input('Введите заголовок №3: ')

# Добавляем заголовки в список
titles.append(title1)
titles.append(title2)
titles.append(title3)

"""
++
amount_titles = int(input('Введите число заголовков для добавления: '))
titles = []
for i in range(1, amount_titles+1):
    new_title = input(f'Введите заголовок №{i}: ')
    titles.append(new_title)
"""
