#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        while elements_printed < x:
            print(my_list[elements_printed], end='')
            elements_printed += 1
        print()
    except IndexError:
        print()
        pass
    return elements_printed
