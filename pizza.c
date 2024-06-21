#include<stdio.h>
int t,i,j;
scanf("%d",t);
for (i=1;i<=t;i++)
{
    int n,k;
    scanf("%d %d",n,k);
    for(j=1;j<=n;j++)
    {
        if((i*k)%n==0)
        {
            printf(i);
            break;
        }
    }
}

