#include <iostream>

int Fibonacci_recursive(int n);
int Fibonacci_non_recursive(int n);

int main()
{
	using namespace std;
	cout << Fibonacci_recursive(11) << endl;
	cout << Fibonacci_non_recursive(11) << endl;
	return 0;
}

int Fibonacci_recursive(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	return Fibonacci_recursive(n - 1) + Fibonacci_recursive(n - 2);
}

int Fibonacci_non_recursive(int n)
{
	int val_1 = 0;
	int val_2 = 1;

	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	for (int i = 0; i < n - 1; i++)
	{
		int val = val_1 + val_2;
		val_1 = val_2;
		val_2 = val;
	}
	return val_2;
}
