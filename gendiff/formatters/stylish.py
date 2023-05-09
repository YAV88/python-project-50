def format_stylish(diff, depth=0):
    result = []
    for key, node in sorted(diff.items()):
        status = node.get("status")
        old_value = node.get("old_value")
        new_value = node.get("new_value")
        indent = "  " * depth
        if status == "nested":
            result.append(f"  {indent}  {key}: {format_stylish(node['children'], depth+2)}")
        elif status == "added":
            result.append(f"  {indent}+ {key}: {format_value(new_value, depth+2)}")
        elif status == "removed":
            result.append(f"  {indent}- {key}: {format_value(old_value, depth+2)}")
        elif status == "updated":
            result.append(f"  {indent}- {key}: {format_value(old_value, depth+2)}")
            result.append(f"  {indent}+ {key}: {format_value(new_value, depth+2)}")
        else:  # status == "unchanged"
            result.append(f"  {indent}  {key}: {format_value(old_value, depth+2)}")
    return "{\n" + "\n".join(result) + "\n" + "  " * depth + "}"


def format_value(value, depth):
    if isinstance(value, dict):
        items = []
        for key, node in sorted(value.items()):
            items.append(f"{depth * '  '}    {key}: {format_value(node, depth + 2)}")
        return "{\n" + "\n".join(items) + "\n" + depth * '  ' + "}"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
