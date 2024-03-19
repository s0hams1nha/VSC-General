#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 4; // Maximum number of stations

int assembly_line_scheduling(int a[2][MAXN], int t[2][MAXN-1], int e[2], int x[2], int n) {
    int f1[MAXN] = {0};
    int f2[MAXN] = {0};
    
    f1[0] = e[0] + a[0][0];
    f2[0] = e[1] + a[1][0];
    
    for (int i = 1; i < n; ++i) {
        f1[i] = min(f1[i-1] + a[0][i], f2[i-1] + t[1][i-1] + a[0][i]);
        f2[i] = min(f2[i-1] + a[1][i], f1[i-1] + t[0][i-1] + a[1][i]);
    }
    
    return min(f1[n-1] + x[0], f2[n-1] + x[1]);
}

int main() {
    int a[2][MAXN], t[2][MAXN-1], e[2], x[2], n;

    cout << "Enter number of stations (<= " << MAXN << "):" << endl;
    cin >> n;

    // Input for array a
    cout << "Enter task times for assembly lines (2x" << MAXN << "):" << endl;
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < MAXN; ++j)
            cin >> a[i][j];

    // Input for array t
    cout << "Enter transfer times for assembly lines (2x" << MAXN << "):" << endl;
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < MAXN; ++j)
            cin >> t[i][j];

    // Input for array e (entry times)
    cout << "Enter entry times for assembly lines (2 elements):" << endl;
    for (int i = 0; i < 2; ++i)
        cin >> e[i];

    // Input for array x (exit times)
    cout << "Enter exit times for assembly lines (2 elements):" << endl;
    for (int i = 0; i < 2; ++i)
        cin >> x[i];

    // Input for number of stations

    cout << "Fastest time: " << assembly_line_scheduling(a, t, e, x, n) << endl;

    return 0;
}
