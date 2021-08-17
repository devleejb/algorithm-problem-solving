#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int size = prices.size();
    int price, cnt, idx;

    for (int i = 0; i < size; i++)
    {
        price = prices[i];
        cnt = 0;

        for (idx = i + 1; idx < size; idx++) // 각 price에 대해 언제 price가 감소하는지 시간을 측정하여 정답 도출함.
        {
            cnt++;            

            if (prices[idx] < price)
            {
                answer.push_back(cnt);

                break;
            }
        }

        if (idx == size)
        {
            answer.push_back(cnt);
        }
    }
    
    return answer;
}