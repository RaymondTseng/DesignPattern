from abc import abstractmethod, ABCMeta


# Builder Mode
class HummerModel(metaclass=ABCMeta):
    _sequence = list()
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

    def set_sequence(self, sequence):
        self._sequence = sequence.copy()

    def run(self):
        for step in self._sequence:
            if step == "start":
                self.start()
            elif step == "stop":
                self.stop()
            elif step == "engine_boom":
                self.engine_boom()
            elif step == "alarm":
                if self.is_alarm():
                    self.alarm()


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


class AbstractCarBuilder(metaclass=ABCMeta):
    @abstractmethod
    def set_sequence(self, sequence):
        pass

    @abstractmethod
    def get_car_model(self):
        pass


class H1CarBuilder(AbstractCarBuilder):
    h1_car = H1Model()

    def set_sequence(self, sequence):
        self.h1_car.set_sequence(sequence)

    def get_car_model(self):
        return self.h1_car


if __name__ == "__main__":
    h1_car_builder = H1CarBuilder()
    h1_car_builder.set_sequence(["start", "stop"])
    h1_car = h1_car_builder.get_car_model()
    h1_car.run()