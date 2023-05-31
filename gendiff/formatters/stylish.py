from collections import namedtuple

Node = namedtuple("Node",
                  ["key", "status", "old_value", "new_value", "children"]
                  )


def format_stylish(diff, depth=0):
    result = []
    for key, node in sorted(diff.items()):
        indent = "  " * depth
        status = node.get("status")
        old_value = node.get("old_value")
        new_value = node.get("new_value")

        if status == "nested":
            result.append(f"  {indent}  {key}: "
                          f"{format_stylish(node['children'], depth+2)}")
        elif status == "added":
            result.append(f"  {indent}+ {key}: "
                          f"{format_value(new_value, depth+2)}")
        elif status == "removed":
            result.append(f"  {indent}- {key}: "
                          f"{format_value(old_value, depth+2)}")
        elif status == "updated":
            result.append(f"  {indent}- {key}: "
                          f"{format_value(old_value, depth+2)}")
            result.append(f"  {indent}+ {key}: "
                          f"{format_value(new_value, depth+2)}")
        else:
            result.append(f"  {indent}  {key}: "
                          f"{format_value(old_value, depth+2)}")

    return "{\n" + "\n".join(result) + "\n" + "  " * depth + "}"


def format_value(value, depth):
    if value is None:
        return "null"
    elif isinstance(value, dict):
        items = []
        for key, node in sorted(value.items()):
            items.append(f"{depth * '  '}    {key}: "
                         f"{format_value(node, depth + 2)}")
        return "{\n" + "\n".join(items) + "\n" + depth * '  ' + "}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == 0:
        return "0"
    return str(value)
