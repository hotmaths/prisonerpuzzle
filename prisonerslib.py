PRISONERS_AMOUNT = 100


class Light_bulb:
    def __init__(self):
        self.state = 0

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, num):
        self.__state = num


class Prisoner:
    pass

# SUBCLASSES ARE STRATEGIES
class RingLeader(Prisoner):

    def __init__(self, id_num, has_acted=False, count=1):
        self.__id = id_num
        self.__has_acted = has_acted
        if self.__id == 0:
            self.__role = 1
        else:
            self.__role = 0
        self.__count = count

    def visit(self, bulb, day):
        if self.__role:
            if bulb.state:
                bulb.state = 0
                self.__count += 1
            return self.query_victory()
        else:
            if bulb.state == 0 and not self.__has_acted:
                bulb.state = 1
                self.__has_acted = True
        return False

    def query_victory(self):
        if self.__role:
            if self.__count == PRISONERS_AMOUNT:
                return True
        return False

