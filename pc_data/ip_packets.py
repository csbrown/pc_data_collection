from util import *

def get_packets_received():
    raw = get_cli_data("netstat -s")
    packets = raw.split("\n")[2].split()[0]
    return packets

if __name__ == "__main__":
    print(get_packets_received())
