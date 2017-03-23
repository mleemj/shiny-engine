class SalesItem(object):
    def __init__(self, item, revenue):
        self._item = item
        self._revenue = revenue

    @property
    def item(self):
        return self._item

    @property
    def revenue(self):
        return self._revenue


class SalesItemByAge(object):
    def __init__(self, age):
        self._age = age
        self._list_items = list()

    def add_item(self, sales_item):
        assert isinstance(sales_item, SalesItem)
        self._list_items.append(sales_item)

    @property
    def data_model(self):
        return {self._age: self._list_items}


class SalesStats(SalesItemByAge):
    def __init__(self):
        self._data_model = dict()

    def add_sales_item_age(self, item_age):
        assert isinstance(item_age, SalesItemByAge)
        self._data_model.update(item_age.data_model)

    @property
    def data_model(self):
        return self._data_model
