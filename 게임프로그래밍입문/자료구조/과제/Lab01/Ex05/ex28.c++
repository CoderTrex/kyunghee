#include "ex28.h"

void SquareMatrix::MakeEmpty(int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++){
			this->matrix[i][j] = 0;
		}
	}
}

void SquareMatrix::StoreValue(int i, int j, int value) {
	this->matrix[i][j] = value;
}

void SquareMatrix::Add(SquareMatrix &Addmatrix) {
	for (int i = 0; i < MAX_RSIZE; i++) {
		for (int j = 0; j < MAX_CSIZE; j++) {
			this->matrix[i][j] += Addmatrix.matrix[i][j];
		}
	}
}

void SquareMatrix::Subtract(SquareMatrix &SubMatrix) {
	for (int i = 0; i < MAX_RSIZE; i++) {
		for (int j = 0; j < MAX_CSIZE; j++) {
			this->matrix[i][j] -= SubMatrix.matrix[i][j];
		}
	}
}

void SquareMatrix::Copy(SquareMatrix &CopyMatrix) {
	for (int i = 0; i < MAX_RSIZE; i++) {
		for (int j = 0; j < MAX_CSIZE; j++) {
			this->matrix[i][j] = CopyMatrix.matrix[i][j];
		}
	}
}