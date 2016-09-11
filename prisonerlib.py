NUM_PRISONERS = 100


class LightBulb:
    def __init__(self):
        self.on = False

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, value):
        self.__on = value


class Prisoner:
    def __init__(self, pid):
        self.__pid = pid

    def visit(self, bulb, day):
        raise NotImplementedError

    @property
    def pid(self):
        return self.__pid
