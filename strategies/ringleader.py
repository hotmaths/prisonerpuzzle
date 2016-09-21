import prisonerlib


NAME = 'Ringleader'

INFO = """
All prisoners are given a value of 1.
One prisoner is chosen as the leader.

For the leader:
- If the light is off, they leave.
- If the light is on, they turn it off and increase their value by one.
- If their count reaches 100, they declare victory.

For all others:
- If the light is off and they have a value of 1, they turn the light on and
  change their value to 0.
- If the light is on, they leave it on.
""".strip()


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
            return self.__count == prisonerlib.NUM_PRISONERS
        return False
