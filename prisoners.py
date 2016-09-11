#!/usr/bin/env python3
import importlib
import strategies
from random import choice
from prisonerlib import Light_bulb, PRISONERS_AMOUNT


def main():

    # TODO: Accept from argument
    strategy_name = 'ringleader'
    mod = importlib.import_module('.' + strategy_name, 'strategies')

    # build list
    prisoners = []
    for i in range(PRISONERS_AMOUNT):
        prisoners.append(mod.Prisoner(i))

    # simulate
    light_bulb = LightBulb()
    day = 0
    while not choice(prisoners).visit(light_bulb, day):
        day += 1

    print('Solved in {:.2f} years.'.format(day / 365.25))


main()
