#include <iostream>
#include "LILIST.h"

using namespace std;

int	main()
{
	LILIST	a;

	a.InsertItem(5);
	a.InsertItem(9);
	a.DeleteItem(5);
	a.InsertList("(4 5 8)");
	a.InsertItem(2);
	a.InsertItem(18);
	a.InsertList("(13 2 6)");
	a.InsertItem(11);
	a.DeleteItem(2);
	a.Print();
	cout << a.Sum1() << " " << a.Sum2() << endl;
	return 0;
}
