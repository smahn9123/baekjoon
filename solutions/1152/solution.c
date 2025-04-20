#include <stdio.h>

char s[1000001];

int main() {
  int count = 0;

  fgets(s, sizeof(s), stdin);

  for (int i = 0; s[i]; i++) {
    if ((s[i] != ' ' && s[i] != '\n') &&
        (s[i + 1] == ' ' || s[i + 1] == '\n' || s[i + 1] == '\0'))
      count++;
  }

  printf("%d", count);
  return 0;
}