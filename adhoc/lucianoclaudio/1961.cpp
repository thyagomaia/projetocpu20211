#include <bits/stdc++.h>

using namespace std;

int main(){

    vector<int> canos;
    int i,p,n,x;
    bool pulo;

    cin >> p >> n;

    for (i=0;i<n;i++){
        cin >> x;
        canos.push_back(x);
    }
    for (i=0;i<n-1;i++){
        if(abs(canos[i]-canos[i+1]) <= p){
            pulo=true;
        }
        else{
            pulo=false;
            break;
        }
    }
    if(pulo==true){
        cout << "YOU WIN\n";
    }
    else {
        cout << "GAME OVER\n";
    }

    return 0;
}