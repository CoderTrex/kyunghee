#include <iostream>
#include <cmath>
using namespace std;

float SqrRoot_R(float num, float result, float tol){

}

//재귀 버전. 문제에 적힌 내용을 적으시면 됩니다.
float SqrRoot_recursion(float number, float approx, float tol)
{
    if(abs(approx*approx - number) <= tol)
        return approx;
    else
        return SqrRoot_recursion(number, (approx*approx + number) / (2 * approx), tol);
}
//비재귀 버전. 재귀 버전에서 반복적으로 계산하는 부분을 조건에 맞춰 돌리면 됩니다.
float SqrRoot_non_recursion(float number, float approx, float tol)
{
    while(abs(approx*approx - number) > tol){
        approx = (approx * approx + number)/(2 * approx);
    }
    return approx;
}

int main(){
    float result;
    // result = SqrRoot_recursion(2, 1, 0.1);
    result = SqrRoot_non_recursion(2, 1, 0.1);
    cout << result << endl;
}