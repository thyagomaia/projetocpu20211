#include <bits/stdc++.h>

using namespace std;

int main(){

    int n,t,ano;

    cin >> n;

    for (int i=0;i<n;i++){
        cin >> t;
        ano = 2015 - t;
        if(ano>0){
            cout << ano << " D.C.\n";
        }
        else {
            ano = abs(ano);
            ano++;
            cout << ano << " A.C.\n";
        }
    }

    return 0;
}