#include <bits/stdc++.h>
using namespace std;
#define ll long long
#include  <vector>
#define mod 100000007

int main()
{
     ll n;cin>>n;
     ll arr[n];
     vector<ll> v1;
     vector<ll> v2;
     for(int i=0;i<n;i++){ 
          cin>>arr[i];
          (arr[i]>=0)?v1.push_back(arr[i]):v2.push_back(arr[i]);
     }     
     // 0123456..
     for (int i = 0; i < v1.size(); i+=2)
     {
          arr[i]=v1[i];
     }
      for (int i = 0; i < v2.size(); i+=2)
     {
          arr[i+1]=v2[i];
     }
     for (int i = 0; i < n; i++)
     {
          cout<<arr[i];
     }     
}