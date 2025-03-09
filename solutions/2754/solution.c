#include <stdio.h>
#include <string.h>

int main() {
  char *grades[] = {"A+", "A0", "A-", "B+", "B0", "B-", "C+",
                    "C0", "C-", "D+", "D0", "D-", "F"};
  char *scores[] = {"4.3", "4.0", "3.7", "3.3", "3.0", "2.7", "2.3",
                    "2.0", "1.7", "1.3", "1.0", "0.7", "0.0"};

  char input[3];
  scanf("%s", input);

  for (int i = 0; i < 13; i++) {
    if (strcmp(input, grades[i]) == 0) {
      printf("%s\n", scores[i]);
      break;
    }
  }

  return 0;
}
