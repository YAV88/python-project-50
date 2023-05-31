def format_plain(diff, parent=''):
    lines = []
    for key in sorted(diff.keys()):
        value = diff[key]
        key_path = f"{parent}.{key}" if parent else key

        if isinstance(value, dict):
            if value.get('status') == 'added':
                line = f"Property '{key_path}' was added with value: {format_value(value.get('new_value'))}"
                lines.append(line)

            elif value.get('status') == 'removed':
                lines.append(f"Property '{key_path}' was removed")

            elif value.get('status') == 'updated':
                old_value = format_value(value['old_value'])
                new_value = format_value(value['new_value'])
                line = f"Property '{key_path}' was updated. From {old_value} to {new_value}"
                lines.append(line)

            elif value.get('status') == 'nested':
                nested_lines = format_plain(value['children'], parent=key_path)
                lines.append(nested_lines)

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return str(value)
