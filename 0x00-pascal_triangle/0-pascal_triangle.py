#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    mylist = [1]
    mylist1 = [[1]]
    count = 0
    while count != (n-1):
        new_list = [1]
        for i in range(len(mylist) - 1):
            new_val = mylist[i] + mylist[i + 1]
            new_list.append(new_val)
        new_list.append(1)
        mylist1.append(new_list)
        mylist = new_list
        count += 1
    return mylist1