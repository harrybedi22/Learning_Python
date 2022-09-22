"""Array Programs"""

from collections import deque


def add_sum_of_arrays(arry):
    """Python Program to find sum of array"""
    print(sum(arry))

def find_largert_of_array(arry):
    """Python Program to find largest element in an array"""
    print(max(arry))

def rotate_array(arry,num):
    """Program to rotate array using deque"""
    test_lst=deque(arry)
    test_lst.rotate(num)
    print(test_lst)
def rotate_array_usingslicing(arry,num):
    """Program to rotate using slicing"""
    test_lst=arry[num:]+arry[:num]
    
    print(test_lst)

obj = rotate_array_usingslicing([1,7,3,4],2)