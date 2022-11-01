#include <iostream>
#define MAX_ROWS 8
#define MAX_COLS 8

int mat[MAX_ROWS][MAX_COLS];

int NumPaths_A(int row, int col, int n);
int NumPaths_B(int row, int col, int n);

int main()
{
	for (int i = 0; i < MAX_ROWS; i++)
	{
		for (int j = 0; j < MAX_COLS; j++)
			mat[i][j] = -1;
	}
	std::cout << NumPaths_A(1, 1, 4) << std::endl;
	std::cout << NumPaths_B(1, 1, 4) << std::endl;
}

int NumPaths_A(int row, int col, int n)
{
	if ((row == n) || (col == n))
		return 1;
	else
		return NumPaths_A(row + 1, col, n) + NumPaths_A(row, col + 1, n);
}

int NumPaths_B(int row, int col, int n)
{
	if ((row == n) || (col == n))
		mat[row][col] = 1;
	else if (mat[row][col] == -1)
	{
		mat[row][col] = NumPaths_B(row + 1, col, n) + NumPaths_B(row, col + 1, n);
	}
	return mat[row][col];
}
