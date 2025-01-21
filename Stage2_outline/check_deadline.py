"""
Grade 1. Этап 2: Задание 3
"""
import datetime


# Функция для привода даты к нужному формату и выводу её
def print_date_for_user(date, time_format: str = "%d-%m-%Y") -> None:
    date = date.strftime(time_format)
    text_for_user = f'Текущая дата: {date}'
    print(text_for_user)

# Запрашиваем у пользователя дату дедлайна
def user_input() -> datetime.date:
    try:
        result_date = input('Введите дату дедлайна (в формате день-месяц-год): ')
        result_date = datetime.datetime.strptime(result_date, "%d-%m-%Y").date()
    except ValueError:
        print('Введено некорректное значение, попробуйте снова в соответствии с указанным форматом')
        result_date = user_input()
    return result_date


if __name__ == '__main__':
    # Получаем текущую дату и дату дедлайна
    current_date = datetime.date.today()
    issue_date = user_input()

    # Вычисление разницы в датах
    result = issue_date - current_date
    result = result.days

    # Проверяем на условие
    if result == 0:
        print('Внимание дедлайн сегодня!')
    elif result > 0:
        print(f'До дедлайна осталось {result}')
    elif result < 0:
        print(f'Внимание! Дедлайн истёк {result} дня (дней) назад.')


