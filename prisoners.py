#!/usr/bin/env python3
from importlib import import_module
import strategies
import argparse
from prisonerlib import Simulation, STRATEGIES


def main():

    # ARGPARSE
    parser = argparse.ArgumentParser(description='Strategy input.')
    parser.add_argument('strategy', choices=STRATEGIES, help='Enter a strategy.')

    args = parser.parse_args()

    strategy = args.strategy

    mod = import_module('.' + strategy, 'strategies')

    # Create simulation and run it
    s = Simulation(mod)
    s.run()

    # Print Results
    s_max, s_min, s_avg = s.run_times
    print('\n{}:'.format(strategy))
    print('\tRUNS: {}'.format(s.runs))
    print('\tAVG: {:.2f} YEARS'.format(s_avg))
    print('\tMIN: {:.2f} YEARS'.format(s_min))
    print('\tMAX: {:.2f} YEARS'.format(s_max))


main()
