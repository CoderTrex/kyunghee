#include <iostream>
using namespace std;

int fibo(int num){
    if (num == 0)
        return 0;
    else if (num == 1)
        return 1;
    else
        return fibo(num - 1) + fibo(num - 2);
}

int Fibonacci_non_recursive(int n){
    int first = 0, second = 1;

    if (n == 0)
        return 0;
    else if (n == 1){
        return 1;
    }
    for (int i = 0; i < n - 1; i++){
        int tmp = first + second;
        first = second;
        second= tmp;
    }
    return second;
    
}

int main(){
    // 0    1    1    2    3    5    8    13   21   34   55   89
    int result;
    result = fibo(11);
    cout << "recursion     : " << result << endl;
    result = Fibonacci_non_recursive(11);
    cout << "non_recursion : " << result << endl;
}