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

    for keyword in sorted(keys):
        key_path = f"{key}.{keyword}" if key else keyword

        if keyword not in obj1:
            diff[keyword] = {"status": "added", "new_value": obj2[keyword]}
        elif keyword not in obj2:
            diff[keyword] = {"status": "removed",
                             "old_value": obj1[keyword]}
        elif obj1[keyword] == obj2[keyword]:
            diff[keyword] = {"status": "unchanged",
                             "old_value": obj1[keyword]}
        elif isinstance(obj1[keyword], dict) and \
                isinstance(obj2[keyword], dict):
            inner_diff = get_diff(obj1[keyword],
                                  obj2[keyword], key_path)
            if inner_diff:
                diff[keyword] = {"status": "nested",
                                 "children": inner_diff}
        else:
            old_value = obj1[keyword]
            new_value = obj2[keyword] \
                if obj2[keyword] is not None else None
            diff[keyword] = {"status": "updated",
                             "old_value": old_value,
                             "new_value": new_value}

    return diff
