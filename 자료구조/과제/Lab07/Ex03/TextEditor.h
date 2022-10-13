#include <iostream>
#include <string.h>
using namespace std;

struct LineType
{
    char info[80];
    LineType* next;
    LineType* before;
};

class TextEditor
{
private:
    LineType *pos_line;
    LineType *head;
    LineType *tail;
    int length;
public:
    TextEditor(){};
    ~TextEditor();
    void ResetText();
    void GoToTop();
    void GoToBottom();
    void Insertline(char newline[]);
    void Print();
};

LineType *newline(){
    LineType *new_line;
    new_line = new LineType;
    new_line->before = NULL;
    new_line->next = NULL;
    return new_line;
}

TextEditor::TextEditor(){
    length = 0;
    head = newline();
    tail = newline();
    head->next = tail;
    tail->before = head;
    pos_line = head;
}

// void TextEditor::GoToTop(){
//     pos_line = head->next;
// }

// void TextEditor::GoToBottom(){
//     pos_line = tail->before;
// }


// void TextEditor::Insertline(char newline[])
// {
//     LineType *location;
//     for (int i = 0; newline[i] != 0, i < 80; i++){
//         location->info[i] = newline[i];
//     }
//     location = location->next;
//     length++;
// }

// void TextEditor::Print(){
//     LineType *Line_print = head->next;
//     while (Line_print != tail){
//         cout << Line_print->info << "\n";
//         Line_print = Line_print->next;
//     }
// }