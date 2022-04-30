import datetime


def input_date(message):
    date_string = input(f'Укажите {message} дату в формате дд.мм.гггг: ')
    try:
        date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
        return date
    except AttributeError as _er:
        print(f'Неверно указан формат даты!\n){_er}')
    except Exception as _er:
        print(_er)
