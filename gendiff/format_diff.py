def format_diff(diff):
    diff_lines = []
    for key, values in sorted(diff.items()):
        for symbol, value in values.items():
            if isinstance(value, bool):
                value = str(value).lower()
            if isinstance(value, str):
                value = f'{value}'
            diff_lines.append(f'  {symbol} {key}: {value}')

    return '{\n' + '\n'.join(diff_lines) + '\n}'
