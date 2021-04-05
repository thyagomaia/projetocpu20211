#include<bits/stdc++.h>

using namespace std;

int main(){

    int i,u,n,m,a;

    cin >> n >> m;
    while (n!=0&&m!=0){
        vector<vector<int>> num;
        int caracteristicas=0;
        int c1=0,c2=0,c3=0,c4=0;

        for (i=0;i<n;i++){
            vector<int> temp;
            for (u=0;u<m;u++){
                cin >> a;
                temp.push_back(a);
            }
            num.push_back(temp);
        }
        for (i=0;i<n;i++){
            for (u=0;u<m;u++){
                if(num[i][u]==0){
                    c1++;
                    break;
                }
            }
        }
        for (i=0;i<n;i++){
            for (u=0;u<m;u++){
                if(num[i][u]==1){
                    c4++;
                    break;
                }
            }
        }
        for (u=0;u<m;u++){
            for (i=0;i<n;i++){
                if(num[i][u]==1){
                    c2++;
                    break;
                }
            }
        }
        for (u=0;u<m;u++){
            for (i=0;i<n;i++){
                if(num[i][u]==0){
                    c3++;
                    break;
                }
            }
        }

        if(c1>=n){
            caracteristicas++;
        }
        if(c2>=m){
            caracteristicas++;
        }
        if(c3>=m){
            caracteristicas++;
        }
        if(c4>=n){
            caracteristicas++;
        }

        cout << caracteristicas << "\n";
        cin >> n >> m;

    }
    return 0;
}