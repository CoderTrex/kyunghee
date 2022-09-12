from QuickSort1 import *


if __name__ == '__main__':
    arr01 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    arr02 = [1, 8, 5, 7, 3, 2, 6, 4, 9]

    print("Before")
    print(arr01)
    print("After")
    print(quick_sort(arr01, 0, len(arr01) - 1))

    print("\nBefore")
    print(arr02)
    print("After")
    print(quick_sort(arr02, 0, len(arr02) - 1))
