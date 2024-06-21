#include<stdio.h>
int main()
{
    int i,j;
    int n;
    printf("Enter number");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<i;j++)
        {
            printf(" ");
        }
        for(j=n-i+1;j>=1;j--)
        {
            printf("%d",j);
        }
        printf("\n");
    }

    return 0;
}
