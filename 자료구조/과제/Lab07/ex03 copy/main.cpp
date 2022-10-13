#include "TextEditor.hpp"


int main() {
	TextEditor te, empty;
	TextEditor te2("Hello world!adfadsfasdfadsfadsfdfadsfadsfasdfadsdddddddddddddddddfadfasfdsdfdsfasdfasfadsfsadfasfd");

	std::cout << "========= te test =========\n";
	std::cout << "Test for insert line\n";
	te.insert_line("Hello world!");
	te.insert_line("my name is dodo");
	te.insert_line("what is your name?");
	te.insert_line("asdfhsadkjgfhaskjdgblisdhgfipdshiofghioadsufghvilusdhfgvilausdhigluhdsidsafdsfdsafdasfadsfsdafdsaafds");

	te.print_all();

	std::cout << "Origin current line\n";
	te.print_current_line();
	std::cout << "Test for go to top\n";
	te.go_to_top();
	te.print_current_line();
	std::cout << "Test for go to bottom\n";
	te.go_to_bottom();
	te.print_current_line();
	te.go_to_top();
	te.insert_line("this must be second line");
	te.go_to_bottom();
	te.insert_line("this must be end line");

	te.print_all();

	std::cout << "\n========= te2 test =========\n";
	te2.print_all();

	std::cout << "Origin current line\n";
	te2.print_current_line();
	std::cout << "Test for go to top\n";
	te2.go_to_top();
	te2.print_current_line();
	std::cout << "Test for go to bottom\n";
	te2.go_to_bottom();
	te2.print_current_line();

	std::cout << '\n';

	std::cout << "\n========= empty test =========\n";
	empty.print_all();

	std::cout << "Origin current line\n";
	empty.print_current_line();
	std::cout << "Test for go to top\n";
	empty.go_to_top();
	empty.print_current_line();
	std::cout << "Test for go to bottom\n";
	empty.go_to_bottom();
	empty.print_current_line();

	std::cout << '\n';
	system("leaks a.out");
}
