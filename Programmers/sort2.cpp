#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(string a, string b) {
    return a + b > b + a ? true : false; // a + b가 더 크다면 true를 b + a가 더 크다면 false를 반환한다.
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> numbers_;
    int size = numbers.size();
    int idx; // input의 모든 원소가 0인지 확인하기 위한 변수

    for (idx = 0; idx < size; idx++)
    {
        if (numbers[idx] != 0)
        {
            break;
        }
    }

    if (idx == size)
    {
        return "0"; // input의 모든 원소가 0이라면 "0"를 반환한다.
    }

    for (int i = 0; i < size; i++)
    {
        numbers_.push_back(to_string(numbers[i])); // string vector 생성
    }
    
    sort(numbers_.begin(), numbers_.end(), compare); // compare 함수를 기준으로 정렬한다.

    for (int i = 0; i < size; i++)
    {
        answer += numbers_[i]; // 정답 생성
    }

    return answer;
}

// int main() {
//     vector<int> numbers;

//     numbers.push_back(6);
//     // numbers.push_back(10);
//     // numbers.push_back(2);

//     cout << solution(numbers);

//     return 0;
// }