#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define pb push_back
#define pll pair<ll,ll>
#define all(a) (a).begin(),(a).end()
#define oset ordered_set
#define rep(i,j,k) for(ll i=j;i<k;i++)
int main()
{
     ll t; 
     cin>>t;
     while(t--)
     {
          int n;
          cin>>n;
          int a[n];
          for(ll i=0;i<n;i++) 
               cin>>a[i];
          unordered_map<int,int> mp;
          for (int i = 0; i < n; i++)
          {
               mp[a[i]]++;
          }
          int m=0;
          for (int i = 0; i < n; i++)
          {
               m=max(m,mp[a[i]]);
          }
          cout<<(n-m)<<endl;
          
     }
 return 0;
}