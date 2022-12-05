#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        mx = my_list[0]

    for idx in range(1, len(my_list)):
        if my_list[idx] > mx:
            mx = my_list[idx]
    return mx
