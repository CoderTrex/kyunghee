#include <iostream>
#include <fstream>
using namespace std;

int main(int ar, char **av){
    if (ar != 3){
        cout << "입력 인자의 개수가 맞지 않습니다.";
        exit(EXIT_FAILURE);
    }
    ifstream input_file(av[1]);
    ofstream output_file(av[2]);
    char ch;
    if (input_file.fail()){
        cout << "파일을 읽지 못했습니다.";
        exit(EXIT_FAILURE);
    }
    while(input_file.eof()){
        input_file.get(ch);
        if (input_file.fail()) break;
        if (ch == '\n')
            continue ;
        else
            output_file << ch;
    }
    input_file.close();
    output_file.close();
}