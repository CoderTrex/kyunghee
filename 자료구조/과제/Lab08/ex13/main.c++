#include <iostream>
using namespace std;

int fibo(int num){
    if (num == 0)
        return 1;
    else if (num == 1)
        return 1;
    else
        return fibo(num - 1) + fibo(num - 2);
}

int Fibonacci_non_recursive(int n){
    int result = 0, first = 0, second = 1;
    if (n == 1)
        return 0;
    else if (n == 2){
        return 1;
    }
    while (n-- > 2){
        int tmp = first;
        first = second;
        second= tmp + second;
        result += first + second;
    }
    return result;
    
}

int main(){
    int result;
    result = fibo(6) - 1;
    result = Fibonacci_non_recursive(6);
    cout << result << endl;
}