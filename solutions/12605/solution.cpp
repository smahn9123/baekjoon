#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 1; i <= n; ++i) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        vector<string> words;
        string word;

        while (ss >> word) {
            words.push_back(word);
        }

        cout << "Case #" << i << ": ";
        for (int j = words.size() - 1; j >= 0; --j) {
            cout << words[j];
            if (j != 0) cout << " ";
        }
        cout << "\n";
    }

    return 0;
}
