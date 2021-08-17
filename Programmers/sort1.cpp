#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// array vector와 자를 start, end 변수와 그 구간 안에서의 idx를 인자로 받아 계산 결과값을 반환한다.
int calculate(vector<int> array, int start, int end, int idx) {
    vector<int> temp; // 필요한 구간의 원소를 담기 위한 임시 vector

    for (int i = start; i <= end; i++)
    {
        temp.push_back(array[i]); // temp vector에 필요한 구간의 원소를 담는다.
    }

    nth_element(temp.begin(), temp.begin() + idx, temp.end()); // 임시 vector에서 idx번째 원소를 찾을 때까지 정렬한다.

    return temp[idx];
}

// commands의 원소에 알맞게 caculate 함수를 호출한 계산 결과값을 answer vector에 담고 반환한다. 
vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    int size = commands.size();

    for ( int i = 0; i < size; i++)
    {
        answer.push_back(calculate(array, commands[i][0] - 1, commands[i][1] - 1, commands[i][2] - 1)); // answer vector에 계산된 결과를 담는다.
    }
    
    return answer;
}

// int main() {
//     vector<int> array;
//     vector<vector<int>> commands;
//     vector<int> tmp;

//     array.push_back(1);
//     array.push_back(5);
//     array.push_back(2);
//     array.push_back(6);
//     array.push_back(3);
//     array.push_back(7);
//     array.push_back(4);

//     tmp.push_back(2);
//     tmp.push_back(5);
//     tmp.push_back(3);

//     commands.push_back(tmp);

//     cout << solution(array, commands).at(0);

//     return 0;
// }