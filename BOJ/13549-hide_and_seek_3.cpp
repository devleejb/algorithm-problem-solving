#include <stdio.h>
#include <queue>

using namespace std;

int N, K, time = 123456789;
int visited[100001], timePos[100001];

void BFS() {
	queue<int> pq, tq;
	int tmpPos, tmpTime;
	
	pq.push(N);
	tq.push(0);
	
	while (!pq.empty()) {
		tmpPos = pq.front();
		tmpTime = tq.front();
		
		pq.pop();
		tq.pop();
		
		if (tmpPos == K && time > tmpTime) {
			time = tmpTime;
		}
		
		if (tmpPos - 1 >= 0 && (visited[tmpPos - 1] == 0 || timePos[tmpPos -1] > tmpTime)) {
			pq.push(tmpPos - 1);
			tq.push(tmpTime + 1);
			visited[tmpPos - 1] = 1;
			timePos[tmpPos - 1] = tmpTime + 1;
		}
		
		if (tmpPos + 1 <= 100000 && (visited[tmpPos + 1] == 0 || timePos[tmpPos + 1] > tmpTime)) {
			pq.push(tmpPos + 1);
			tq.push(tmpTime + 1);
			visited[tmpPos + 1] = 1;
			timePos[tmpPos + 1] = tmpTime + 1;
		}
		
		if (tmpPos * 2 <= 100000 && (visited[tmpPos * 2] == 0 || timePos[tmpPos * 2] > tmpTime)) {
			pq.push(tmpPos * 2);
			tq.push(tmpTime);
			visited[tmpPos * 2] = 1;
			timePos[tmpPos * 2] = tmpTime; 
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &K);
	
	visited[N] = 1;
	
	BFS();
	
	printf("%d", time);
	
	return 0;
}