#include <iostream>
#include "TextEditor.h"
using namespace std;

int main(){
    TextEditor tester;
    char arr[10] = "hello";
    for (int i=0; i < 10; i++){
        tester.Insertline(arr);
    }
    tester.Print();
}