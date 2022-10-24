#include <iostream>
using namespace std;

const int MAX_ITEM = 200;

class DoubleStack{
private:
    int top_small;
    int top_big;
    int item[MAX_ITEM];
public:
    void Push(int item);
    void Print();
};

void DoubleStack::Push(int item)
{
    static int front = 0, rear = 200;
    if (item > 1000){
        
    }
}
