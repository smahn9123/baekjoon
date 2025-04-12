#include <stdio.h>
#include <string.h>

int main() {
    char codename[101];
    int order = 1;
    int found = 0;

    while (fgets(codename, sizeof(codename), stdin)) {
        if (strstr(codename, "FBI") != NULL) {
            printf("%d ", order);
            found = 1;
        }
        order++;
    }

    if (!found)
        printf("HE GOT AWAY!");

    return 0;
}
