from math import ceil

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.list_ = collection
        self.num = items_per_page

    def item_count(self):
        return len(self.list_)

    def page_count(self):
        return ceil(len(self.list_)/self.num)

    def page_item_count(self, page_index: int):
        if self.page_count() - 1 < page_index or page_index < 0:
            return -1
        elif not self.item_count() % self.num * (page_index + 1):
            return self.num
        elif page_index  + 1 < self.page_count():
            return self.num
        else:
            return self.item_count() % self.num

    def page_index(self, item_index):
        if self.item_count() <= item_index or item_index < 0:
            return -1
        else:
            return (item_index) // self.num
        

helper = PaginationHelper(['a','b','c','d','e','f', 3, 3], 4)

# print(helper.__dict__)
print('Количество элементов в массиве: ',helper.item_count())
print('Количество страниц: ', helper.page_count())
print('Количество элементов на странице: ', helper.page_item_count(3))
print('Элеметнт расположен на странице: ', helper.page_index(7))