#include <stdio.h>
#include <string.h>

int main() {
  char input[8];
  scanf("%7s", input);  // 개행 전까지 문자열 입력 받기

  if (strncmp(input, "555", 3) == 0) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }

  return 0;
}
