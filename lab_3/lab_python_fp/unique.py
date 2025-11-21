class Unique:
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.unq = set()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.unq:
                self.unq.add(key)
                return item
        raise StopIteration

# data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# print(list(Unique(data)))
#
# data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# print(list(Unique(data)))
# print(list(Unique(data, ignore_case=True)))