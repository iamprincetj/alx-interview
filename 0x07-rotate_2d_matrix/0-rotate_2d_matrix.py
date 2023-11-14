#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix function
    """
    len_list = len(matrix) - 1
    matrix_copy = matrix.copy()
    new = []
    idx = 0
    matrix.clear()

    for j in range(len(matrix_copy)):
        mylist = []
        while len_list >= 0:
            my_list = matrix_copy[len_list]
            try:
                mylist.append(my_list[idx])
            except IndexError:
                break
            len_list -= 1
        if not len(mylist):
            break
        matrix.append(mylist)
        len_list = len(matrix_copy) - 1
        idx += 1
