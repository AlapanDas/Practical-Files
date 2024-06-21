/*
This Program is to print diamond pattern
1          *
2        *****
3      *********
4        *****
5          *
    when n=3
           
*/
#include<stdio.h>
int main()
{
    int i,j,n;
    printf("enter number");
    scanf("%d",&n);

    for(i=1;i<=n;i++)
    {
        for(j=n-i;j>=1;j--)
            printf(" ");
        for(j=1;j<=i;j++)
            printf("%d",j);
        for(j=1;j<=i-1;j++)    
            printf("%d",j);
        printf("\n");
    }
    /*
    for(i=1;i<=n-1;i++)
    {
        for(j=1;j<=i;j++)
            printf(" ");
        for (j=1;j<=n-i;j++)
            printf("*");
        for (j=1;j<=n-1-i;j++)
            printf("*");
        printf("\n");
    }
    */
    return 0;
}
