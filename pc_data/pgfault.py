from util import *

def get_pgfaults():
    raw = get_cli_data("grep pgfault /proc/vmstat")
    pgfaults = raw.split()[-1]
    return pgfaults

if __name__ == "__main__":
    print(get_pgfaults())
