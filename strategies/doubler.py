import math
import prisonerlib


CYCLES = int(math.log2(prisonerlib.NUM_PRISONERS))
MAX_DOUBLE = 2 ** CYCLES
WINDOW = 5 * prisonerlib.NUM_PRISONERS


print('CYCLES', CYCLES)
print('MAX_DOUBLE', MAX_DOUBLE)
print('WINDOW', WINDOW)


def day_value(day):
    return 2 ** ((day // WINDOW) % CYCLES)


class Prisoner(prisonerlib.Prisoner):
    def __init__(self, *args, **kwargs):
        super(Prisoner, self).__init__(*args, **kwargs)
        self.__value = 1

    def __is_boss(self):
        return self.__value >= MAX_DOUBLE

    def __is_double(self):
        return self.__value and not math.log2(self.__value) % 1

    def __give(self, light_bulb, day):
        today_value = day_value(day)
        assert(light_bulb.on == False)
        assert(self.__value >= today_value)
        light_bulb.on = True
        self.__value -= today_value

    def __take(self, light_bulb, day):
        yesterday_value = day_value(day - 1)
        assert(light_bulb.on == True)
        light_bulb.on = False
        self.__value += yesterday_value

    def visit(self, light_bulb, day):
        today_value = day_value(day)
        action = 'N'
        if light_bulb.on:
            yesterday_value = day_value(day - 1)
            if (self.__value == yesterday_value      # We can double
                or self.__is_boss()                  # We are taking over
                or today_value != yesterday_value):  # Have to grab
                self.__take(light_bulb, day)
        elif (self.__value == today_value  # We can offer a double
              or (not self.__is_double()   # Break up a non-double
                  and not self.__is_boss()
                  and self.__value >= today_value)):
            self.__give(light_bulb, day)
        return self.__value == prisonerlib.NUM_PRISONERS
