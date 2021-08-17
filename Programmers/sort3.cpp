#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int size = citations.size();

    sort(citations.begin(), citations.end());

    for (int i = size - 1; i > -1; i--)
    {
        if (answer < size - i && size - i <= citations[i]) // size - i가 H-Index가 되는 경우, ex) [0, 100, 100] -> 2
        {
            answer = size - i;
        } else if ( answer < citations[i] && citations[i] < size - i) // citations[i]가 H-Index가 되는 경우, ex) [0, 1, 1] -> 1
        {
            answer = citations[i];
        }
        
    }
    
    return answer;
}