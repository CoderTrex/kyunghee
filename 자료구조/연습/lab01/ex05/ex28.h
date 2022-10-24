#ifndef EX28_H
#define EX28_H
#include <iostream>


class SquareMatrix{
private:
    int matrix[50][50];
public:
    void MakeEmpty(int n);
    void Storevalue(int i , int j, int value);
    void Add(SquareMatrix &arr);
    void Subtract(SquareMatrix &arr);
    void Copy(SquareMatrix &arr);
};

void SquareMatrix::MakeEmpty(int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            matrix[i][j] = 0;
        }
    }
}

void SquareMatrix::Storevalue(int i, int j, int value){
    matrix[i][j] = value;
}

void SquareMatrix::Add(SquareMatrix &arr){
    for (int i = 0; i < 50; i++){
        for (int j = 0; j < 50; j++){
            matrix[i][j] += arr.matrix[i][j];
        }
    }
}

void SquareMatrix::Subtract(SquareMatrix &arr){
    for (int i = 0; i < 50; i++){
        for (int j = 0; j < 50; j++){
            matrix[i][j] -= arr.matrix[i][j];
        }
    }
}

void SquareMatrix::Copy(SquareMatrix &arr){
    for (int i = 0; i < 50; i++){
        for (int j = 0; j < 50; j++){
            matrix[i][j] = arr.matrix[i][j];
        }
    }
}




#endif