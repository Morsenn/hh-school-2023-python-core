import time
from random import randint

from hw.invocation_logger import invocation_logger
from hw.wine import Wine
from hw.beer import Beer
from hw.market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
beers = [Beer(f'Beer number {i}', randint(1, 100)) for i in range(5)]
wines = [Wine(f'Wine number {i}', randint(1, 100)) for i in range(5)]
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


print([my_format(el) for el in market.get_drinks_by_production_date()])
print([my_format(el) for el in market.get_drinks_by_production_date(1, 50)])
print([my_format(el) for el in market.get_drinks_by_production_date(to_date=50)])
print([my_format(el) for el in market.get_drinks_by_production_date(50)])


# Task4 test
print('Task4 test')


@invocation_logger(lambda name: print(f'Вызвана функция {name} в {time.time()}'))
def decorator_test(a, b):
    """
    Документация исходной функции
    """
    time.sleep(1)
    return a + b


decorator_test(1, 2)
decorator_test(3, 4)
print(decorator_test.__doc__)
