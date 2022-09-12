#ifndef EX28_H
#define EX28_H
#define MAX_RSIZE 50
#define MAX_CSIZE 50

class SquareMatrix {
private:
	int matrix[50][50];
public:
	void MakeEmpty(int n);
	void StoreValue(int i, int j, int value);
	void Add(SquareMatrix &AddMatrix);
	void Subtract(SquareMatrix &SubMatrix);
	void Copy(SquareMatrix &CopyMatrix);
};

#endif