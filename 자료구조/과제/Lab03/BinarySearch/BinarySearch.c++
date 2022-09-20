#include <iostream>
using namespace std;

// Case_one :
// 찾으면    : 수 반환
// 못 찾으면 : -1 반환
int  BinarySearch(int array[], int sizeOfArray, int value){
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
    cout << "this is result : "  << result << endl;
    return result;  
}

int main()
{
    int list[10] = {1,2,3,4,5,6,7,8,9,10};
    int result = BinarySearch(list, 10, 11);
    cout << result << endl; // -1 리턴
    result = BinarySearch(list, 10, 7);
    cout << result << endl; // 6 리턴
    return 0;
}
