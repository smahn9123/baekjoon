#include <stdio.h>
#include <string.h>

int main(void) {
	char s[101];
	scanf("%s", s);

	int len = strlen(s);

	for (int i = 0; i < len; i += 10) {
		fwrite(s + i, 1, (len - i >= 10 ? 10 : len - i), stdout);
		putchar('\n');
	}

	return 0;
}
