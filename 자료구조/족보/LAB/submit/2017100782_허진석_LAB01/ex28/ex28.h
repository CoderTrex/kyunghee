#ifndef EX28_H
#define EX28_H
#define MAX_ROWS 50
#define MAX_COLS 50

//	규격명세서
//	구조:
//		[private] matrix int[50][50]: 행렬 데이터
//	연산:
//		1. MakeEmpty(int n)
//			1.1 기능: Matrix의 n행 열 내부를 0으로 초기화
//			1.2 조건: n의 최대 크기는 50
//			1.3 결과: n안의 행 열은 0으로 초기화
//		2. StoreValue(int i, int j, int value)
//			2.1 기능: value를 i번째행, j번째 열의 위치에 저장
//			2.2 조건: i, j < 50
//			2.3 결과: Matrix[i][j]의 값이 value로 변경
//		3. Add(SquareMatrix&)
//			3.1 기능: 두 행렬의 합을 계산
//			3.2 조건: 없음
//			3.3 결과: 인수로 받은 행렬을 더한 결과가 저장됨
//		4. Subtract(SquareMatrix&)
//			4.1 기능: 한 행렬을 다른 행렬로부터 뺀다
//			4.2 조건: 없음
//			4.3 결과: 인수로 받은 행렬을 뺀 결과가 저장됨
//		5. Copy(SquareMatrix&)
//			5.1 기능: 한 행렬을 다른 행렬로 복사
//			5.2 조건: 없음
//			5.3 결과: 인자로 들어온 행렬에 객체의 행렬 데이터가 복사됨

class SquareMatrix {
private:
	int matrix[50][50];
public:
	void MakeEmpty(int n);
	void StoreValue(int i, int j, int value);
	void Add(SquareMatrix &otherMatrix);
	void Subtract(SquareMatrix &otherMatrix);
	void Copy(SquareMatrix &otherMatrix);
};

#endif