class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drinks = Market.check_list(wines) + Market.check_list(beers)
        self.drink_titles = set(drink.title for drink in self.drinks)

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)
        :param title:
        :return: True|False
        """
        return title in self.drink_titles

    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        # Если список не менялся или менялся незначитально, сортировка займёт O(n) времени
        self.drinks.sort(key=lambda drink: drink.title)
        return self.drinks.copy()

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        if from_date is None and to_date is None:
            return self.drinks.copy()
        if from_date is None:
            def check_date(arg): return arg.production_date <= to_date
        elif to_date is None:
            def check_date(arg): return from_date <= arg.production_date
        else:
            def check_date(arg): return from_date <= arg.production_date <= to_date
        return list(filter(check_date, self.drinks))

    @staticmethod
    def check_list(arg: list):
        return [] if arg is None else arg
