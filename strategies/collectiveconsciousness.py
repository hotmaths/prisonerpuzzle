import prisonerlib


NAME = 'Collective Consciousness'

INFO = """
All prisoners are assigned a number from 0-99.

Each day,
- If a prisoner in the room knows that prisoner <day> % 100 has been in the
room, he turns on the light bulb.
- If he says a light bulb on at <day - 1> % 100, then he knows that prisoner
has been in the room.
""".strip()


class Prisoner(prisonerlib.Prisoner):
    def __init__(self, *args, **kwargs):
        super(Prisoner, self).__init__(*args, **kwargs)
        self.__memory = set([self.pid])

    def visit(self, light_bulb, day):
        if light_bulb.on:
            self.__memory.add((day - 1) % prisonerlib.NUM_PRISONERS)
        light_bulb.on = day % prisonerlib.NUM_PRISONERS in self.__memory
        return len(self.__memory) == prisonerlib.NUM_PRISONERS
