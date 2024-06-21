#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
     ll t;cin>>t;
     while(t--)
     {
          ll n,x; cin>>n>>x;
          int arr[n];
          for (int i = 0; i < n; i++)
          {
               cin>>arr[i];
          }
          // for single target
          ll count_for_single=0,count_for_multi=0;
          count_for_multi=*max_element(arr,arr+n);
          auto max_index=find(arr,arr+n,*max_element(arr,arr+n));
          for (int i = 0; i < n; i++)
          {
               if(count(arr,arr+n,0)==n)   break;
               arr[i]=arr[i]-x;
               if(arr[i]<0) arr[i]=0;
               count_for_single++;
          }
          cout<<min(count_for_multi,count_for_single)<<endl;
          
     }
}