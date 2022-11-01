#include <iostream>
#define MAX_ROWS 10;
#define MAX_COLS 10;
using namespace std;


int NumPaths_A(int row,int col,int n){
    if((row==n)||(col==n))
        return 1;
    else{
        return NumPaths_A(row + 1, col, n) + NumPaths_A(row, col + 1, n);
    }
}


int mat[10][10];

int NumPaths_B(int row,int col,int n)
{
    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            mat[i][j] = -1;
        }
    }
    if(mat[row][col] == -1) { // 아직 구해지지 않은 경우
    // (A) 번의 코드를 이용하여 계산
    // 위에서 구한 값을 mat[row][col]에 기억시켜 놓음
        mat[row][col] = NumPaths_A(1, 1, n);
    }
    
    return mat[row][col];
}

int main(){
    int result_a, result_b;
    result_a = NumPaths_A(1,1,5);
    result_b = NumPaths_B(1,1,5);
    cout << result_a << endl;
    cout << result_b << endl;
}