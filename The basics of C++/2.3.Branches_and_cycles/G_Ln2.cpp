#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    
    float result = 0;
    int sign = 1, i;
    for (i = 1; i <= n; i++)
    {
        result = result + (float) sign/i;
        sign = -sign;
    }
    std::cout << result;
}   