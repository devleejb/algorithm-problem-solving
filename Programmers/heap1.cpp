#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int size = scoville.size();
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < size; i++)
    {
        pq.push(scoville[i]);
    }

    while (pq.size() != 1 && pq.top() < K) // pq에서 가장 작은 값이 K보다 작다면 음식을 섞어 새로운 음식을 만든다.
    {
        int a, b;

        answer++;
        
        a = pq.top();
        pq.pop();

        b = pq.top();
        pq.pop();

        pq.push(a + b * 2);
    }

    if (pq.top() >= K) return answer;
    else return -1;
}