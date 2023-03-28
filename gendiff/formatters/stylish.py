import json


def format_diff_stylish(diff, depth=0, indent_size=4):
    indent = ' ' * depth * indent_size
    lines = []
    for key, value in diff.items():
        if isinstance(value, dict):
            lines.append(f"{indent}  {key}: {{")
            lines.append(format_diff_stylish(value, depth+1, indent_size))
            lines.append(f"{indent}  }}")
        elif isinstance(value, str):
            lines.append(f"{indent}  {key}: {value}")
        else:
            lines.append(f"{indent}  {key}: {json.dumps(value)}")
    if depth == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    else:
        return '\n'.join(lines)
