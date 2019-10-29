import math

def simpson_method(values, delta_h):
    if len(values) > 3:
        total = sum([4*x if ind % 2 == 0 else 2*x for ind, x in enumerate(values[1:-1])]) \
            + values[0] + values[-1]
    else:
        total = sum(values) + values[1] * 3

    return f'{delta_h * total / 3 : .4f}'

def trapeziodal_rule(values, delta_h):

    if len(values) > 2:   
        total = sum([2*x for x in values[1:-1]]) + values[0] + values[-1]
    else:
        total = values[1] + values[-1]

    return f'{delta_h * total / 2 : .4f}'

# print(trapeziodal_rule([0, 0.25, 0.75, 1, 0.75, 0.25, 0], math.pi/6))
# print(simpson_method([0, 0.25, 0.75, 1, 0.75, 0.25, 0], math.pi/6))
