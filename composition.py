from abc import abstractmethod, ABC


class Corp(ABC):
    _name = ""
    _position = ""
    _salary = 0

    def __init__(self, _name, _position, _salary):
        self._name = _name
        self._position = _position
        self._salary = _salary

    def get_info(self):
        info = "name: " + self._name
        info = info + "\nposition: " + self._position
        info = info + "\nsalary: %d" + self._salary
        return info


class Leaf(Corp):
    def __init__(self, _name, _position, _salary):
        super().__init__(_name, _position, _salary)


class Branch(Corp):
    subordinate_list = list()

    def __init__(self, _name, _position, _salary):
        super().__init__(_name, _position, _salary)

    def add_subordinate(self, corp):
        self.subordinate_list.append(corp)

    def get_subordinate(self):
        return self.subordinate_list