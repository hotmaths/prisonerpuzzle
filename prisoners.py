from random import randint

PRISONER_COUNT = 100
TIME = 10000 # for limits

class Prisoner:
    def __init__(self, wait=0, visits=0, has_acted=False):
        self.wait = wait
        self.visits = visits
        self.has_acted = has_acted

    # WAIT ----------------------
    @property
    def wait(self):
        return self.__wait

    @wait.setter
    def wait(self, days):
        self.__wait = days

    # VISITS ---------------------
    @property
    def visits(self):
        return self.__visits

    @visits.setter
    def visits(self, num):
        self.__visits = num

    # HAS_ACTED ------------------
    @property
    def has_acted(self):
        return self.__has_acted

    @has_acted.setter
    def has_acted(self, bool):
        self.__has_acted = bool


    # DUTY (CUSTOMIZE LATER)-------------------
    def duty(self, bulb):
        if bulb == 0 and not self.has_acted:
            bulb = 1
            self.has_acted = True
        return bulb

    # MUTATORS ---------------------
    def decrement_wait(self):
        self.__wait -= 1

    def increment_visits(self):
        self.__visits += 1



class Leader(Prisoner):
    def __init__(self, wait=0, visits=0, count=1):
        self.wait = wait
        self.visits = visits
        self.count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, num):
        self.__count = num

    def duty(self, bulb):
        if bulb == 1:
            bulb = 0
            self.__count += 1
        return bulb

def main():

    # generates prisoner list
    prisoner_list = []
    leader_count = 1
    for i in range(PRISONER_COUNT):
        if leader_count:
            prisoner = Leader()
            leader_count -= 1
        else:
            prisoner = Prisoner()
        prisoner_list.append(prisoner)

    leader = prisoner_list[0]

    light_bulb = 0
    days = 0
    while leader.count < PRISONER_COUNT:
        prisoner = prisoner_list[randint(0, PRISONER_COUNT - 1)]
        prisoner.increment_visits()
        light_bulb = prisoner.duty(light_bulb)
        days += 1

    visit_total = 0
    for p in prisoner_list:
        if isinstance(p, Leader):
            print('Leader counted:', p.count)
        visit_total += p.visits
    print('Average visits:', visit_total / PRISONER_COUNT)
    print('Days passed:', days)


main()