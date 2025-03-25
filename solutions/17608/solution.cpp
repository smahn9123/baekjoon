#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int numPillars;
    cin >> numPillars;

    stack<int> s;
    
    for (int i = 0; i < numPillars; i++) {
        int height;
        cin >> height;

        while (!s.empty() && s.top() <= height)
            s.pop();

        s.push(height);
    }

    cout << s.size() << '\n';

    return 0;
}
