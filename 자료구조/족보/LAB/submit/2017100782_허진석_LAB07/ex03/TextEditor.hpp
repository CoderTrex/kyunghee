#ifndef TEXTEDITOR_H
#define TEXTEDITOR_H

#include <iostream>
#include <string>
#define LINE_LEN 80

// Problem A
struct LineType {
	LineType *prev;
	LineType *next;
	char text[LINE_LEN];
};

LineType *new_line_type();

class TextEditor {
private:
	LineType *head;
	LineType *tail;
	LineType *cur_line;
	std::size_t line_count;

	void _init();

public:
	// Problem B
	TextEditor();
	TextEditor(const std::string &text);
	~TextEditor();
	// Problem C
	void go_to_top();
	void go_to_bottom();
	// Problem E
	void insert_line(const std::string &text);
	void print_current_line();
	void print_all();
};

#endif