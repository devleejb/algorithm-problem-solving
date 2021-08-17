#include <string>
#include <set>

using namespace std;

int divide(int a, int b) {
    if (!b) return -1;
    else return a / b;
}

int solution(int N, int number) {
    int answer = 9;
    set<int> arr[8];

    for (int i = 0; i < 8; i++) arr[i] = set<int>();

    for (int i = 0; i < 8; i++)
    {
        string tmp = "";

        for (int j = 0; j < i + 1; j++) tmp = tmp + to_string(N);    
        
        arr[i].insert(atoi(tmp.c_str()));

        for (int j = 0; j < i / 2; j++)
        {
            for (auto k = arr[j].begin(); k != arr[j].end(); k++)
            {
                for (auto l = arr[i - j].begin(); l != arr[i - j].end(); l++)
                {
                    int tmp = divide(*k, *l);

                    arr[i].insert(*k + *l);
                    arr[i].insert(*k - *l);
                    arr[i].insert(*k * *l);

                    if (tmp != -1) arr[i].insert(tmp);
                }
            }
        }
    }

    for (int i = 0; i < 8; i++)
    {
        for (auto j = arr[i].begin(); j != arr[i].end(); j++)
        {
            if (*j == number)
            {
                return i + 1;
            }   
        }
    }
    
    return -1;
}