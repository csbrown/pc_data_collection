from util import *

def get_ping_time(target):
    one_ping = get_cli_data("ping " + target + " -c 1")
    time_data = " ".join(one_ping.split("\n")[1].split()[-2:]).split("=")[-1]
    return time_data

if __name__ == "__main__":
    print(get_ping_time("lab1-24"))
