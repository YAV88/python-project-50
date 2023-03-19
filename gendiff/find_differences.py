def find_differences(source, target):
    differences = {}

    for key in source:
        if key not in target:
            differences[key] = ('deleted', source[key])
        elif source[key] != target[key]:
            if isinstance(source[key], dict) and isinstance(target[key], dict):
                nested_differences = find_differences(source[key], target[key])
                if nested_differences:
                    differences[key] = nested_differences
            else:
                differences[key] = ('changed', source[key], target[key])

    for key in target:
        if key not in source:
            differences[key] = ('added', target[key])

    return differences
