#include <iostream>
#include "TextEditor.h"
using namespace std;

int main(){
    TextEditor<int> tester;
    for (int i=0; i < 10; i++){
        tester.InsertItem("hello");
    }
    tester.Print();
}