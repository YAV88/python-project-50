def format_plain(diff, parent=''):
    lines = []
    for key in sorted(diff.keys()):
        value = diff[key]
        key_path = f"{parent}.{key}" if parent else key

        if isinstance(value, dict) and value.get('status') == 'added':
            if isinstance(value.get('new_value'), dict):
                line = (
                    f"Property '{key_path}' was added with value: "
                    f"[complex value]"
                )
            elif value['new_value'] is None:
                line = f"Property '{key_path}' was added with value: null"
            else:
                line = (
                    f"Property '{key_path}' was added with value: "
                    f"{format_value(value['new_value'])}"
                )
            lines.append(line)

        elif isinstance(value, dict) and value.get('status') == 'removed':
            lines.append(f"Property '{key_path}' was removed")

        elif isinstance(value, dict) and value.get('status') == 'updated':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            line = (
                f"Property '{key_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
            lines.append(line)

        elif isinstance(value, dict) and value.get('status') == 'nested':
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
