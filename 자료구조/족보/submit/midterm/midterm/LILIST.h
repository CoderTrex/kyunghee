struct Node
{
	int item;
	Node *sublist;
	Node *next;
};

class LILIST
{
public:
	LILIST();
	~LILIST();
	int isLength();
	void InsertList(char *);
	void InsertItem(int);
	void DeleteItem(int);
	int Sum1();
	int Sum2();
	void Print();
	void PrintRec(Node *);

private:
	Node *elem;
};
