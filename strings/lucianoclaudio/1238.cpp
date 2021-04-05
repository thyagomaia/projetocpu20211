#include <bits/stdc++.h>

using namespace std;

int main(){

    string a,b;
    int n;

    cin >> n;

    for (int i=0;i<n;i++){
        int tam;
        cin >> a >> b;

        if(a.size()>=b.size()){
            tam = a.size();
        }
        else{
            tam = b.size();
        }

        for (int i=0;i<tam;i++){
            if (a.size()-1>= i){
                cout << a[i];
            }
            if (b.size()-1>= i){
                cout << b[i];
            }
        }
        cout << "\n";
    }
    return 0;
}