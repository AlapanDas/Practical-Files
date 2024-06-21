#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
     ll t;cin>>t;
     while(t--)
     {
            ll n;
            ll arr[n];
            ll cnt=0;
          for (int  i = 0; i < n; i++)
          {
               cin>>arr[i];
               cnt+=arr[i];               
          }
         cnt*=2;
         (cnt%n==0  and (cnt/n)&1==0)?cout<<"YES"<<endl:cout<<"NO"<<endl;
     }
}