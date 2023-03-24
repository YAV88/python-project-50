def format_diff(diff):
    diff_lines = [
        "  {} {}: {}".format(symbol, key, str(value).lower() if isinstance(value, bool) else str(value))
        for key, values in sorted(diff.items())
        for symbol, value in values.items()
    ]
    return "{{\n{}\n}}".format("\n".join(diff_lines))
