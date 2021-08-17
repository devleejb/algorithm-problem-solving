#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string, bool> m;
    int size = participant.size();
    int cnt = 0;

    for (int i = 0; i < size; i++)
    {
        m.insert({participant[i], false}); // 참가자 삽입
    }

    for (int i = 0; i < size - 1; i++)
    {
        auto tmp = m.find(completion[i]); // 완주자 체크

        tmp->second = true;

        cnt = 0;

        for (int j = 0; j < participant.size(); j++) // 동명이인 체크
        {
            if (tmp->first == participant[j]) cnt++;
        }
        
        if (cnt > 1)
        {
            for (int j = 0; j < participant.size(); j++)
            {
                if (participant[j] == tmp->first)
                {
                    participant.erase(participant.begin() + j);
                }
            }
        
            tmp->second = false;
        }
        
    }

    for (int i = 0; i < size; i++)
    {
        if (m.find(participant[i])->second == false) // 완주하지 못한 사람 체크 후 반환
        {
            return m.find(participant[i])->first;
        }
    }
}