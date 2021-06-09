class Target:
    def request(self):
        print("target function")


class Adaptee:
    def specific_request(self):
        print("adaptee function")


class Adapter(Target, Adaptee):
    def request(self):
        print("adapter function")