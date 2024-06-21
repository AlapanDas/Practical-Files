#include<stdio.h>

int main()
{
	int n;
	scanf("%d",&n);
	int flag,p,ne,z;
	for (int i = 0; i <=n; i++)
	{
		printf("Enter number");
		scanf("%d",flag);
		if(flag>0)
			p=p+1;
		if (flag<0)
			ne=ne+1;
		if (flag==0)
			z++;
	}
	printf("%d",(p/n));
	printf("%d",(ne/n));
	printf("%d",(z/n));
	return 0;
}