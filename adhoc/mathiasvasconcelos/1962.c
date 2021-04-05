#include<stdio.h>
int main()
{
    int i, n, ano;
    scanf("%d",&n);
    for (i = 0; i < n; i++) {
        scanf("%d",&ano);
        if (ano > 2015) printf("%d A.C.\n",ano-2014);
        else if(ano < 2015)printf("%d D.C.\n",2015-ano);
        else printf("1 A.C.\n");
    }
    return 0;
}