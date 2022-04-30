import datetime


def get_default_first_date():
    date = datetime.datetime.now()
    date = date.replace(day=1)
    return date


def get_default_last_date():
    return datetime.datetime.now()


def input_date(date_string):
    try:
        date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
        return date
    except AttributeError as _er:
        print(f'Неверно указан формат даты!\n){_er}')
    except Exception as _er:
        print(_er)


def get_first_date():
    default_first_date = get_default_first_date()
    str_default_date = default_first_date.strftime('%d.%m.%Y')
    date_string = input(f'Укажите начальную дату в формате дд.мм.гггг (Enter, чтобы указать {str_default_date}): ')
    if date_string == '':
        return default_first_date
    else:
        return input_date(date_string)


def get_last_date():
    default_last_date = get_default_last_date()
    str_default_date = default_last_date.strftime('%d.%m.%Y')
    date_string = input(f'Укажите конечную дату в формате дд.мм.гггг (Enter, чтобы указать {str_default_date}): ')
    if date_string == '':
        return get_default_last_date()
    else:
        return input_date(date_string)
