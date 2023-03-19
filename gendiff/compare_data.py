from collections import defaultdict


def compare_data(data1, data2):
    diff = defaultdict(dict)

    for key in data1.keys() | data2.keys():
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key][" "] = data1[key]
            else:
                diff[key]["-"] = data1[key]
                diff[key]["+"] = data2[key]
        elif key in data1:
            diff[key]["-"] = data1[key]
        else:
            diff[key]["+"] = data2[key]

    return diff
