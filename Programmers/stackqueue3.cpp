#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int cnt;

    while (!progresses.empty())
    {
        for (int i = 0; i < progresses.size(); i++)
        {
            progresses[i] += speeds[i]; // progress 진행
        }

        cnt = 0;

        for (int i = 0; i < progresses.size(); i++)
        {
            if (progresses[i] >= 100)
            {
                progresses.erase(progresses.begin() + i); // 완료된 프로세스 삭제
                speeds.erase(speeds.begin() + i);

                cnt++;
                i--;
            } 
            else
            {
                break;
            }   
        }

        if (cnt != 0)
        {
            answer.push_back(cnt);
        }
    }

    return answer;
}