#include <iostream>

int main()
{
	int i1, i2, i3;
	std::cin >> i1 >> i2 >> i3;
	int a, b, c;
	a = std::max(std::max(i1, i2), i3);
	c = std::min(std::min(i1, i2), i3);
	b = i1 + i2 + i3 - a - c;

	if (a > b + c)
	{
		std::cout << "UNDEFINED";
	}
	else if (a * a == b * b + c * c)
	{
		std::cout << "YES";
	}
	else
	{
		std::cout << "NO";
	}
	return 0;
}