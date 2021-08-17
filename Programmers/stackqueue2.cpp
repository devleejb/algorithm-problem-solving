#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Truck {
    public:
        int wieght;
        int position;

        Truck(int weight, int position) {
            this->wieght = weight;
            this->position = position;
        }
};

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int total_weight = 0;
    int isComplete = 0;
    int size = truck_weights.size();
    vector<Truck> ing;

    while (1)
    {
        answer++;

        // 건너고 있는 트럭들에 대해 position을 하나씩 증가시키고, 다 건넌 트럭은 지움. 
        for (int i = 0; i != ing.size(); i++)
        {
            ing[i].position++;

            if (ing[i].position > bridge_length)
            {
                total_weight -= ing[i].wieght;
                ing.erase(ing.begin() + i);

                i--;
            }
        }

        // 다리를 모두 건넘.
        if (truck_weights.empty() && ing.empty())
        {
            break;
        }
            
        // 다리 위에 새로운 트럭이 올라갈 수 있다면 올림.
        if (((ing.empty() || (!ing.empty() && ing.begin()->position != 1))) && (!truck_weights.empty() && weight >= total_weight + *(truck_weights.begin())))
        {
            total_weight += *(truck_weights.begin());

            ing.push_back(Truck(*(truck_weights.begin()), 1));

            truck_weights.erase(truck_weights.begin());
        }
        
    }

    return answer;
}