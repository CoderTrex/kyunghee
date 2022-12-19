#include <iostream>
#include <string.h>
#include "QueType.h"
#include "StackType.h"
using namespace std;

int main(){
    StackType tmp;
    int i = 0;
    char item;
    // string target = "(((1+2)-(3/4))*5)";
    string target = "((6+(7*8))+((9-10)/11))";
    
    while (target[i]){
        if (target[i] == ')'){
            item = tmp.Top();
            tmp.Pop();
            cout << item;
        }
        else if (target[i] == '-' || target[i] == '+' || target[i] == '/' 
        || target[i] == '*'){
            tmp.Push(target[i]);
        }
        else if (target[i] != '('){
            cout << target[i];
        }
        i++;
    }
}