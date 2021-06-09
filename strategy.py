from abc import abstractmethod, ABC


class IStrategy(ABC):
    @abstractmethod
    def operate(self):
        pass


class BackDoor(IStrategy):
    def operate(self):
        print("back door strategy")


class GreenLight(IStrategy):
    def operate(self):
        print("green light strategy")


class BlockEnemy(IStrategy):
    def operate(self):
        print("block enemy strategy")


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def operate(self):
        self.strategy.operate()


if __name__ == "__main__":
    strategy = BackDoor()
    context = Context(strategy)
    context.operate()
    strategy = GreenLight()
    context = Context(strategy)
    context.operate()