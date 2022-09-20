#include <iostream>

int BinarySearch(int *arr, int size, int val) {
	int left, right, mid;

	left = 0;
	right = size - 1;
	while (left <= right) {
		mid = (left + right) / 2;
		if (val < arr[mid]) {
			right = mid - 1;
		}
		else if (val > arr[mid]) {
			left = mid + 1;
		}
		else
			return mid;
	}
	if (arr[mid] == val)
		return mid;
	return -1;
}

int main() {
	int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	int res = BinarySearch(arr, 10, 11);
	std::cout << res << std::endl;

	res = BinarySearch(arr, 10, 7);
	std::cout << res << std::endl;
	return 0;
}
