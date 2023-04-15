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

    for k in keys:
        key_path = f"{key}.{k}" if key else k

        if k not in obj1:
            diff[k] = {"status": "added", "new_value": obj2[k]}
        elif k not in obj2:
            diff[k] = {"status": "removed", "old_value": obj1[k]}
        elif obj1[k] != obj2[k]:
            if isinstance(obj1[k], dict) and isinstance(obj2[k], dict):
                diff[k] = get_diff(obj1[k], obj2[k], key_path)
            else:
                diff[k] = {"status": "updated", "old_value": obj1[k], "new_value": obj2[k]}

    return diff
