def bubble_up(values, start: int, end: int):
    for i in range(end, start - 1, -1):
        if values[i] < values[i - 1]:
            tmp = values[i]
            values[i] = values[i - 1]
            values[i - 1] = tmp


def bubble_sort(values):
    l = len(values)
    for i in range(0, l - 1, 1):
        bubble_up(values, i, l - 1)
