"""
Grade 1. Этап 2: Задание 3
"""
import datetime


# запрашиваем у пользователя дату дедлайна и объект datetime.date для дальнейших вычислений
def get_issue_date(format_date: str = '%d.%m.%Y') -> datetime.date:
    # вводим вспомогательные переменные
    formats_date = {'%d.%m.%Y': 'в формате день-месяц-год, например 22.01.2025'}
    prompt_issue_date = f'Введите дату дедлайна ({formats_date.get(format_date)}): '
    # запускаем цикл, чтобы в нём можно было обработать ошибки
    while True:
        try:
            # получаем ввод от пользователя
            date_from_user = input(prompt_issue_date)
            # преобразуем его в список для преобразования в нужный объект
            date_from_user_temp = date_from_user.split('.')
            day = int(date_from_user_temp[0])
            month = int(date_from_user_temp[1])
            year = int(date_from_user_temp[2])
            result_date = datetime.date(year,month,day)
            # с получением нужного объекта выходим из цикла
            return result_date
        except ValueError:
            print('Введено некорректное значение, попробуйте снова в соответствии с указанным форматом')
            continue
        except Exception as e:
            print(f'Произошла ошибка {e}. Попробуйте снова ввести дату в соответствии с указанным форматом')
            continue

def main():
    # Получаем текущую дату и дату дедлайна
    current_date = datetime.date.today()
    issue_date = get_issue_date()
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

if __name__ == '__main__':
    main()

