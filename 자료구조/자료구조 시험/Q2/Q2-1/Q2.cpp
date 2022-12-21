#include <iostream>
#include <string>
#include "StackTType.h"
using namespace std;


bool isBalance(string inp) {

	// 균형 잡힌 괄호 문자열인지 검사

	

}

bool isCorrect(string inp) {

	// Stack을 이용해서 올바른 괄호 문자열인지 검사



}

string solution(string inp) {


	string x = inp;
	string y = "";
	string z = "";
	string answer = "";
	char c = '(';
	char d = ')';

	// 입력이 빈문자열이 경우
	if (inp == "") {

		return x;
	}
	else {

		// 균형잡힌 괄호 문자열 y, z 분리
		for (int i = 0; i < x.length(); i++) {
			if (x[i] == c)
				y.


		}
		// 올바른 괄호 문자열 처리
		if (isCorrect(y)){
			
		}
		// 아닌 경우에 대한 처리
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

