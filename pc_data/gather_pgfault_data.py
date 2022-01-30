from util import *
from pgfault import get_pgfaults 
import csv

def gather_pgfault_data(how_long_in_s, how_often_in_s, headers=None, csv_file=None):
    gather_data(get_pgfaults, how_long_in_s, how_often_in_s, headers=headers, csv_file=csv_file)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", help="output file", type=str)
    parser.add_argument("timeout", help="how long to gather data in s", type=float)
    parser.add_argument("freq", help="how often to gather data, in Hz", type=float)
    args = parser.parse_args()
    
    gather_pgfault_data(args.timeout, 1/args.freq, headers=["time", "total_pgfaults"], csv_file=(args.output if args.output else None))

