#!/usr/bin/env python3
import argparse
import strategies
import importlib
from prisonerlib import Simulation, STRATEGIES


def run_simulation(mod):
    """Create simulation and run it."""
    s = Simulation(mod)
    s.run()

    # Print Results
    s_max, s_min, s_avg = s.run_times
    print('\n{}:'.format(mod.NAME))
    print('\tRUNS: {}'.format(s.runs))
    print('\tAVG: {:.2f} YEARS'.format(s_avg))
    print('\tMIN: {:.2f} YEARS'.format(s_min))
    print('\tMAX: {:.2f} YEARS'.format(s_max))


def print_info(mod):
    print(mod.NAME)
    print('=' * len(mod.NAME))
    print()
    print(mod.INFO)


def main():
    parser = argparse.ArgumentParser(description='Strategy input.')
    parser.add_argument('-i', '--info', action='store_true',
                        help='Print info on a strategy and exit.')
    parser.add_argument('strategy', choices=STRATEGIES,
                        help='Enter a strategy.')
    args = parser.parse_args()

    mod = importlib.import_module('.{}'.format(args.strategy), 'strategies')
    if args.info:
        print_info(mod)
    else:
        run_simulation(mod)

    exit(0)


if __name__ == '__main__':
    main()
