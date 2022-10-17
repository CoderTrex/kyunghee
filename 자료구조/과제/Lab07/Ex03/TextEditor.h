#include <iostream>
using namespace std;

template<class ItemType>
class TextEditor
{
private:
    LineType<ItemType>* listdata;
    LineType<ItemType>* currentPos;
    int length;
public:
    TextEditor(){
        head = 0;
        tail = 0;
        length = 0;
        listdata = NULL;
    };~TextEditor();
    void RestText();
    void GoToTop();
    void GoToBottom();
    void InsertItem(char newline[]);
    void Print();
};

template<class ItemType>
struct LineType
{
    char info[80];
    int* Header;
    int* Tailer;
};

template<class ItemType>
void TextEditor<ItemType>::GoToTop(){
    while (listdata->Tailer != nullptr){
        listdata = listdata->Tailer;
    }
    listdata = listdata->Header;
}

template<class ItemType>
void TextEditor<ItemType>::GoToBottom(){
    while (listdata->Header != nullptr){
        listdata = listdata->Hailer;
    }
    listdata = listdata->Tailer;
}

template<class ItemType>
void TextEditor<ItemType>::InsertItem(char newline[])
{
    LineType<ItemType> *location;

    location = new LineType<ItemType>;
    location->info = newline;
    location->next = listData;
    listData = location;
    length++;
}

template<class ItemType>
void TextEditor<ItemType>::Print(){
    LineType<ItemType> *tempPtr = listdata;

    while (tempPtr != NULL){
        cout << tempPtr->info << " ";
        tempPtr = tempPtr->Header;
    }
}