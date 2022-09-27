
def short_bubble(values, numValues):
    cur = 0
    sorted = False
    while cur < numValues - 1 and sorted is False:
        bubble_up(values, cur, numValues - 1)
        cur += 1

def bubble_up(values, startIndex, endIndex):
    sorted = True
    for i in range(endIndex, startIndex, -1):
        if values[i] < values[i - 1]:
            tmp = values[i]
            values[i] = values[i - 1]
            values[i - 1] = tmp
            sorted = False
    return sorted
