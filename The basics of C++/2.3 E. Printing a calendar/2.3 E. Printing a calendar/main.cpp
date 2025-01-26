#include <iostream>

int main() 
{
	int n, k;
	std::cin >> n >> k;
	for (int j = 1; j < n - 1; j++) 
	{
		std::cout << "   ";
		if (j != n - 2) 
		{
			std::cout << " ";
		}
	}
	int day = n;
	int i = 1;
	while (i <= k) 
	{
		if (i < 10) 
		{
			std::cout << "  " << i;
		}
		else 
		{
			std::cout << " " << i;
		}
		
		if (day == 7) 
		{
			std::cout << "\n";
			day = 1;
			i++;
			continue;
		}
		i++;
		day++;
	}
}