#include <iostream>
#include <fstream>
using namespace std;;

int main(int ar, char **av){
    if (ar != 3){
        cout << "입력 인자의 개수가 맞지 않습니다.";
        return 0;
    }

    ifstream input_file(av[1]);
    ofstream output_file(av[2]);
    char ch;
    while(!input_file.eof()){
        input_file.get(ch);
        if (input_file.fail()) break;
        if (ch == '\r') {// ch가 LF ('\r')이라면
            output_file << ch;
            output_file << "\n";
        }
        else
            output_file << ch;
    }
    input_file.close();
    output_file.close();
}