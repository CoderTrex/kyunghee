#include <iostream>
using namespace std;

int BinarySearch(int arr[], int sizeOfArray, int value){
    int midnum = sizeOfArray/2 - 1, result = -1;
    int lownum = 0, highnum = sizeOfArray - 1;
    for (int i = 0; i < sizeOfArray; i++){
        if (arr[midnum] == value){
            result = midnum;
            break;
        }
        else{
            if (arr[midnum] < value){
                lownum = midnum + 1;
            }
            else if (arr[midnum] > value){
                highnum = midnum - 1;

            }
            midnum = (lownum + highnum)/2;
            if (midnum > highnum || midnum < lownum){
                break;
            }
        }
    }
    return result;    
}

int main() {
	int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	int res = BinarySearch(arr, 10, 11);
	std::cout << res << std::endl;

	res = BinarySearch(arr, 10, 7);
	std::cout << res << std::endl;
	return 0;
}