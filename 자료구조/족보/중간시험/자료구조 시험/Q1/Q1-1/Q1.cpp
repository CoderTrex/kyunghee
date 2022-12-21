#include <iostream>
#include <ctime>
#include "QueType.h"
using namespace std;

#define QUEUE_SIZE 10
#define MAX_BIT 32

void radixsort(int*, int);

int main()
{
    int number, rand_int;
    cout << "Input: ";
    cin >> number;

    int* data = new int [number];

    //난수 초기화
    srand(time(NULL));

    for (int i = 0; i < number; i++) {
        rand_int = rand() % 10000;
        data[i] = rand_int;
    }

    cout << "\nBefore: ";
    for (int i = 0; i < number; i++) {
        cout << data[i] << " ";
    }

    // 정렬
    radixsort(data, number);

    // 정렬 후 출력
    cout << "\nAfter: ";
    for (int i = 0; i < number; i++) {
        cout << data[i] << " ";
    }
    return 0;
}

void    radixsort(int* data, int number)
{
    QueType bucket_for_bit_0(QUEUE_SIZE);
	QueType bucket_for_bit_1(QUEUE_SIZE);
    QueType box_zero(number);
    QueType box_one(number);
    QueType box_two(number);
    QueType box_tree(number);
    QueType box_four(number);
    QueType box_five(number);
    QueType box_six(number);
    QueType box_seven(number);
    QueType box_eight(number);
    QueType box_nine(number);

	// int mask = 1;
    for (int i = 1; i <= 10000; i *= 10)
	{
		for (int j = 0; j < number; j++)
		{
            int divide = i % 10;
            int compare = data[j] % divide;
            if ((compare % divide) == 0)
                box_zero.Enqueue(j);
            else if ((compare % divide) == 1)
                box_one.Enqueue(j);
            else if ((compare % divide) == 2)
                box_two.Enqueue(j);
            else if ((compare % divide) == 3)
                box_tree.Enqueue(j);
            else if ((compare % divide) == 4)
                box_four.Enqueue(j);
            else if ((compare % divide) == 5)
                box_five.Enqueue(j);
            else if ((compare % divide) == 6)
                box_six.Enqueue(j);
            else if ((compare % divide) == 7)
                box_seven.Enqueue(j);
            else if ((compare % divide) == 8)
                box_eight.Enqueue(j);
            else if ((compare % divide) == 9)
                box_nine.Enqueue(j);
		}
		int *tmp = (int *)malloc(number* sizeof(int));

		int index = 0;
		int temp_item = 0;
        while (box_zero.IsEmpty() == 0)
        {
            int i;
            box_one.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_one.IsEmpty() == 0)
        {
            int i;
            box_one.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_two.IsEmpty() == 0)
        {
            int i;
            box_two.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_tree.IsEmpty() == 0)
        {
            int i;
            box_tree.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_four.IsEmpty() == 0)
        {
            int i;
            box_four.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_five.IsEmpty() == 0)
        {
            int i;
            box_five.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_six.IsEmpty() == 0)
        {
            int i;
            box_six.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_seven.IsEmpty() == 0)
        {
            int i;
            box_seven.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_eight.IsEmpty() == 0)
        {
            int i;
            box_eight.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        while (box_nine.IsEmpty() == 0)
        {
            int i;
            box_nine.Dequeue(i);
            tmp[index] = data[i];
            index++;
        }
        
		for (int i = 0; i < number; i++) {
			data[i] = tmp[i];
		}
	}
}