from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def del_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, context):
        pass


class IHanFeiZi(ABC):
    @abstractmethod
    def have_breakfast(self):
        pass

    @abstractmethod
    def have_fun(self):
        pass


class HanFeiZi(Observable, IHanFeiZi):
    observer_list = list()

    def add_observer(self, observer):
        self.observer_list.append(observer)

    def del_observer(self, observer):
        self.observer_list.remove(observer)

    def notify_observers(self, context):
        for observer in self.observer_list:
            observer.update(context)

    def have_breakfast(self):
        print("HanFeiZi having breakfast")
        self.notify_observers("HanFeiZi having breakfast")

    def have_fun(self):
        print("HanFeiZi having fun")
        self.notify_observers("HanFeiZi having fun")


class Observer(ABC):
    @abstractmethod
    def update(self, context):
        pass


class LiSi(Observer):
    def update(self, context):
        print("update hanfeizi's activity: %s" % context)


if __name__ == "__main__":
    hfz = HanFeiZi()
    lisi = LiSi()
    hfz.add_observer(lisi)
    hfz.have_breakfast()
    hfz.have_fun()