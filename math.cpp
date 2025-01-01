// calculate area of a circle from radius
#include <iostream>
#include <cmath>

using namespace std;
const double pi = 3.14;

int main() {
    double radius;

    cout << "Enter radius: ";
    cin >> radius;

    if (cin.fail()) {
        cin.clear();
        cin.ignore(256, '\n');
        std::cout << "Invalid input. Please enter number" << endl;
        return 1;
    }

    cout << "Area: " << pi * pow(radius, 2) << endl;

    return 0;
}
