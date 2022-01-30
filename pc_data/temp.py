from util import *
import json

def get_coretemp():
    raw = get_cli_data("sensors -j")
    asdict = json.loads(raw)
    keys = list(asdict.keys())
    coretemp_key = find_str(keys, "coretemp")[0]
    coretemp_dict = asdict[coretemp_key]
    keys = list(coretemp_dict.keys())
    core_keys = find_str(keys, "Core")
    res = []
    for key in sorted(core_keys):
        core_dict = coretemp_dict[key]
        temp_keys = list(core_dict.keys())
        temp_key = find_str(temp_keys, "input")[0]
        res.append(core_dict[temp_key])
    return res

if __name__ == "__main__":
    print(get_coretemp())
