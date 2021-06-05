from abc import abstractmethod, ABCMeta


class AbstractCar(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class BMW_M3(AbstractCar):
    def describe(self):
        print("I am BMW_M3")


class BMW_X5(AbstractCar):
    def describe(self):
        print("I am BMW_X5")


class Mercedes_C(AbstractCar):
    def describe(self):
        print("I am Mercedes_C")


class Mercedes_G350(AbstractCar):
    def describe(self):
        print("I am Mercedes_G350")


# Factory
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def produce_car(self):
        pass

    @abstractmethod
    def produce_suv(self):
        pass


class BMWFactory(AbstractFactory):
    def produce_car(self):
        return BMW_M3()

    def produce_suv(self):
        return BMW_X5()


class MercedesFactory(AbstractFactory):
    def produce_car(self):
        return Mercedes_C()

    def produce_suv(self):
        return Mercedes_G350()


if __name__ == "__main__":
    bf = BMWFactory()
    bmw = bf.produce_car()
    bmw.describe()
    bmw = bf.produce_suv()
    bmw.describe()