#include <string>
#include <vector>

using namespace std;

typedef struct Document {
    public:
        int priority; // 해당 문서의 우선순위
        int location; // 해당 문서의 인덱스

        Document(int priority, int location) {
            this->priority = priority;
            this->location = location;
        }
} Document;


int solution(vector<int> priorities, int location) {
    vector<Document> v;
    int size = priorities.size();
    int order = 0;
    int idx;

    for (int i = 0; i < size; i++)
    {
        v.push_back(Document(priorities[i], i));
    }
    
    while (!v.empty())
    {
        Document doc = v[0]; // 첫번째 문서를 꺼냄.
     
        v.erase(v.begin());

        order++;

        for (idx = 0; idx < v.size(); idx++) // 대기열에 우선순위가 더 높은 문서가 존재하는지 확인함.
        {
            if (doc.priority < v[idx].priority) // 우선순위가 더 높은 문서가 존재한다면 그 문서를 맨 뒤로 보냄.
            {
                v.push_back(doc); 
                order--;

                break;   
            }
        }

        if (idx == v.size())
        {
            if (doc.location == location)
            {
                return order;
            }
        }
    }
}