def compare_data(obj1, obj2):
    diff = {}
    all_keys = set(obj1.keys()) | set(obj2.keys())
    for key in sorted(all_keys):
        if key in obj1 and key not in obj2:
            diff['-' + ' ' + key] = obj1[key]
        elif key in obj2 and key not in obj1:
            diff['+' + ' ' + key] = obj2[key]
        elif obj1.get(key) != obj2.get(key):
            if isinstance(obj1.get(key), dict) and \
                    isinstance(obj2.get(key), dict):
                diff[key] = compare_data(obj1[key], obj2[key])
            elif obj1.get(key) is None and obj2.get(key) is False:
                diff[' ' + ' ' + key] = obj1.get(key)
            elif obj1.get(key) is False and obj2.get(key) is None:
                diff[' ' + ' ' + key] = obj2.get(key)
            else:
                diff['-' + ' ' + key] = obj1.get(key)
                diff['+' + ' ' + key] = obj2.get(key)
        else:
            diff[' ' + ' ' + key] = obj1.get(key)
    return diff
