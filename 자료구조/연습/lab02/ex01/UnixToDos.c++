#include <iostream>
#include <fstream>
using namespace std;


int main(){
    ifstream input_file("text.txt");
    ofstream output_file("out.txt");

    char ch;
    while (input_file.eof()){
        input_file.get(ch);
        if (ch == '\r'){
            output_file << ch;
            output_file << '\n';
        }
        else{
            output_file << ch;
        }
    }
    input_file.close();
    output_file.close();
}