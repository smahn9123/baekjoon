#include <iostream>

using namespace std;

int main() {
  int a, b, c, d, e;
  int total = 0;
  cin >> a >> b >> c >> d >> e;
  total = a < 0 ? -a * c + d + b * e : (b - a) * e;
  cout << total << endl;
  return 0;
}