import json


def format_diff(diff, depth=0):
    indent = ' ' * depth * 4
    lines = []
    for key, value in diff.items():
        if isinstance(value, dict):
            lines.append(f"{indent}{key}: {{")
            lines.append(format_diff(value, depth+1))
            lines.append(f"{indent}}}")
        else:
            lines.append(f"{indent}{key}: {json.dumps(value)}")
    return '\n'.join(lines)
