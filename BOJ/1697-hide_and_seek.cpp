#include <stdio.h>
#include <queue>

using namespace std;

int N, K, time;
int pos[100001], visited[100001];

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
		
		if (tmpPos == K) {
			time = tmpTime;
			return;
		}
		
		if (tmpPos - 1 >= 0 && visited[tmpPos - 1] == 0) {
			pq.push(tmpPos - 1);
			tq.push(tmpTime + 1);
			visited[tmpPos - 1] = 1;
		}
		
		if (tmpPos + 1 <= 100000 && visited[tmpPos + 1] == 0) {
			pq.push(tmpPos + 1);
			tq.push(tmpTime + 1);
			visited[tmpPos + 1] = 1;
		}
		
		if (tmpPos * 2 <= 100000 && visited[tmpPos * 2] == 0) {
			pq.push(tmpPos * 2);
			tq.push(tmpTime + 1);
			visited[tmpPos * 2] = 1;
		}
	}
}

int main(void) {
	scanf("%d %d", &N, &K);
	
	// 1 : A
	pos[N] = 1;
	visited[N] = 1;
	// 2 : B
	pos[K] = 2;
	
	BFS();
	
	printf("%d", time);
	
	return 0;
}