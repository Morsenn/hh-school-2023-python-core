from datetime import timedelta, date
from random import randint

from hw.beer import Beer
from hw.market import Market
from hw.wine import Wine

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
beers = [Beer(f'Beer number {i}', date.today() + timedelta(days=randint(1, 100))) for i in range(5)]
wines = [Wine(f'Wine number {i}', date.today() + timedelta(days=randint(1, 100))) for i in range(5)]
market = Market(beers, wines)

# Task1 test
print('Task1 test')
print([el.title for el in market.get_drinks_sorted_by_title()])

# Task2 test
print('Task2 test')
print(market.has_drink_with_title('Beer number 2'))
print(market.has_drink_with_title('Beer number 5'))

# Task3 test
print('Task3 test')
def my_format(drink): return f'{drink.title}; date: {drink.production_date}'


from_date = date.today()
to_date = date.today() + timedelta(days=25)
print(f'Начальная дата: {from_date}')
print(f'Конечная дата: {to_date}')
print([my_format(el) for el in market.get_drinks_by_production_date()])
print([my_format(el) for el in market.get_drinks_by_production_date(from_date, to_date)])
print([my_format(el) for el in market.get_drinks_by_production_date(to_date=to_date)])
print([my_format(el) for el in market.get_drinks_by_production_date(from_date)])


# Task4 test
print('Task4 test')
big_beers = [Beer(f'Beer number {i}', date.today() + timedelta(days=randint(1, 100))) for i in range(50000)]
big_wines = [Wine(f'Wine number {i}', date.today() + timedelta(days=randint(1, 100))) for i in range(50000)]
big_market = Market(big_wines, big_beers)
big_market.has_drink_with_title('Beer number 2')
big_market.get_drinks_sorted_by_title()
big_market.get_drinks_by_production_date(from_date, to_date)
