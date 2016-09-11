#!/usr/bin/env python3
import importlib
import strategies
import random
from prisonerlib import LightBulb, NUM_PRISONERS


def main():

    # TODO: Accept from argument
    strategy_name = 'collectiveconsciousness'
    mod = importlib.import_module('.' + strategy_name, 'strategies')

    # build list
    prisoners = []
    for i in range(NUM_PRISONERS):
        prisoners.append(mod.Prisoner(i))

    # simulate
    light_bulb = LightBulb()
    day = 0
    while not random.choice(prisoners).visit(light_bulb, day):
        day += 1

    print('Solved in {:.2f} years.'.format(day / 365.25))


main()
