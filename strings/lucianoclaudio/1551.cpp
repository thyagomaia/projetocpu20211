#include <bits/stdc++.h>

using namespace std;

int main(){

    string a;
    int n;

    cin >> n;
    cin.ignore(INT_MAX, '\n');
    for (int i=0;i<n;i++){
        int l=0;
        getline(cin,a);
        string alfa="abcdefghijklmnopqrstuvwxyz";
        for (int u=0;u<a.size();u++){
            for (int j=alfa.size();j>=0;j--){
                if (a[u]==alfa[j]){
                    l++;
                    alfa.erase(alfa.begin()+j);
                    if (j==0){
                        break;
                    }
                }
            }
        }
        if (l==26){
            cout << "frase completa\n";
        }
        else{
            if (l>13){
                cout << "frase quase completa\n";
            }
            else{
                cout << "frase mal elaborada\n";
            }
        }
    }
    return 0;
}