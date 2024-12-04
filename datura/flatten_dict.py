def flatten_dict(d: dict[str, str | int | dict]) -> dict[str, str | int]:
    """
    Take a nested dictionary d and return a new dictionary with all nested keys
    flattened into a single level.
    The keys in the flattened dictionary should represent the path to each value in the
    original dictionary, joined by dots (.).

    # Example usage:
    nested_dict = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
                'f': 4
            }
        },
        'g': {
            'h': 5
        }
    }

    flattened = flatten_dict(nested_dict)

    print(flattened)

    {
        'a': 1,
        'b.c': 2,
        'b.d.e': 3,
        'b.d.f': 4,
        'g.h': 5
    }
    """

    if not isinstance(d, dict):
        raise ValueError("Input must be a dict")

    result = {}

    for key, value in d.items():
        if not isinstance(key, str):
            raise ValueError("Keys must be strings")

        if isinstance(value, (str | int)):
            result[key] = value
        elif isinstance(value, dict):
            for subkey, subvalue in flatten_dict(value).items():
                result[f"{key}.{subkey}"] = subvalue
        else:
            raise ValueError("Values must be eiter int, strings or dicts")

    return result
