from abc import abstractmethod, ABC
from types import MethodType

# simple proxy

class User(ABC):
    @abstractmethod
    def request(self):
        pass


class RealUser(User):
    def __init__(self, name):
        self.name = name

    def request(self):
        print("%s is requesting something" % self.name)


class Proxy(User):
    def __init__(self, user: User):
        self.user = user

    def request(self):
        self.before()
        self.user.request()
        self.after()

    def before(self):
        print("before")

    def after(self):
        print("after")


# common proxy
class CommonRealUser(User):
    def __init__(self, user, name):
        if user is None:
            raise Exception("cannot create real user!!")
        self.name = name

    def request(self):
        print("%s is requesting something" % self.name)


class CommonProxy(User):
    def __init__(self, name):
        try:
            self.user = CommonRealUser(self, name)
        except Exception as e:
            print(e)
            print("must use a qualified proxy")

    def request(self):
        self.before()
        self.user.request()
        self.after()

    def before(self):
        print("before")

    def after(self):
        print("after")


# Mandatory Proxy
class MDUser(ABC):
    @abstractmethod
    def request(self):
        pass

    @abstractmethod
    def get_proxy(self):
        pass


class MDRealUser(MDUser):
    def __init__(self, name):
        self.name = name
        self.proxy = None

    def request(self):
        if self.__is_proxy__():
            print("%s is requesting something" % self.name)
        else:
            print("Please use assigned proxy")

    def get_proxy(self):
        self.proxy = MDProxy(self)
        return self.proxy

    def __is_proxy__(self):
        return self.proxy is not None and self.proxy.requesting


class MDProxy(MDUser):
    def __init__(self, user):
        self.user = user
        self.requesting = False

    def request(self):
        self.requesting = True
        self.user.request()
        self.requesting = False

    def get_proxy(self):
        return self


# dynamic proxy
class InvocationHandler:
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print("handler:", self.func, args, kwargs)
        return self.func(*args, **kwargs)


class DynamicProxy:
    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = dict()

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print("get attr", item)
        is_exist = hasattr(self.obj, item)
        res = None
        if is_exist:
            res = getattr(self.obj, item)
            if isinstance(res, MethodType):
                if self.handlers.get(res) is None:
                    self.handlers[res] = self.hcls(self.obj, res)
                return self.handlers[res]
            else:
                return res
        return res


class DynamicProxyFactory:
    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise Exception()

    def __call__(self, cls):
        return DynamicProxy(cls, self.hcls)


@DynamicProxyFactory(InvocationHandler)
class Sample:
    def __init__(self, age):
        self.age = age

    def foo(self):
        print("Hello, %d" % self.age)



if __name__ == "__main__":
    # simple proxy
    user = RealUser("Raymond")
    proxy = Proxy(user)
    proxy.request()

    # common proxy
    proxy = CommonProxy("Raymond")
    proxy.request()

    # mandatory proxy
    user = MDRealUser("Raymond")
    proxy = user.get_proxy()
    proxy.request()
    user.request()

    s = Sample(12)
    s.foo()