#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <time.h>

using namespace std;

template <class ItemType >
int MinIndex(ItemType values [ ], int start, int end)
{
    int indexOfMin = start ;
    for(int index = start + 1 ; index <= end ; index++)
        if (values[ index] < values [indexOfMin])
            indexOfMin = index ;
    return indexOfMin;
}



template <class ItemType >
void SelectionSort (ItemType values[ ], int numValues )
{
    int endIndex = numValues - 1 ;
    for (int current = 0 ; current < endIndex; current++)
        swap(values[current], values[MinIndex(values, current, endIndex)]);
}


template<class itemtype>
void BubbleSort(itemtype value[], int numValue)
{
    int current = 0;
    while (current < numValue - 1)
    {
        BubbleUp(value, current, numValue - 1);
        current++;
    }
}



template<class itemtype>
void BubbleUp(itemtype value[], int startIndex, int endIndex)
{
    for (int index = endIndex; index > startIndex; index--)
    {
        if (value[index] < value[index - 1])
            swap(value[index], value[index - 1]);
    }
}


template<class itemtype>
void InsertItem(itemtype value[], int start, int end)
{
    bool finished = false;
    int current = end;
    bool moreToSearch = (current != end);
    while (moreToSearch && !finished)
    {
        if (value[current] < value[current - 1])
        {
            swap(value[current], value[current - 1]);
            current--;
            moreToSearch = (current != start);
        }
        else
            finished = true;
    }
    
}

template <class ItemType >
void HeapSort ( ItemType values [ ] , int
numValues )
{
int index ;
    for (index = numValues/2 - 1; index >= 0; index--)
    ReheapDown ( values , index , numValues - 1 ) ;
    // N개 가짓수
    for (index = numValues - 1; index >= 1; index--)
    {
        // logN의 수
        Swap (values [0] , values[index]);
        ReheapDown (values , 0 , index - 1);
    }
}


















































void print_unsort(){
    srand(time(NULL));
    int *arr, random_n;
    arr = (int*)malloc(sizeof(10));
    cout << "random arr: ";
    for (int i =  0; i < 10; i++){
        random_n = rand() % 10;
        cout << random_n << " ";
        arr[i] = random_n;
    }
    cout << "\n";
    SelectionSort(arr, 10);
    cout << "sorted arr: ";
    for (int i =  0; i < 10; i++){
        cout << arr[i] << " ";
    }
}

void print_bubble(){
    srand(time(NULL));
    int *arr, random_n;
    arr = (int*)malloc(sizeof(10));
    cout << "random arr: ";
    for (int i =  0; i < 10; i++){
        random_n = rand() % 10;
        cout << random_n << " ";
        arr[i] = random_n;
    }
    cout << "\n";
    SelectionSort(arr, 10);
    cout << "sorted arr: ";
    for (int i =  0; i < 10; i++){
        cout << arr[i] << " ";
    }
}

int main()
{
    print_unsort();
}