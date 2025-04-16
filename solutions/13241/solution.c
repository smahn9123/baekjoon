#include <stdio.h>

long long gcd(long long a, long long b) {
  while (b != 0) {
    long long r = a % b;
    a = b;
    b = r;
  }
  return a;
}

int main() {
  long long a, b;
  scanf("%lld %lld", &a, &b);

  long long g = gcd(a, b);
  long long lcm = (a / g) * b;

  printf("%lld\n", lcm);

  return 0;
}
