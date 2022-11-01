#include <iostream>
#include <cmath>

float SqrRoot_recursion(float number, float approx, float tol);
float SqrRoot_non_recursion(float number, float approx, float tol);

int main()
{
	std::cout << SqrRoot_recursion(2, 0.01, 0.01) << std::endl;
	std::cout << SqrRoot_non_recursion(2, 0.01, 0.01) << std::endl;
}

float SqrRoot_recursion(float number, float approx, float tol)
{
	if (abs(approx * approx - number) <= tol)
		return approx;
	return SqrRoot_recursion(number, (approx * approx + number) / (2 * approx), tol);
}

float SqrRoot_non_recursion(float number, float approx, float tol)
{
	while(abs(approx * approx - number) > tol)
	{
		approx = (approx * approx + number) / (2 * approx);
	}
	return approx;
}
