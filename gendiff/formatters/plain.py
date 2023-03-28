def format_diff_plain(diff, parent_key=''):
    lines = []
    for key, value in diff.items():
        if isinstance(value, dict):
            nested_parent_key = f"{parent_key}.{key}" if parent_key else key
            lines.append(format_diff_plain(value, nested_parent_key))
        else:
            if value is None:
                value = 'null'
            elif value is True:
                value = 'true'
            elif value is False:
                value = 'false'
            nested_key = f"{parent_key}.{key}" if parent_key else key
            lines.append(f"Property '{nested_key}' was {value}")
    return '\n'.join(lines)
