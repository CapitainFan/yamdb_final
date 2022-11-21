import datetime as dt


def validate_year(year):
    current_date = dt.date.today()
    if year > current_date.year:
        raise ValueError(f'Некорректный год {year}')
