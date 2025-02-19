#include <iostream>

using namespace std;

int main() {
  int n, x = 0, y = 0;
  char result;
  cin >> n;
  while (n--) {
    cin >> result;
    if (result == 'D')
      x++;
    else
      y++;
    if (x - y >= 2 || y - x >= 2) break;
  }
  cout << x << ':' << y << endl;
  return 0;
}