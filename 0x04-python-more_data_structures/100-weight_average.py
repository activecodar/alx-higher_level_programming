#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    weight_total = sum([i[1] for i in my_list])
    for score, weight in my_list:
        total += score * weight
        weight += weight
    return (total / weight_total)
