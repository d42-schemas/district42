import re


def check_type(value, expected_types):
    for expected_type in expected_types:
        if isinstance(value, expected_type):
            return None
    if len(expected_types) == 2:
        message = 'Value "{value}" must be an instance of {type1} or {type2}, instance of {actual_type} given'
    elif len(expected_types) == 1:
        message = 'Value "{value}" must be an instance of {type1}, instance of {actual_type} given'
    else:
        message = 'Value "{value}" must be an instance of {types}, instance of {actual_type} given'
    return message.format(
        value=value,
        type1=expected_types[0],
        type2=expected_types[-1],
        types=tuple(expected_types),
        actual_type=type(value)
    )


def check_types(values, expected_types):
    for value in values:
        error = check_type(value, expected_types)
        if error:
            return error
    return None


def roll_out(keys):
    new_keys = {}
    for composite_key, val in keys.items():
        parts = re.split(r'(?<!\\)\.', composite_key) if isinstance(composite_key, str) else [composite_key]
        key = parts[0]
        if len(parts) == 1:
            new_keys[key] = val
        else:
            new_composite_key = '.'.join(parts[1:])
            if key not in new_keys:
                new_keys[key] = {}
            new_keys[key][new_composite_key] = val
    return {k: (roll_out(v) if type(v) is dict else v) for k, v in new_keys.items()}
