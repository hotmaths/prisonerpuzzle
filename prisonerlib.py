NUM_PRISONERS = 100
RUNS = 10


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
        # all work must be in visit function
        raise NotImplementedError

    @property
    def pid(self):
        return self.__pid


class Simulation:
    __visited = set()

    def __init__(self, prisoner_class, mod):
        self.__prisoner_class = prisoner_class
        self.__mod = mod
        self.__run_times = []

    @property
    def run_times(self):
        return max(self.__run_times) / 365.25, min(self.__run_times) / 365.25,\
               (sum(self.__run_times) / len(self.__run_times)) / 365.25

    @staticmethod
    def solved():
        if len(Simulation.__visited) == NUM_PRISONERS:
            return True
        else:
            return False

    def simulate(self):

        from random import choice

        # build list
        prisoners = []
        for i in range(NUM_PRISONERS):
            prisoners.append(self.__mod.Prisoner(i))

        # simulate
        light_bulb = LightBulb()
        days = 0
        victorious = False
        while not victorious:
            prisoner = choice(prisoners)
            Simulation.__visited.add(prisoner.pid)
            victorious = prisoner.visit(light_bulb, days)
            days += 1

        # check if actually solved before assigning
        if self.solved():
            self.__run_times.append(days)
        else:
            print('A test failed.')
            exit()

    def run(self):
        for i in range(RUNS):
            self.simulate()
