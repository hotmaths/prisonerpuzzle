#!/usr/bin/env python3
from importlib import import_module
from pkgutil import iter_modules
import strategies
import argparse
from prisonerlib import Simulation, RUNS


# for list argument
def print_strategies():
    temp = iter_modules(['strategies'])
    strategy_list = []
    for each in temp:
        strategy_list.append(each[1])
    return strategy_list


def main():

    # ARGPARSE
    parser = argparse.ArgumentParser(description='Strategy input.')
    parser.add_argument('strategy', choices=print_strategies(), help='Enter a strategy.')

    args = parser.parse_args()

    strategy = args.strategy

    mod = import_module('.' + strategy, 'strategies')

    s = Simulation(strategy, mod)
    s.run()

    s_max, s_min, s_avg = s.run_times

    # print results
    print('\n{}:'.format(strategy))
    print('\tRUNS: {}'.format(RUNS))
    print('\tAVG: {:.2f} YEARS'.format(s_avg))
    print('\tMIN: {:.2f} YEARS'.format(s_min))
    print('\tMAX: {:.2f} YEARS'.format(s_max))


main()
