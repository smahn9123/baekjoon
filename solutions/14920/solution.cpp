#include <iostream>

using namespace std;

int main() {
  int x, n = 1;
  cin >> x;
  while (x != 1) {
    n++;
    x = x % 2 == 0 ? x / 2 : 3 * x + 1;
  }
  cout << n << endl;
  return 0;
}