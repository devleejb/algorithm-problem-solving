#include <stdio.h>

using namespace std;

int M, n;
int set;
char op[10];

int main(void) {
	int x; 
	
	scanf("%d", &M);
	
	for (int i = 0; i < M; ++i) {
		scanf("%s ", op);
		
		if (op[0] == 'a' && op[1] == 'd') {
			scanf("%d", &x);
			
			n |= 1 << x;
		} else if (op[0] == 'r') {
			scanf("%d", &x);
			
			n &= ~(1 << x);
		} else if (op[0] == 'c') {
			scanf("%d", &x);
			
			printf("%d\n", n & (1 << x) ? 1 : 0);
		} else if (op[0] == 't') {
			scanf("%d", &x);
			
			n ^= 1 << x;
		} else if (op[0] == 'a' && op[1] == 'l') {
			n = (1 << 21) - 1;
		} else if (op[0] == 'e') {
			n = 0;
		}
	}
	
	return 0;
}