def split(values, first, last):
    if first >= last:
        return -1
    p = values[first]
    left = first + 1
    right = last

    while left < right:
        while left <= last and values[left] <= p:
            left += 1
        while right > first and values[right] >= p:
            right -= 1
        if left > right:
            values[first] = values[right]
            values[right] = p
        else:
            tmp = values[left]
            values[left] = values[right]
            values[right] = tmp
    return right

    
def quick_sort(values, first, last):
    if first < last:
        s = split(values, first, last)
        if s == -1:
            return
        quick_sort(values, first, s - 1)
        quick_sort(values, s + 1, last)
