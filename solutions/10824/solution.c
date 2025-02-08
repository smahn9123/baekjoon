#include <stdio.h>
#include <stdlib.h>

int main() {
  char a[8], b[8], c[8], d[8], n1[16], n2[16];
  long long n_1, n_2;
  scanf("%s %s %s %s", &a, &b, &c, &d);
  sprintf(n1, "%s%s", a, b);
  sprintf(n2, "%s%s", c, d);
  n_1 = strtoll(n1, NULL, 10);
  n_2 = strtoll(n2, NULL, 10);
  printf("%lld\n", n_1 + n_2);
  return 0;
}