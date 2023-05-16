def format_plain(diff, parent=''):
    """
    Formats the differences between two objects in plain text format
    :param diff: Differences between objects
    :param parent: Parent key during recursive traversal
    :return: Formatted string in plain text format
    """
    lines = []
    for key in sorted(diff.keys()):
        value = diff[key]
        key_path = f"{parent}.{key}" if parent else key

        if isinstance(value, dict):
            if value.get('status') == 'added':
                if isinstance(value.get('new_value'), dict):
                    line = f"Property '{key_path}' " \
                           f"was added with value: [complex value]"
                elif value['new_value'] is None:
                    line = f"Property '{key_path}' " \
                           f"was added with value: null"
                else:
                    line = f"Property '{key_path}' " \
                           f"was added with value: " \
                           f"{format_value(value['new_value'])}"
                if line.strip():
                    lines.append(line)

            elif value.get('status') == 'removed':
                lines.append(f"Property '{key_path}' was removed")

            elif value.get('status') == 'updated':
                old_value = format_value(value['old_value'])
                new_value = format_value(value['new_value'])
                if new_value == 'null':
                    line = f"Property '{key_path}' was updated. " \
                           f"From {old_value} to null"
                else:
                    line = f"Property '{key_path}' was updated. " \
                           f"From {old_value} to {new_value}"
                if line.strip():
                    lines.append(line)

            elif value.get('status') == 'nested':
                nested_lines = format_plain(value['children'], parent=key_path)
                if nested_lines.strip():
                    lines.append(nested_lines)

    return '\n'.join(lines)


def format_value(value):
    """
    Formats the value to be displayed in plain text
    :param value: Value
    :return: Formatted value
    """
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return '[complex value]'
