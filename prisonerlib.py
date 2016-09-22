from pkgutil import iter_modules
from random import choice
import threading
import time
import sys

# generates available strategies for argparse choices
STRATEGIES = [mod[1] for mod in iter_modules(['strategies'])]
NUM_PRISONERS = 100
TIMEOUT = 15  # seconds
RUN_TIME = 3  # seconds


class LightBulb:
    def __init__(self):
        self.on = False

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, value):
        if isinstance(value, bool):
            self.__on = value
        else:
            raise TypeError('LightBulb can only receive bool values')


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

    def __init__(self, mod):
        self.__mod = mod
        self.__run_times = []
        self.__runs = 0
        self.__alive = True

    @property
    def run_times(self):
        return max(self.__run_times) / 365.25, min(self.__run_times) / 365.25,\
               (sum(self.__run_times) / len(self.__run_times)) / 365.25

    @property
    def runs(self):
        return self.__runs

    @staticmethod
    def solved():  # Measures __visited set to total number of prisoners
        if len(Simulation.__visited) == NUM_PRISONERS:
            return True
        else:
            return False

    def simulate(self):

        # build list
        prisoners = []
        try:
            for i in range(NUM_PRISONERS):
                prisoners.append(self.__mod.Prisoner(i))  # STRATEGY
        except:
            self.__alive = False
            raise RuntimeError('Error occurred while building the prisoners list')

        # simulate
        light_bulb = LightBulb()
        days = 0
        victorious = False
        while self.__alive and not victorious:
            prisoner = choice(prisoners)
            Simulation.__visited.add(prisoner.pid)
            try:
                victorious = prisoner.visit(light_bulb, days)  # STRATEGY
            except:
                print("Error in the strategy's visit: {}".format(sys.exc_info()[0]))
            if isinstance(victorious, bool):
                days += 1
            else:
                self.__alive = False
                raise TypeError('Visit can only return bool value')

        # check if solved
        if self.solved():
            self.__run_times.append(days)
        else:
            self.__alive = False

        # add to runs and clear visited set
        self.__runs += 1
        Simulation.__visited.clear()

    def run(self):
        start = time.time()
        while (time.time() - start) < RUN_TIME and self.__alive:
            thread = threading.Thread(target=self.simulate)
            thread.start()
            if self.__runs == 0:
                thread.join(timeout=TIMEOUT)
                if thread.is_alive():
                    self.__alive = False
                    raise TimeoutError('Strategy took longer than allowed')
            else:
                thread.join()
        if not self.__alive:
            print('\n\tSTRATEGY FAILED')
            exit()
