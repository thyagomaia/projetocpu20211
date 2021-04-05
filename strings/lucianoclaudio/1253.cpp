#include <bits/stdc++.h>

using namespace std;

int main(){

    string a;
    int n,num;

    cin >> n;
    for (int i=0;i<n;i++){
        cin >> a;
        cin >> num;

        for (int i=0;i<a.size();i++){
            if((a[i]-num<65)){
                a[i]-=num;
                a[i]+=26;
            }
            else{
                a[i]-=num;
            }
            cout << a[i];
        }   
        cout << "\n";
    }
    return 0;
}