#include <iostream>
#include <string>
#include "StackTType.h"
using namespace std;


bool isBalance(string inp) {

	// ���� ���� ��ȣ ���ڿ����� �˻�

	

}

bool isCorrect(string inp) {

	// Stack�� �̿��ؼ� �ùٸ� ��ȣ ���ڿ����� �˻�



}

string solution(string inp) {


	string x = inp;
	string y = "";
	string z = "";
	string answer = "";
	char c = '(';
	char d = ')';

	// �Է��� ���ڿ��� ���
	if (inp == "") {

		return x;
	}
	else {

		// �������� ��ȣ ���ڿ� y, z �и�
		for (int i = 0; i < x.length(); i++) {
			if (x[i] == c)
				y.


		}
		// �ùٸ� ��ȣ ���ڿ� ó��
		if (isCorrect(y)){
			
		}
		// �ƴ� ��쿡 ���� ó��
		else {
			
		}

	}


	return answer;
}

int main() {

	string inp;
	string answer;

	cin >> inp;

	answer = solution(inp);

	cout << answer;

	return 0;
}

