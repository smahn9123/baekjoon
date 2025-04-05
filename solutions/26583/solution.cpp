#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        stringstream ss(line);
        vector<int> numbers;
        int num;

        while (ss >> num)
            numbers.push_back(num);

        vector<int> result;
        for (size_t i = 0; i < numbers.size(); ++i) {
            int a = (i > 0) ? numbers[i - 1] : 1;
            int b = numbers[i];
            int c = (i < numbers.size() - 1) ? numbers[i + 1] : 1;
            result.push_back(a * b * c);
        }

        for (size_t i = 0; i < result.size(); ++i) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << '\n';
    }

    return 0;
}
