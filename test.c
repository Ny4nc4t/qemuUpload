#include <stdio.h>
#include <string.h>

int lt(int x, int y) {
	return x < y;
}
int gt(int x, int y) {
	return x > y;
}

int sort(int a[], int len, int (*f)(int, int) {
	(f*)(a[len], a[len+1]);
	return 0;
}

int sort2(int a[], int b[], int len) {
	sort( a, len, &lt );
	sort( b, len, &gt );
	return 0;
}

int main(int argc, char** argv) {
	int ia[10];
	int ib[10];
	sort2(ia, ib, argc);
	return 0;
}
