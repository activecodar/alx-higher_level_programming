"""
Module that implements peak finding in an unsorted list
"""


def find_peak(list_of_integers):
    """
    A python function that loops through a list of
    unsorted integers and gives a peek when detected

    The algorithm that is used to implement this peak finding function
    algorithm is going to a  binary search algorithm that will have a
    Big O notation complexity of O(log(n))
    """

    integers_list_length = len(list_of_integers)

    if integers_list_length == 0:
        return None

    if integers_list_length == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[integers_list_length - 1] >= \
            list_of_integers[integers_list_length - 2]:
        return list_of_integers[integers_list_length - 1]

    left_side = 1
    right_side = integers_list_length - 2
    while left_side <= right_side:
        midpoint = (left_side + right_side) // 2
        if list_of_integers[midpoint - 1] < list_of_integers[midpoint] > \
                list_of_integers[midpoint + 1]:
            return list_of_integers[midpoint]
        else:
            if list_of_integers[midpoint] < list_of_integers[midpoint + 1]:
                left_side = midpoint + 1
            else:
                right_side = midpoint - 1
