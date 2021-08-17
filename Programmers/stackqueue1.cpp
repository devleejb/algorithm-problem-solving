#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    stack<int> ans_stack;
    int size = heights.size();
    int height;

    for (int i = size - 1; i > -1; i--)
    {
        height = heights[i];

        for (int j = i - 1; j > -1; j--)
        {
            if (heights[j] > height)
            {
                ans_stack.push(j + 1);

                break;
            }
        }

        if (ans_stack.size() != size - i)
        {
            ans_stack.push(0);
        }
        
    }

    for (int i = 0; i < size; i++)
    {
        answer.push_back(ans_stack.top());
        ans_stack.pop();
    }

    return answer;
}