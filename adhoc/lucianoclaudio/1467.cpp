#include <bits/stdc++.h>

using namespace std;

int main(){

    int a,b,c;
    cin >> a >> b >> c;
	while (!cin.eof()){
        if (a==b){
            if (a==c){
                cout << "*\n";
            }
            else{
                cout << "C\n";
            }
        }
        else{
            if (a==c){
                cout << "B\n";
            }
            else{
                cout << "A\n";
            }
        }
    cin >> a >> b >> c;
    }
    return 0;
}