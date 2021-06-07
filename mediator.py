from abc import abstractmethod, ABC
import random


class AbstractMediator(ABC):
    def __init__(self):
        self.purchase = Purchase(self)
        self.stock = Stock(self)
        self.sale = Sale(self)

    @abstractmethod
    def execute(self, command, *args):
        pass


class AbstractCollege(ABC):
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator


class Purchase(AbstractCollege):
    def __init__(self, mediator):
        super().__init__(mediator)

    def buy_IBM_computer(self, number):
        self.mediator.execute("purchase.buy", number)

    def refuse_buy_IBM(self):
        print("No longer to buy IBM computers.")


class Stock(AbstractCollege):
    COMPUTER_NUMBER = 100
    def __init__(self, mediator):
        super().__init__(mediator)

    def increase(self, number):
        self.COMPUTER_NUMBER += number
        print("The stock becomes %d" % self.COMPUTER_NUMBER)

    def decrease(self, number):
        self.COMPUTER_NUMBER -= number
        print("The stock becomes %d" % self.COMPUTER_NUMBER)

    def get_stock_number(self):
        return self.COMPUTER_NUMBER

    def clear_stock(self):
        print("Clear stock %d" % self.COMPUTER_NUMBER)
        self.mediator.execute("stock.clear")


class Sale(AbstractCollege):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.mediator = mediator

    def sell_IBM_computer(self, number):
        self.mediator.execute("sale.sell", number)
        print("Sell IBM computer %d" % number)

    def get_sale_status(self):
        sale_status = random.randint(0, 100)
        print("IBM computer sale status %d" % sale_status)
        return sale_status

    def off_sale(self):
        self.mediator.execute("sale.offsale")


class Mediator(AbstractMediator):
    def __init__(self):
        super().__init__()

    def execute(self, command, *args):
        if command == "purchase.buy":
            self.__buy_computer__(args[0])
        elif command == "sale.sell":
            self.__sell_computer__(args[0])
        elif command == "stock.clear":
            self.clear_stock()
        elif command == "sale.offsale":
            self.__off_sale__()

    def __buy_computer__(self, number):
        sale_status = self.sale.get_sale_status()
        if sale_status > 80:
            print("Purchase %d computers" % number)
        else:
            number /= 2
            print("Purchase %d computers" % number)
        self.stock.increase(number)

    def __sell_computer__(self, number):
        if self.stock.get_stock_number() < number:
            self.purchase.buy_IBM_computer(number)
        self.stock.decrease(number)

    def __off_sale__(self):
        print("Off sale %d computers" % self.stock.get_stock_number())

    def clear_stock(self):
        self.sale.off_sale()
        self.purchase.refuse_buy_IBM()


if __name__ == "__main__":
    mediator = Mediator()
    print("------------ Purchase Computer ------------")
    purchase = Purchase(mediator)
    purchase.buy_IBM_computer(100)
    print("------------ Sell Computer ------------")
    Sale = Sale(mediator)
    Sale.sell_IBM_computer(1)
    print("------------ Clear Stock ------------")
    stock = Stock(mediator)
    stock.clear_stock()
