#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE 1000
#define MAX_WORDS 100

int main() {
    int n;
    scanf("%d", &n);
    getchar(); // 개행 문자 제거

    for (int i = 1; i <= n; i++) {
        char line[MAX_LINE];
        char* words[MAX_WORDS];
        int word_count = 0;

        fgets(line, sizeof(line), stdin);
        line[strcspn(line, "\n")] = '\0';  // 개행 제거

        char* token = strtok(line, " ");
        while (token != NULL) {
            words[word_count++] = token;
            token = strtok(NULL, " ");
        }

        printf("Case #%d: ", i);
        for (int j = word_count - 1; j >= 0; j--) {
            printf("%s", words[j]);
            if (j != 0) printf(" ");
        }
        printf("\n");
    }

    return 0;
}
