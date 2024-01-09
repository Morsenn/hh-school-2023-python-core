from datetime import datetime
from itertools import chain

from hw.invocation_logger import invocation_logger


class Market:
    @invocation_logger(lambda name: print(f'Вызвана функция {name} в {datetime.now()}'))
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = sorted(Market.check_list(wines), key=lambda drink: drink.title)
        self.beers = sorted(Market.check_list(beers), key=lambda drink: drink.title)
        self.drink_titles = set(drink.title for drink in chain(self.wines, self.beers))

    @invocation_logger(lambda name: print(f'Вызвана функция {name} в {datetime.now()}'))
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)
        :param title:
        :return: True|False
        """
        return title in self.drink_titles

    @invocation_logger(lambda name: print(f'Вызвана функция {name} в {datetime.now()}'))
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(chain(self.beers, self.wines), key=lambda drink: drink.title)

    @invocation_logger(lambda name: print(f'Вызвана функция {name} в {datetime.now()}'))
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return list(filter(
            lambda drink: (from_date is None or from_date <= drink.production_date) and
                          (to_date is None or drink.production_date <= to_date),
            chain(self.beers, self.wines)))

    @staticmethod
    def check_list(arg: list):
        return [] if arg is None else arg
