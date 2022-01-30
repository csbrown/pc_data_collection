from util import *
from ping import get_ping_time
import functools

def gather_ping_data(how_long_in_s, how_often_in_s, target, headers=None, csv_file=None):
    gather_data(functools.partial(get_ping_time, target), how_long_in_s, how_often_in_s, headers=headers, csv_file=csv_file)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", help="output file", type=str)
    parser.add_argument("timeout", help="how long to gather data in s", type=float)
    parser.add_argument("freq", help="how often to gather data, in Hz", type=float)
    parser.add_argument("target", help="which machine to ping, e.g. lab1-3", type=str)
    args = parser.parse_args()

    gather_ping_data(args.timeout, 1/args.freq, args.target, headers=["time", "ping"], csv_file=(args.output if args.output else None))
