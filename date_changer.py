"""
Grade 1. Этап 1: Задание 2
"""

# Запрашиваем при помощи ввода дату у пользователя
created_date = input('Введите дату создания заметки (формат = день-месяц-год, например "10-11-2024"')
issue_date = input('Введите дату дедлайна заметки (формат = день-месяц-год, например "10-11-2024"')

# Создаем временные переменные для хранения представления даты
temp_created_date = created_date[:-5]
temp_issue_date = issue_date[:-5]

# Выводим представление даты
print(temp_created_date)
print(temp_issue_date)

# 2 допущения:
# 1) пользователь всегда соблюдает формат ввода
# 2) год всегда состоит из 4 цифр
# полагаю, что 2 допущения можно избежать, если в срез указать индекс 3 по счёту "-"