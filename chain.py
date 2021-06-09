from abc import abstractmethod, ABC
import random


class Handler(ABC):
    FATHER_LEVEL = 0
    HUSBAND_LEVEL = 1
    SON_LEVEL = 2

    def __init__(self, level):
        self._level = level
        self.next_handler = None

    def handle_message(self, women):
        if women.get_type() == self._level:
            self.response(women)
        elif self.next_handler is None:
            print("No next handler, disagree")
        else:
            self.next_handler.handle_message(women)

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    @abstractmethod
    def response(self, women):
        pass


class Father(Handler):
    def __init__(self):
        super().__init__(Handler.FATHER_LEVEL)

    def response(self, women):
        print("daughter's request: %s" % women.get_request())
        print("father's response: agree")


class Husband(Handler):
    def __init__(self):
        super().__init__(Handler.HUSBAND_LEVEL)

    def response(self, women):
        print("Wife's request: %s" % women.get_request())
        print("husband's response: agree")


class Son(Handler):
    def __init__(self):
        super().__init__(Handler.SON_LEVEL)

    def response(self, women):
        print("Mother's request: %s" % women.get_request())
        print("son's response: agree")


class IWomen(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_request(self):
        pass


class Women(IWomen):
    def __init__(self, _type, _request):
        self._type = _type
        self._request = _request
        if _type == 1:
            print("Daughter's request: %s" % _request)
        elif _type == 2:
            print("Wife's request: %s" % _request)
        elif _type == 3:
            print("Mother's request: %s" % _request)

    def get_type(self):
        return self._type

    def get_request(self):
        return self._request


if __name__ == "__main__":
    all_women = [Women(random.randint(1, 4), "hang out") for _ in range(5)]
    father = Father()
    husband = Husband()
    son = Son()
    father.set_next_handler(husband)
    husband.set_next_handler(son)
    for women in all_women:
        father.handle_message(women)



