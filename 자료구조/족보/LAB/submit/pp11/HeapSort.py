def reheap_down(elements, root, bottom):
    left_child = root * 2 + 1
    right_child = root * 2 + 2
    if left_child <= bottom:
        if left_child == bottom:
            max_child = left_child
        else:
            if elements[left_child] <= elements[right_child]:
                max_child = right_child
            else:
                max_child = left_child
        if elements[root] < elements[max_child]:
            tmp = elements[root]
            elements[root] = elements[max_child]
            elements[max_child] = tmp
            reheap_down(elements, max_child, bottom)


def heap_sort(values, numValues):
    for i in range(numValues//2 - 1, -1, -1):
        reheap_down(values, i, numValues - 1)
    for i in range(numValues - 1, 0, -1):
        tmp = values[0]
        values[0] = values[i] 
        values[i] = tmp
        reheap_down(values, 0, i - 1)
