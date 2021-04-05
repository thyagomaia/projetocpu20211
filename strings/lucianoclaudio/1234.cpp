#include <bits/stdc++.h>

using namespace std;

int main ( ) {

    string dance;
    int tam;
    while(getline(cin,dance)){
        tam = dance.size();
        bool d=0;
            
        for (int i=0;i<tam;i++){
            if (dance[i]==' '){
                goto fim;
            }
            if (d==0){
                if(int(dance[i])>=97 && int(dance[i])<=122){ // minusculas
                    dance[i]-=32;
                    d=1;
                }
                else{
                    d=1;
                }
            }
            else{
                if(int(dance[i])>=65 && int(dance[i])<=90){ // maiusculas
                    dance[i]+=32;
                    d=0;
                }
                else{
                    d=0;
                }
            }
            fim:
            cout << dance[i];
        }
        cout << "\n";
    }    
    return 0;
}