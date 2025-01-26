#include <iostream>

int main()
{
	int month, year;
	std::cin >> month >> year;
	int vis;
	if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
	{
		vis = 1;
	}
	else
	{
		vis = 0;
	}

	if (month == 2)
	{
		if (vis == 1)
		{
			std::cout << 29;
		}
		else
		{
			std::cout << 28;
		}

	}
	else if (month == 4 or month == 6 or month == 9 or month == 11)
	{
		std::cout << 30;
	}
	else
	{
		std::cout << 31;
	}
	return 0;
}