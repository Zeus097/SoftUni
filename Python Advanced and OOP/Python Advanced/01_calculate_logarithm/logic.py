from math import log


def calculate_logarithm(number, base=None):
    if base.isdigit():
        return log(number, float(base))
    return log(number)
