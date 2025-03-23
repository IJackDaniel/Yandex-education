#include <iostream>

int main()
{
	int n, k;
	std:: cin >> n >> k;
	int num = -(n - 2);
	int pos = 1;
	do
	{
		if (num >= 1)
		{
			if (num <= 9)
			{
				std::cout << ' ' << num;
			}
			else
			{
				std::cout << num;
			}
		}
		else
		{
			std::cout << "  ";
		}
		if (pos % 7 == 0)
		{
			std::cout << std::endl;
		}
		else
		{
			std::cout << ' ';
		}
		num++;
		pos++;
	} while (num <= k);
}
