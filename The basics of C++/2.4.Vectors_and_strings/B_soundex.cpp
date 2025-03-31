#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<char> one = {'b', 'f', 'p', 'v'};
    std::vector<char> two = {'c', 'g', 'j', 'k', 'q', 's', 'x', 'z'};
    std::vector<char> three = {'d', 't'};
    std::vector<char> four = {'l'};
    std::vector<char> five = {'m', 'n'};
    std::vector<char> six = {'r'};

    std::vector<char> delete_arr = {'a', 'e', 'h', 'i', 'o', 'u', 'w', 'y'};

    std::string inp;
    std::cin >> inp;
    std::string result1 = "";
    for (size_t i1 = 1; i1 < inp.size(); ++i1)
    {
        bool f1 = true;
        for (size_t j1 = 0; j1 < delete_arr.size(); ++j1)
        {
            if (inp[i1] == delete_arr[j1]) f1 = false;
        }
        if (f1) result1 += inp[i1];
    
    }
    result1 = inp[0] + result1;

    std::string result = "";
    result += inp[0];
    for (size_t i = 1; i < result1.size(); ++i)
    {
        for (size_t a = 0; a < one.size(); ++a)
        {
            if (result1[i] == one[a] && result.back() != '1')
            {
                result += "1";
            }
        }
        for (size_t b = 0; b < two.size(); ++b)
        {
            if (result1[i] == two[b] && result.back() != '2')
            {
                result += "2";
            }
        }
        for (size_t c = 0; c < three.size(); ++c)
        {
            if (result1[i] == three[c] && result.back() != '3')
            {
                result += "3";
            }
        }
        for (size_t d = 0; d < four.size(); ++d)
        {
            if (result1[i] == four[d] && result.back() != '4')
            {
                result += "4";
            }
        }
        for (size_t e = 0; e < five.size(); ++e)
        {
            if (result1[i] == five[e] && result.back() != '5')
            {
                result += "5";
            }
        }
        for (size_t f = 0; f < six.size(); ++f)
        {
            if (result1[i] == six[f] && result.back() != '6')
            {
                result += "6";
            }
        }
    }
    while (result.size() < 4)
    {
        result += "0";
    }
    if (result.size() > 4)
    {
        result = result.substr(0, 4);
    }
    std::cout << result;
}