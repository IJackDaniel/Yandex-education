#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

int main()
{
    std::string password;
    std::cin >> password;
    std::string result = "YES";
    if (password.size() > 14 || password.size() < 8) result = "NO";  // Проверка длины пароля
    std::vector<bool> classes (4, false);
    for (char symb : password)
    {
        if ((33 <= int(symb) && int(symb) <= 47) || (58 <= int(symb) && int(symb) <= 64) || (91 <= int(symb) && int(symb) <= 96)) 
        {
            classes[0] = true;      // Специальные символы
        }
        else if (48 <= int(symb) && int(symb) <= 57) 
        {
            classes[1] = true;      // Цифры
        }
        else if (65 <= int(symb) && int(symb) <= 90) 
        {
            classes[2] = true;      // Заглавные буквы
        }
        else if (97 <= int(symb) && int(symb) <= 122) 
        {
            classes[3] = true;      // Строчные буквы
        }
        else result = "NO";         // Проверка по таблице ASCII
    }

    int cnt = 0;
    for (bool elem : classes)
    {
        cnt = elem ? cnt + 1 : cnt;
    }
    if (cnt < 3) result = "NO";  // Проверка классов символов

    std::cout << result;
}

