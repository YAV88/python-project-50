def get_diff(obj1, obj2, key=''):
    """
    Recursively finds the differences between two objects
    :param obj1: First object to compare
    :param obj2: Second object to compare
    :param key: Current key during recursive traversal
    :return: Differences between objects
    """
    diff = {}
    keys = set(obj1.keys()) | set(obj2.keys())

    for sorted_key in sorted(keys):
        key_path = f"{key}.{sorted_key}" if key else sorted_key

        if sorted_key not in obj1:
            diff[sorted_key] = {"status": "added", "new_value": obj2[sorted_key]}
        elif sorted_key not in obj2:
            diff[sorted_key] = {"status": "removed", "old_value": obj1[sorted_key]}
        elif obj1[sorted_key] == obj2[sorted_key]:
            diff[sorted_key] = {"status": "unchanged", "old_value": obj1[sorted_key]}
        elif isinstance(obj1[sorted_key], dict) and isinstance(obj2[sorted_key], dict):
            inner_diff = get_diff(obj1[sorted_key], obj2[sorted_key], key_path)
            if inner_diff:
                diff[sorted_key] = {"status": "nested", "children": inner_diff}
        else:
            old_value = obj1[sorted_key]
            new_value = obj2[sorted_key] if obj2[sorted_key] is not None else None
            diff[sorted_key] = {"status": "updated", "old_value": old_value, "new_value": new_value}

    return diff
