import os
from QueueType import *

if __name__ == '__main__':
    my_queue = QueueType()
    
    for i in range(5):
        number = int(input("enter the number: "))
        my_queue.enqueue(number)
    
    your_queue = QueueType()
    
    for i in range(5):
        number = int(input("enter the number: "))
        your_queue.enqueue(number)
        
    print()
    print(my_queue.is_full())
    print()
    
    while (True):
        if (my_queue.is_empty() == True):
            break
        else:
            print(my_queue.dequeue())
    
    print()
    print(my_queue.is_full())
    print(my_queue.is_empty())
    print()
    print()
    
    
    print(your_queue.is_full())
    print()
    
    your_queue.make_empty()
    
    print(your_queue.is_full())
    print(your_queue.is_empty())

