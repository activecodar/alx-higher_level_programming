#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_lst = [False] * len(my_list)

    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            final_lst[idx] = True
    return final_lst
