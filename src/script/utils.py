import random


def calculate_value(value_obj):
    _min = value_obj["min"]
    _max = value_obj["max"]
    distribution = value_obj["distribution"]
    if _min == _max:
        return _min
    if distribution == "linear":
        return random.randint(_min, _max)
