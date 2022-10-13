#include "TextEditor.hpp"

LineType *new_line_type() {
	LineType *new_lt;

	new_lt = new LineType;
	new_lt->prev = NULL;
	new_lt->next = NULL;
	return new_lt;
}

TextEditor::TextEditor() {
	_init();
}

TextEditor::TextEditor(const std::string &text) {
	_init();

	insert_line(text);
}

TextEditor::~TextEditor() {
	LineType *tmp = head;
	LineType *target;

	while (tmp != NULL) {
		target = tmp;
		tmp = tmp->next;
		delete target;
		target = NULL;
	}
}

void TextEditor::print_current_line() {
	std::cout << cur_line->text << '\n';
}

void TextEditor::print_all() {
	LineType *tmp = head->next;

	while (tmp != tail) {
		std::cout << tmp->text << '\n';
		tmp = tmp->next;
	}
}

void TextEditor::go_to_top() {
	cur_line = head->next;
}

void TextEditor::go_to_bottom() {
	cur_line = tail->prev;
}

void TextEditor::insert_line(const std::string &text) {
	LineType *line;
	std::size_t size = text.length();
	std::size_t row_num;

	if (size % (LINE_LEN - 1) != 0) {
		row_num = size / (LINE_LEN - 1) + 1;
	} else {
		row_num = size / (LINE_LEN - 1);
	}

	for (int r = 0; r < row_num; r++) {
		line = new_line_type();
		line->next = cur_line->next;
		cur_line->next->prev = line;
		line->prev = cur_line;
		cur_line->next = line;
		cur_line = line;

		std::string s = text.substr(r * (LINE_LEN - 1), (r + 1) * (LINE_LEN - 1));
		for (int i = 0; i < LINE_LEN - 1; i++) {
			line->text[i] = s[i];
		}
	}
	line_count += row_num;
}

void TextEditor::_init() {
	head = new_line_type();
	tail = new_line_type();
	head->next = tail;
	tail->prev = head;
	cur_line = head;

	line_count = 0;
}
