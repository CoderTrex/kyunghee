from BubbleSort import *
from SelectionSort import *
from InsertionSort import *
from MergeSort import *
from QuickSort import *
from HeapSort import *
from ShortBubble import *

if __name__ == '__main__':
    arr = [8,5,4,6,2]
    bubble_sort(arr)
    print(arr)

    arr = [8,5,4,6,2]
    selection_sort(arr)
    print(arr)

    arr = [8,5,4,6,2]
    insertion_sort(arr)
    print(arr)

    arr = [8,5,4,6,2]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)

    arr = [8,5,4,6,2]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

    arr = [8,5,4,6,2]
    heap_sort(arr, len(arr))
    print(arr)

    arr = [8,5,4,6,2]
    short_bubble(arr, len(arr))
    print(arr)
