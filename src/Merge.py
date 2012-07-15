'''
Created on 15.7.2012

@author: salama
'''
import HighScore

def mergesort(listitem):
    if len(listitem) < 2:
        return listitem
    middle = int(len(listitem) / 2)
    left = mergesort(listitem[:middle])
    right = mergesort(listitem[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i , j = 0, 0
    while i < len(left) and j < len(right):
        if HighScore.compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
