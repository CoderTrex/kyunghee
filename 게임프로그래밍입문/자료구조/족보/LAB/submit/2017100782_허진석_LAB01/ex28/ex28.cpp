#include "ex28.h"

void SquareMatrix::MakeEmpty(int n) {
	for (int i = 0; i < MAX_ROWS; i++) {
		this->matrix[i][n] = 0;
	}
	for (int i = 0; i < MAX_COLS; i++) {
		this->matrix[n][i] = 0;
	}
}

void SquareMatrix::StoreValue(int i, int j, int value) {
	this->matrix[i][j] = value;
}

void SquareMatrix::Add(SquareMatrix &otherMatrix) {
	for (int i = 0; i < MAX_ROWS; i++) {
		for (int j = 0; j < MAX_COLS; j++) {
			this->matrix[i][j] += otherMatrix.matrix[i][j];
		}
	}
}

void SquareMatrix::Subtract(SquareMatrix &otherMatrix) {
	for (int i = 0; i < MAX_ROWS; i++) {
		for (int j = 0; j < MAX_COLS; j++) {
			this->matrix[i][j] -= otherMatrix.matrix[i][j];
		}
	}
}

void SquareMatrix::Copy(SquareMatrix &otherMatrix) {
	for (int i = 0; i < MAX_ROWS; i++) {
		for (int j = 0; j < MAX_COLS; j++) {
			this->matrix[i][j] = otherMatrix.matrix[i][j];
		}
	}
}
