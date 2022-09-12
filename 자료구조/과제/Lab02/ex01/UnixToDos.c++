#include <iostream>
#include <fstream>
using namespace std;;

int main(){
    ifstream input_file("myln.txt");
    ofstream output_file("myOut.txt");
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