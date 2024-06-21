#include <bits/stdc++.h>
using namespace std;
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
int n,k;
cin>>n;
int arr[n];
void selection()
{
	int i,j,min;
	for ( i = 0; i <n-1; i++)
	{
	     min=i;
		for (j = i+1; j < n; j++)
		{
			if(arr[min]<arr[j])
				min=j;
		}
		if(min!=i)
			swap(&arr[min],&arr[i]);
	}
}
int main(){
	
	for ( k = 0; k < n; k++)
	{
		cin>>arr[k];
	}
	for (int i = 0; i < n; i++)
	{
		cout<<arr[i]<<endl;
	}
	
}