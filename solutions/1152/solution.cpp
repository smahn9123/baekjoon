#include <iostream>
#include <string>

using namespace std;

int main() {
  string s;
  int count = 0;

  getline(cin, s);

  for (size_t i = 0; i < s.length(); i++) {
    if ((s[i] != ' ') && (i + 1 == s.length() || s[i + 1] == ' ')) count++;
  }

  cout << count;
  return 0;
}
