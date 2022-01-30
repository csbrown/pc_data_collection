import subprocess
import time
import csv

def flatten(list_of_list):
    if isinstance(list_of_list, list):
        return sum([flatten(item) for item in list_of_list], [])
    return [list_of_list]

def gather_over_time(f, how_long_in_s, how_often_in_s):
    current = time.time()
    end = current + how_long_in_s
    data = []
    while end - current > 0:
        current = time.time()
        data.append(flatten([current, f()]))
        time.sleep(how_often_in_s)
    return data

def find_str(list_of_str, search_str):
    res = []
    for string in list_of_str:
        if search_str in string:
            res.append(string)
    return res

def get_cli_data(command):
    return subprocess.check_output(command.split()).decode("utf-8")

def gather_data(row_function, how_long_in_s, how_often_in_s, headers=None, csv_file=None):
    data = gather_over_time(row_function, how_long_in_s, how_often_in_s)
    if headers is not None:
        data = [headers] + data
    if csv_file is not None:
        with open(csv_file, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    else:
        print(data)
