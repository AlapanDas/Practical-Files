#include <iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter Number";
    cin>>n;
    int arr[n+1];
    for (int i = 0; i<n+1; i++)
    {
        arr[i]=1;
    }
    arr[0]=0;
    arr[1]=0;
    for (int i = 2; i*i<=n; i++)
    {
        for (int  j = i*2; j <=n; j+=i)
        {
            arr[j]=0;
        }        
    }
    cout<<"Prime Numbers:"<<endl;
    for (int i = 0; i <=n; i++)
    {
        if (arr[i]==1)
            cout<<i<<endl;        
    }
    
}