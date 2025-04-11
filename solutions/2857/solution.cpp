#include <iostream>
#include <string>

using namespace std;

int main() {
    string codename;
    bool found = false;
    int order = 1;

    while (getline(cin, codename)) {
        if (codename.find("FBI") != string::npos) {
            cout << order << " ";
            found = true;
        }
        order++;
    }

    if (!found)
        cout << "HE GOT AWAY!";

    return 0;
}
