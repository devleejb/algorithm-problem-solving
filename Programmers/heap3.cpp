#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

typedef struct job {
    public:
        int start;
        int len;

        job(int start, int len) {
            this->start = start;
            this->len = len;
        }
} job;

bool operator<(job a, job b) {
    if (a.len > b.len) return true;
    else if (a.len == b.len) return a.start > b.start;
    else return false;
}

bool compare(vector<int> a, vector<int> b) {
    if (a[0] < b[0]) return true;
    else if (a[0] == b[0]) return a[1] < b[1];
    else return false;
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int time = 0;
    int size = jobs.size();
    priority_queue<job> pq;

    sort(jobs.begin(), jobs.end(), compare);

    pq.push(job(jobs[0][0], jobs[0][1]));
    
    jobs.erase(jobs.begin());

    while (!pq.empty())
    {
        job ing = pq.top();

        pq.pop();

        if (ing.start > time)
        {
            time = ing.start + ing.len; // 현재 시간 이후에 일이 요청됨.
        } 
        else
        {
            time += ing.len;
        }

        answer += time - ing.start;

        while (!jobs.empty() && jobs[0][0] <= time)
        {
            pq.push(job(jobs[0][0], jobs[0][1]));
            jobs.erase(jobs.begin());
        }

        if (pq.empty() && !jobs.empty()) // 일이 다 끝나지 않았지만 pq가 비어버린 상황
        {
            pq.push(job(jobs[0][0], jobs[0][1]));
            jobs.erase(jobs.begin());

            while (!jobs.empty() && jobs[0][0] == pq.top().start)
            {
                pq.push(job(jobs[0][0], jobs[0][1]));
                jobs.erase(jobs.begin());
            }     
        }
        
    }
    
    return answer / size;
}