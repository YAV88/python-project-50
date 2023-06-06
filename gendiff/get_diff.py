def get_diff(obj1, obj2):
    """
    Recursively finds the differences between two objects
    :param obj1: First object to compare
    :param obj2: Second object to compare
    :return: Differences between objects
    """
    diff = {}
    keys = set(obj1.keys()) | set(obj2.keys())

    for keyword in sorted(keys):

        if keyword not in obj1:
            diff[keyword] = {"type": "added", "new_value": obj2[keyword]}
        elif keyword not in obj2:
            diff[keyword] = {"type": "removed",
                             "old_value": obj1[keyword]}
        elif obj1[keyword] == obj2[keyword]:
            diff[keyword] = {"type": "unchanged",
                             "old_value": obj1[keyword]}
        elif isinstance(obj1[keyword], dict) and \
                isinstance(obj2[keyword], dict):
            inner_diff = get_diff(obj1[keyword], obj2[keyword])
            if inner_diff:
                diff[keyword] = {"type": "nested",
                                 "children": inner_diff}
        else:
            old_value = obj1[keyword]
            new_value = obj2[keyword] \
                if obj2[keyword] is not None else None
            diff[keyword] = {"type": "updated",
                             "old_value": old_value,
                             "new_value": new_value}

    return diff
