#include <bits/stdc++.h>
using namespace std;
#define ll long long
bool canAttack(ll qR, ll qC, ll oR, ll oC)
{
    if (qR == oR)
        return true;
    if (qC == oC)
        return true;
    if (abs(qR - oR) == abs(qC - oC))
        return true;
    return false;
}
int main()
{
    ll t;cin>>t;
    while(t--)
    {
      ll n,x,y; cin>>n>>x>>y;
      ll count=0;
      for (int i = 0; i < n; i++)
      {
        for (int j = 0; j < n; j++)
        {
          if(canAttack(x,y,i,j)) count++;
        }
      }
      cout<<count<<endl;
    }
    return 0;
}   