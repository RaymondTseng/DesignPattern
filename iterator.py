from abc import ABC, abstractmethod


# same as the common for...loop


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class ConcreteIterator(Iterator):
    _list = list()

    def __init__(self, _list):
        self._list = _list
        self.cursor = 0

    def has_next(self):
        if self.cursor == len(list):
            return False
        return True

    def next(self):
        res = None
        if self.has_next():
            self.cursor += 1
            res = self._list[self.cursor]
        return res

    def remove(self):
        del self._list[self.cursor]
        return True


class Aggregator(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def iterator(self):
        pass


class ConcreteAggregator(Aggregator):
    _list = list()

    def add(self, obj):
        self._list.append(obj)

    def remove(self, obj):
        self._list.remove(obj)

    def iterator(self):
        return ConcreteIterator(self._list)

