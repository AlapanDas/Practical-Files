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
            printf("*");
        for(j=1;j<=i-1;j++)    
            printf("*");
        printf("\n");
    }
    for(i=1;i<=n/2;i++)
    {
      for(j=1;j<=(n*0.75);j++)
        printf(" ");
      for( j = 0; j <=(n/2) ; j++)
        printf("*");
     printf("\n");
    }
    return 0;
}
