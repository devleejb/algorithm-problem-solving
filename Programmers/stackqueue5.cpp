#include <string>
#include <stack>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
    int light = 0;
    int len = arrangement.length();
    stack<int> s;

    for (int i = 0; i < len; i++)
    {
        if (arrangement.at(i) == '(')
        {
            if (arrangement.at(i + 1) == ')') // 레이저
            {
                light++;
                i++;
            }
            else s.push(light); // 새로운 막대기 생성
        } else if(arrangement.at(i) == ')') // 막대기 닫힘
        {
            if (!s.empty())
            {
                answer += light - s.top() + 1; // 막대기가 닫힐 때 그 막대기가 맞은 레이저 갯수에 1을 더하여 조각 갯수를 구함.
                s.pop();
            }
        }
    }

    return answer;
}