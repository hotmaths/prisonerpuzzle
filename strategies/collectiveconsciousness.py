import prisonerlib


class Prisoner(prisonerlib.Prisoner):
    def __init__(self, *args, **kwargs):
        super(Prisoner, self).__init__(*args, **kwargs)
        self.__memory = set()

    def visit(self, light_bulb, day):
        if light_bulb.on:
            self.__memory.add((day - 1) % prisonerlib.NUM_PRISONERS)
        light_bulb.on = self.pid == day % prisonerlib.NUM_PRISONERS
        return len(self.__memory) == prisonerlib.NUM_PRISONERS
