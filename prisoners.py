#!/usr/bin/env python3
import random
from prisonerslib import Light_bulb, RingLeader, PRISONERS_AMOUNT


def main():

    # build list
    prisoners = []
    for i in range(PRISONERS_AMOUNT):
        # CREATE PRISONERS WITH YOUR STRATEGY HERE
        p = RingLeader(i)
        prisoners.append(p)

    # simulate
    light_bulb = Light_bulb()
    day = 0
    while not random.choice(prisoners).visit(light_bulb, day):
        day += 1

    print('Solved in {:.2f} years.'.format(day / 365.25))


main()
