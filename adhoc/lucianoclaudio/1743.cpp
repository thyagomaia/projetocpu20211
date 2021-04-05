#include <bits/stdc++.h>

using namespace std;

int main(){

    bool x[5],y[5],c;

        cin >> x[0] >> x[1] >> x[2] >> x[3] >> x[4];
    
        cin >> y[0] >> y[1] >> y[2] >> y[3] >> y[4];

    for (int i=0;i<5;i++){
        if(x[i]!=y[i]){
            c=true;
        }
        else{
            c=false;
            break;
        }
    }
    if (c==true){
        cout << "Y\n";
    }
    else {
        cout << "N\n";
    }

    return 0;
}