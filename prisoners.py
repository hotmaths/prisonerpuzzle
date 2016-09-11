from random import randint
PRISONERS_AMOUNT = 100


class Prisoner:

    def wait(self):
        return NotImplementedError

    def visit(self):
        return NotImplementedError


# SUBCLASSES ARE STRATEGIES
class RingLeader(Prisoner):
    count_for_ID = 0

    def __init__(self, has_acted=False, count=1):
        self.__id = RingLeader.count_for_ID
        RingLeader.count_for_ID += 1
        self.__has_acted = has_acted
        if self.__id == 0:
            self.__role = 1
        else:
            self.__role = 0
        self.__count = count

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, count):
        self.__id = count

    @property
    def has_acted(self):
        return self.__has_acted

    @has_acted.setter
    def has_acted(self, bool):
        self.__has_acted = bool

    @property
    def role(self):
        return self.__role

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, num):
        self.__count = num

    def duty(self, bulb, day):
        if self.role:
            if bulb == 1:
                bulb = 0
                self.__count += 1
            return bulb
        else:
            if bulb == 0 and not self.__has_acted:
                bulb = 1
                self.__has_acted = True
            return bulb

    def query_victory(self):
        if self.role:
            if self.__count == PRISONERS_AMOUNT:
                return True
        return False


def main():

    # build list
    prisoner_list = []
    for i in range(PRISONERS_AMOUNT):
        # CREATE PRISONERS WITH YOUR STRATEGY HERE
        p = RingLeader()
        prisoner_list.append(p)

    victory = False
    light_bulb = 0
    days = 0
    while not victory:
        random_prisoner = prisoner_list[randint(0, PRISONERS_AMOUNT - 1)]
        light_bulb = random_prisoner.duty(light_bulb, days)
        victory = random_prisoner.query_victory()
        days += 1
    print("Solved in ", days, 'days.')


main()
