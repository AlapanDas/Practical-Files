#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 10000007
void merge(int arr[],int const l,int const mid, int const r)
{
    auto const n=mid-l+1;
    auto const m=r-mid;

    auto *leftarray=new int[n];
    auto *rightarray=new int[m];
     for(auto i=0;i<n;i++)
          leftarray[i]=arr[l+1];
     for (auto j = 0; j < m; j++)
          rightarray[j]=arr[mid+1+j];     
     auto a=0;
     auto b=0;
     int c=l;
     while(a<n and b<m)
     {
          if(leftarray[a]<=rightarray[b])
          { 
               arr[c]=leftarray[a];
               a++;
          }
          else
          {
               arr[c]=rightarray[b];
               b++;
          }
     }
     while (a<n)
     {
          arr[c]=leftarray[a];
          c++;a++;
     }
     
     while(b<m)
     {
          arr[c]=rightarray[b];
          c++;
          b++;
     }
     
}
void mergesort(int arr[], int l, int r)
{
     if(l>=r) return;
     
     auto mid=(l+r-l)/2;
     mergesort(arr,l,mid);
     mergesort(arr,mid+1,r);
     merge(arr,l,mid,r);

}
int main()
{
//     time_t start,end;
//     time(&start);
    int n;
    cin>>n;
    int arra[n];
    for (int i = 0; i < n; i++)
    {
         cin>>arra[i];
    }
    mergesort(arra,0,n-1);
    for (int i = 0; i < n; i++)
    {
         cout<<arra[i]<<endl;
    }
    
//     cout<<double(end-start)<<setprecision(5)<<endl;

}