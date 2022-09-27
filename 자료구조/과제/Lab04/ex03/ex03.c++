#include <iostream>
using namespace std;
const int MAX_ITEMS = 200; 


class doublestack
{
private:
    int top_small; 
    int items[MAX_ITEMS];
public:

    void Push(int item); 
    void Print();
};

void doublestack::Push(int item){
    static int check_front = 0, check_back = 199;
    if (item > 1000){
        items[check_back] = item;
        check_back--;
    }
    else if (item < 1000){
        items[check_front] = item;
        check_front++;
    }
    if (check_front == check_back){
        cout << "stack is full \n you can't push the item";
    }
}

void doublestack::Print(){
    for (int i = 0; i < 200; i++){
        cout << items[i] << " ";
        if (i%10 == 9){
            cout << "\n";
        }
    }
}