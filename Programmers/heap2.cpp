#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    int idx = 0;
    priority_queue<int> pq;

    for (int day = 0; day < k; day++)
    {
        stock--; // 재고 소진
        day = day + stock + 1; // 재고 모두 소진하는 날짜

        if (day > k - 1) break;
        else stock = -1;
    
        while (dates[idx] <= day) pq.push(supplies[idx++]);
        
        stock += pq.top();
        pq.pop();
        answer++;
    }
    
    return answer;
}