def format_plain(diff, parent=''):
    """
    Formats the differences between two objects in plain text format
    :param diff: Differences between objects
    :param parent: Parent key during recursive traversal
    :return: Formatted string in plain text format
    """
    lines = []
    for key in sorted(diff.keys()):  # Сортировка ключей
        value = diff[key]
        key_path = f"{parent}.{key}" if parent else key
        if isinstance(value, dict):
            if value.get('status') == 'added':
                if isinstance(value.get('new_value'), dict):
                    lines.append(f"Property '{key_path}' was added with value: [complex value]")
                else:
                    lines.append(f"Property '{key_path}' was added with value: {format_value(value['new_value'])}")
            elif value.get('status') == 'removed':
                lines.append(f"Property '{key_path}' was removed")
            elif value.get('status') == 'updated':
                old_value = format_value(value['old_value'])
                new_value = format_value(value['new_value'])
                lines.append(f"Property '{key_path}' was updated. From {old_value} to {new_value}")
            elif isinstance(value, dict):
                nested_lines = format_plain(value, parent=key_path)
                lines.append(nested_lines)
    return '\n'.join(lines)


def format_value(value):
    """
    Форматирует значение для отображения в plain тексте
    :param value: Значение
    :return: Отформатированное значение
    """
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return value
