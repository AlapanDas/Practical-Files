#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 100000007
int main()
{
     ll t;
     while(t--)
     {
          ll n;  cin>>n;
          ll arr[n];
          for (int i = 0; i < n; i++)
          {
                cin>>arr[i];
          }

          sort(arr,arr+n);
          
          for (int i = 0; i < (n+1)/2; i++)
          {     
               if(arr[i]==arr[n/2 +i])
               { 
                    cout<<"NO"<<endl; 
                    continue ;
               }
          }
          
          if(n&1==0 and arr[0]==arr[n/2 -1] and arr[n/2]==arr[n-1]) 
          { 
               cout<<"NO"<<endl; 
               continue ;
          }
          cout<<"YES"<<endl;
          for (int i = 0; i < n; i++)
          {
               cout<<arr[i]<<" ";
          }
          cout<<endl;
          for (int i = (n+1)/2; i < n; i++)
          {
               cout<<arr[i]<<" ";
          }
          for (int i = 0; i < (n+1)/2; i++)
          {
               cout<<arr[i]<<" ";
          }
          cout<<endl; 
     }
     return 0;
}