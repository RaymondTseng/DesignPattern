# function decorator
def singleton(cls):
    _instance = {}

    def check():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return check


@singleton
class SampleClass1(object):
    def __init__(self):
        pass


sc1 = SampleClass1()
sc2 = SampleClass1()
print(id(sc1) == id(sc2))


# class decorator
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class SampleClass2(object):
    def __init__(self):
        pass


sc3 = SampleClass2()
sc4 = SampleClass2()
print(id(sc3) == id(sc4))


class SampleClass3():
    def __init__(self):
        pass


SampleClass3 = Singleton(SampleClass3)
sc3 = SampleClass3()
sc4 = SampleClass3()
print(id(sc3) == id(sc4))


# using __new__ function
class Single(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


sc5 = Single()
sc6 = Single()
print(id(sc5) == id(sc6))


# using metaclass
# using type to create a class
class Single2(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Single2, self).__call__(*args, **kwargs)
        return self._instances[self]


class SampleClass4(metaclass=Single2):
    def __init__(self):
        pass


sc7 = SampleClass4()
sc8 = SampleClass4()
print(id(sc7) == id(sc8))


# We need to use lock for multi-thread scenario
# Using metaclass case as an example
import threading


class Single3(type):
    _instances = {}
    _instance_lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            with Single3._instance_lock:
                if self not in self._instances:
                    self._instances[self] = super(Single3, self).__call__(*args, **kwargs)
        return self._instances[self]


class SampleClass5(metaclass=Single3):
    def __init__(self):
        pass


def task(arg):
    obj = SampleClass5()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
