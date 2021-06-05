from abc import abstractmethod, ABCMeta
# Simple Factory


class AbstractCar(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class BMW(AbstractCar):
    def describe(self):
        print("I am BMW")


class Mercedes(AbstractCar):
    def describe(self):
        print("I am Mercedes")


class SimpleFactory(object):
    @staticmethod
    def produce_car(class_type):
        return eval(class_type)()


# Factory
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def produce_car(self):
        pass


class BMWFactory(AbstractFactory):
    def produce_car(self):
        return BMW()


class MercedesFactory(AbstractFactory):
    def produce_car(self):
        return Mercedes()


if __name__ == "__main__":
    sf = SimpleFactory()
    bmw = sf.produce_car("BMW")
    bmw.describe()
    mercedes = sf.produce_car("Mercedes")
    mercedes.describe()

