#include <bits/stdc++.h>

using namespace std;

int main(){

    int n,m;
    string first;
    bool sn=1;
    char a;

    cin >> n;
    for (int i=0;i<n;i++){
        cin >> m;
        vector<string> idioma;
        for (int u=0;u<m;u++){
            cin >> first;
            idioma.push_back(first);
        }
        for (int u=m-1;u>0;u--){
            if (idioma[u]==idioma[u-1]){
                sn=1;
            }
            else{
                sn=0;
                break;
            }
        }
        if (sn==1){
            cout << idioma[0] << "\n";
        }
        else{
            cout << "ingles\n";
        }
    }
    return 0;
}