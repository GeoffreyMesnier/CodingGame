#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int tempMin = 0;
int main()
{
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        if (tempMin == 0){
            tempMin = t;
        }
        else if (abs(t) < abs(tempMin)){
                tempMin = t;
            }
        else if (abs(t) == abs(tempMin)){
                tempMin = abs(t);
            }
        }

    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << tempMin << endl;
}
