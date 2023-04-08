def value_to_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def compare_data(obj1, obj2, path=''):
    diff = []
    all_keys = set(obj1.keys()) | set(obj2.keys())
    for key in sorted(all_keys):
        new_path = f'{path}.{key}' if path else key
        if key in obj1 and key not in obj2:
            diff.append(f"Property '{new_path}' was removed")
        elif key in obj2 and key not in obj1:
            if isinstance(obj2[key], dict):
                diff += compare_data({}, obj2[key], new_path)
            else:
                diff.append(f"Property '{new_path}' was added with value: "
                            f"{value_to_string(obj2[key])}")
        elif obj1.get(key) != obj2.get(key):
            if isinstance(obj1.get(key), dict) and \
                    isinstance(obj2.get(key), dict):
                diff += compare_data(obj1[key], obj2[key], new_path)
            elif obj1.get(key) is None and obj2.get(key) is False:
                diff.append(f"Property '{new_path}' was updated. "
                            f"From {obj1.get(key)} to {obj2.get(key)}")
            elif obj1.get(key) is False and obj2.get(key) is None:
                diff.append(f"Property '{new_path}' was updated. "
                            f"From {obj1.get(key)} to {obj2.get(key)}")
            else:
                diff.append(f"Property '{new_path}' was updated. "
                            f"From {value_to_string(obj1.get(key))} to "
                            f"{value_to_string(obj2.get(key))}")
        else:
            if isinstance(obj1.get(key), dict) and \
                    isinstance(obj2.get(key), dict):
                diff += compare_data(obj1[key], obj2[key], new_path)
            else:
                pass
    return diff
