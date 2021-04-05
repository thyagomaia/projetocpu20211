#include <bits/stdc++.h>

using namespace std;

int main(){

    int t,q;
    double a,b,area;

    cin >> t;
    while(t>0){
        for (int i=1;i<=t;i++){
            cin >> q >> a >> b;
            area = (a+b)*5/2;
            area *= q;
            cout << "Size #" << i << ":\n";
            cout << fixed << setprecision(2);
            cout << "Ice Cream Used: " << area << " cm2\n";
        }
        cout << "\n";
        cin >> t;
    }
    

    return 0;
}