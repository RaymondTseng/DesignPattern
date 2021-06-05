from abc import abstractmethod, ABCMeta


# Template Mode
class HummerModel(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def engine_boom(self):
        pass

    @abstractmethod
    def alarm(self):
        pass

    def is_alarm(self):
        return True

    def run(self):
        self.start()
        self.engine_boom()
        if self.is_alarm():
            self.alarm()
        self.stop()


class H1Model(HummerModel):
    alarm_flag = True

    def start(self):
        print("H1 start")

    def stop(self):
        print("H1 stop")

    def engine_boom(self):
        print("H1 engine boom boom")

    def alarm(self):
        print("H1 alarm")

    def is_alarm(self):
        return self.alarm_flag

    def set_alarm(self, alarm_flag):
        self.alarm_flag = alarm_flag


if __name__ == "__main__":
    h1 = H1Model()
    h1.set_alarm(False)
    h1.run()