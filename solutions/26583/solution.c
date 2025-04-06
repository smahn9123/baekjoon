#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1000

int main() {
    char line[MAX_LEN];

    while (fgets(line, sizeof(line), stdin)) {
        int numbers[100], result[100];
        int count = 0;

        char* token = strtok(line, " \n");
        while (token != NULL) {
            numbers[count++] = atoi(token);
            token = strtok(NULL, " \n");
        }

        for (int i = 0; i < count; ++i) {
            int a = (i > 0) ? numbers[i - 1] : 1;
            int b = numbers[i];
            int c = (i < count - 1) ? numbers[i + 1] : 1;
            result[i] = a * b * c;
        }

        for (int i = 0; i < count; ++i) {
            if (i > 0) printf(" ");
            printf("%d", result[i]);
        }
        printf("\n");
    }

    return 0;
}
