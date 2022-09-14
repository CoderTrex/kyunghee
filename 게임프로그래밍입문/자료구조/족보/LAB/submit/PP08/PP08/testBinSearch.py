from BinSearch import *


if __name__ == '__main__':


    arr = [1,3, 5, 6, 7, 10, 17, 20]


    item = 13
    
    if  binary_search(arr, item, 0, len(arr) - 1) == True:
        print(f'{item} is in the list.')
    else:
         print(f'{item} is not in the list.')
    

    item = 20
    
    if  binary_search(arr, item, 0, len(arr) - 1) == True:
        print(f'{item} is in the list.')
    else:
         print(f'{item} is not in the list.')    
