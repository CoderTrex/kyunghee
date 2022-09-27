from logging import RootLogger
from statistics import median_grouped
from turtle import right


def merge_sort(values, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort(values, first, middle)
        merge_sort(values, middle + 1, last)
        merge(values, first, middle, middle + 1, last)
    

def merge(values, leftFirst, leftLast, rightFirst, rightLast):
    saveFirst = leftFirst
    tmp = []
    
    while leftFirst <= leftLast and rightFirst <= rightLast:
        if values[leftFirst] < values[rightFirst]:
            tmp.append(values[leftFirst])
            leftFirst += 1
        else:
            tmp.append(values[rightFirst])
            rightFirst += 1

    while leftFirst <= leftLast:
        tmp.append(values[leftFirst])
        leftFirst += 1

    while rightFirst <= rightLast:
        tmp.append(values[rightFirst])
        rightFirst += 1
    for i in range(saveFirst, rightLast + 1, 1):
        values[i] = tmp[i - saveFirst]
