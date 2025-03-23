#include <iostream>

int main()
{
    int num;
    std::cin >> num;
    int sum = 0;
    do
    {
        sum += num % 10;
        num /= 10;
    } while (num != 0);
    std::cout << sum;
}