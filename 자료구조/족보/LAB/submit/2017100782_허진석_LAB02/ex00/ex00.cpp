// mac os에서 작성됨
#include <fstream>
#include <iostream>

int main(int argc, char **argv) {
	if (argc != 3) {
		printf("wrong argument\n");
		exit(EXIT_FAILURE);
	}
	std::ifstream input(argv[1]);
	std::ofstream output(argv[2]);

	if (input.fail()) {
		std::cout << "error while reading input file\n" << std::endl;
		exit(EXIT_FAILURE);
	}

	char ch;
	while(input.eof()) {
		input.get(ch);
		if (input.fail()) {
			break;
		}
		if ((int)ch == 13) {
			output << (char)10;
			output << (char)13;
		} else {
			output << ch;
		}
	}
	input.close();
	output.close();
}
