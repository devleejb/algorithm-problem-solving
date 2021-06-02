#include <stdio.h>
#include <queue>

using namespace std;

int S;
int visited[2000][2000];
queue<int> cntq, cbq, timeq;

int BFS() {
	int tmpCnt, tmpCb, tmpTime;
	
	cntq.push(1);
	cbq.push(0);
	timeq.push(0);
	
	while (!cntq.empty()) {
		tmpCnt = cntq.front();
		tmpCb = cbq.front();
		tmpTime = timeq.front();
		
		cntq.pop();
		cbq.pop();
		timeq.pop();
		
		// 1st op
		if (visited[tmpCnt][tmpCnt] == 0) {
			cntq.push(tmpCnt);
			cbq.push(tmpCnt);
			timeq.push(tmpTime + 1);
			visited[tmpCnt][tmpCnt] = 1;
		}
		
		// 2nd op
		if (tmpCb != 0 && tmpCnt + tmpCb < 2000 && visited[tmpCnt + tmpCb][tmpCb] == 0) {
			cntq.push(tmpCnt + tmpCb);
			cbq.push(tmpCb);
			timeq.push(tmpTime + 1);
			visited[tmpCnt + tmpCb][tmpCb] = 1;
		}
		
		// 3rd op
		if (tmpCnt != 0 && visited[tmpCnt - 1][tmpCb] == 0) {
			cntq.push(tmpCnt - 1);
			cbq.push(tmpCb);
			timeq.push(tmpTime + 1);
			visited[tmpCnt - 1][tmpCb] = 1;
		}
			
		if (tmpCnt == S || tmpCnt + tmpCb == S || tmpCnt - 1 == S) {
			return tmpTime + 1;
		}
	}
	
	return 0;
}


int main(void) {
	scanf("%d", &S);
	
	printf("%d", BFS());
	
	return 0;
}