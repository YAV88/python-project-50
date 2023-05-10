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

    for k in sorted(keys):
        key_path = f"{key}.{k}" if key else k

        if k not in obj1:
            diff[k] = added_diff(obj2[k])
        elif k not in obj2:
            diff[k] = removed_diff(obj1[k])
        else:
            if obj1[k] == obj2[k]:
                diff[k] = {"status": "unchanged", "old_value": obj1[k]}
            elif isinstance(obj1[k], dict) and isinstance(obj2[k], dict):
                inner_diff = get_diff(obj1[k], obj2[k], key_path)
                if inner_diff:
                    diff[k] = {"status": "nested", "children": inner_diff}
            else:
                old_value = obj1[k] if obj1[k] is not None else "null"
                new_value = obj2[k] if obj2[k] is not None else "null"
                diff[k] = updated_diff(old_value, new_value)

    return diff if diff else {}


def added_diff(new_value):
    """
    Creates a diff for an added value
    :param new_value: New value that was added
    :return: Difference object for added value
    """
    return {"status": "added", "new_value": new_value}


def removed_diff(old_value):
    """
    Creates a diff for a removed value
    :param old_value: Old value that was removed
    :return: Difference object for removed value
    """
    return {"status": "removed", "old_value": old_value}


def updated_diff(old_value, new_value):
    """
    Creates a diff for an updated value
    :param old_value: Old value before update
    :param new_value: New value after update
    :return: Difference object for updated value
    """
    return {"status": "updated", "old_value": old_value, "new_value": new_value}
