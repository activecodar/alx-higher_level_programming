#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                elements_printed += 1
        print()
    except TypeError:
        print()
        pass
    return elements_printed
