class Wine:
    def __init__(self, title=None, production_date=None) -> None:
        # TODO: добавить инициализацию
        self.title = title
        self.production_date = production_date

    def __hash__(self):
        return hash((self.title, self.production_date))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.title == other.title and self.production_date == other.production_date
