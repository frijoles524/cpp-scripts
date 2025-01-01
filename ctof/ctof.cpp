#include <iostream>
#include <libctof.h>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " (-cf for c to f or -fc for f to c)" << endl;
        return 1;
    }

    if (strcmp(argv[1], "-cf") > 0 && strcmp(argv[1], "-fc") > 0) {
        cout << "Error: Invalid argument" << endl;
        return 1;
    }

    bool mode = (strcmp(argv[1], "-cf") == 0);

    cout << "Enter degrees: ";

    double input;
    cin >> input;

    if (cin.fail()) {
        cin.clear();
        cin.ignore(256, '\n');
        cout << "Invalid input. Please enter a number" << endl;
        return 1;
    }

    cout << "Degrees in " << (mode ? "F: " : "C: ") << (mode ? celsius_to_fahrenheit(input) : fahrenheit_to_celsius(input)) << endl;

    return 0;
}
