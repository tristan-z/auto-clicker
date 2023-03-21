import random

"""
returns `False` only when `mod` matches `i`
"""
bypass_iteration = lambda _mod, i: bool(_mod and (i % _mod) != 0)


def calculate_itr_count(value_obj):
    _min = value_obj["min"]
    _max = value_obj["max"]
    distribution = value_obj.get("distribution")
    if _min == _max:
        return _min
    match distribution:
        case "linear" | _:
            return random.randint(_min, _max)
