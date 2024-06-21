#include<bits/stdc++.h>
using namespace std;

class A
{
public:
     int x=9,y=3;
     void show(){ cout<<x<<y<<endl; }
};
class B
{
public:
     int x=6,y=2;
     void show(){ cout<<x<<y<<endl; }
};
class C: public A, public B
{
     
public:
     int x=3,y=1;
     void show(){ cout<<x<<y<<endl; }     
};

int main()
{
     C c;
     // Calling the Function of the Base Class
     cout<<c.x<<endl;
     //  Printing the variable of the A class
     cout<<c.A::x<<endl;
     //  Printing the variable of the B class
     cout<<c.B::x<<endl;
}