def split(values, first, last):
    piv = values[first]
    left = first
    right = last
    while left < right:
        while left <= last and piv >= values[left]:
            left += 1
        while right > first and piv <= values[right]:
            right -= 1
        if left < right:
            tmp = values[right]
            values[right] = values[left]
            values[left] = tmp
        else:
            values[first] = values[right]
            values[right] = piv
            return right
    return right

def quick_sort(values, first, last):
    if first >= last:
        return
    piv_idx = split(values, first, last)
    quick_sort(values, first, piv_idx-1)
    quick_sort(values, piv_idx+1, last)
    return values
