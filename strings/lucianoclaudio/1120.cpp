#include <bits/stdc++.h>

using namespace std;

int main ( ) {

    string n;
    char d;
    int num=1;
    int tam;

    cin >> d >> n;
    tam = n.size();
    if (tam==1){
        num = stoi(n);
    }
    while(d!=0 && num!=0){

        tam = n.size();
        for (int i=tam-1;i>=0;i--){
            if (n[i]==d){
                n.erase(n.begin()+i);
            }
        }

        tam = n.size();
        for (int i=0;i<tam;i++){
            if (n[i]=='0'){
                n.erase(n.begin()+i);
                tam = n.size();
                i--;
            }
            else{
                break;
            }
        }

        tam = n.size();
        if (tam==0){
            n.push_back('0');
        }

        cout << n << "\n";

        cin >> d >> n;
        tam = n.size();
        if (tam==1){
            num = stoi(n);
        }
    
    }
    return 0;
}