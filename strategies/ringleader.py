import prisonerlib
from prisonerlib import Light_bulb, PRISONERS_AMOUNT

class Prisoner(prisonerlib.Prisoner):
    def __init__(self, *args, **kwargs):
        super(Prisoner, self).__init__(*args, **kwargs)
        if self.pid:
            self.__has_acted = False
        else:
            self.__count = 1

    def visit(self, bulb, day):
        if self.pid:
            if not bulb.on and not self.__has_acted:
                bulb.on = True
                self.__has_acted = True
        elif bulb.on:
            bulb.on = False
            self.__count += 1
            return self.__count == PRISONERS_AMOUNT
        return False
