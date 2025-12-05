class Unique:
    def __init__(self, items, ignore_case=False):
        self.items = list(items)
        self.ignore_case = ignore_case
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

    def reset(self):
        self.unq.clear()
        self.index = 0

