#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> weight) {
    int answer = 0;
    int size = weight.size();

    sort(weight.begin(), weight.end());

    for (int i = 0; i < size; i++)
    {
        answer += weight[i];

        if (i + 1 < size && weight[i + 1] > answer + 1)
        {
            return answer + 1;
        }
    }

    return answer + 1;
}