struct Node {
	char	ch;
	Node	*next;
};

class StrType {
public:
	StrType(const char* inp);
	void MakeEmpty();
	void Print();
	int LengthIs();
	int Compare(StrType& otherString);
    void Concat(StrType& otherString);
private:
	Node	*str;
};