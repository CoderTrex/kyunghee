#include <iostream>
using namespace std;

// Case_one :
// 찾으면    : 수 반환
// 못 찾으면 : -1 반환
int  BinarySearch_1(int array[], int sizeOfArray, int value){
    int first = 0;
    int last = sizeOfArray - 1;
    int midpoint;
    int result = -1;
    bool check_one = true;
    bool check_two = (first < last);

    // found = check_one 
    // moreToSearch = check_two
    while (check_one && check_two){
        midpoint = first + last;
        if (array[midpoint] > value){
            last = midpoint - 1;
            check_two = (first < last);
        }
        else if (array[midpoint] < value){
            first = midpoint + 1;
            check_two = (first < last);
        }
        else if (array[midpoint] == value){
            result = array[midpoint];
            check_one = false;
            break;
        }
    }  
    return result;  
}

// Case_two :
// 찾으면  : 해당 수 반환
// 못찾으면 : 그 수보다 작은 가장 가까운 수 출력
// 만약에 찾으려는 수가 array의 수보다 전부 크면 -1을 출력함.
int  BinarySearch_2(int array[], int sizeOfArray, int value){
    int first = 0;
    int last = sizeOfArray - 1;
    int midpoint;
    int result = -1;
    bool check_one = true;
    bool check_two = (first < last);

    while (check_one && check_two){
        midpoint = first + last;
        if (array[midpoint] > value){
            last = midpoint - 1;
            check_two = (first < last);
        }
        else if (array[midpoint] < value){
            first = midpoint + 1;
            check_two = (first < last);
        }
        else if (array[midpoint] == value){
            result = array[midpoint];
            return result;
        }
    }
    if (value > array[last]){
        return array[last]; 
    }
    return result;  
}

// Case_three :
// 찾으면  : 해당 수 반환
// 못찾으면 : 그 수보다 큰 가장 가까운 수 출력
// 만약에 찾으려는 수가 array의 수보다 전부 작으면 -1을 출력함.

int  BinarySearch_3(int array[], int sizeOfArray, int value){
    int first = 0;
    int last = sizeOfArray - 1;
    int midpoint;
    int result = -1;
    bool check_one = true;
    bool check_two = (first < last);

    // found = check_one 
    // moreToSearch = check_two
    while (check_one && check_two){
        midpoint = first + last;
        if (array[midpoint] > value){
            last = midpoint - 1;
            check_two = (first < last);
        }
        else if (array[midpoint] < value){
            first = midpoint + 1;
            check_two = (first < last);
        }
        else if (array[midpoint] == value){
            result = array[midpoint];
            return result;
        }
    }
    if (value < array[first])
        return array[first];
    return result;  
}





int main()
{
    // 1 6 9
    int list[10] = {2,3,4,5,7,8,10,11,12,13};
    
    // 1.
    int result = BinarySearch_1(list, 10, 1);
    cout << result << endl; // -1
    result = BinarySearch_3(list, 10, 8);
    cout << result << endl; // 8
    result = BinarySearch_3(list, 10, 14);
    cout << result << endl; // -1
    
    // 2.
    result = BinarySearch_2(list, 10, 1);
    cout << result << endl; // 자신보다 작은 값이 없기에 -1을 반환
    result = BinarySearch_2(list, 10, 6);
    cout << result << endl; // 자신보다 작은 5를 반환
    result = BinarySearch_2(list, 10, 14);
    cout << result << endl; // 자신보다 작은 13을 반환
    
    // 3.
    result = BinarySearch_3(list, 10, 1);
    cout << result << endl; // 자신보다 큰 2를 반환
    result = BinarySearch_3(list, 10, 6);
    cout << result << endl; // 자신보다 큰 7을 반환
    result = BinarySearch_3(list, 10, 14);
    cout << result << endl; // 자신보다 큰 수가 없기에 -1을 반환
    return 0;
}
