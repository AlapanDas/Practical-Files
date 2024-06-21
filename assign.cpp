#include <bits/stdc++.h>
using namespace std;

class complex
{
     int x, y;
public:   
     complex(int i=0, int j=0)
     {
          x = i;
          y = j;
     }
     void show()
     {
          cout<<x<<"+i"<<y<<endl;
     }
     // void operator>=(complex &c1)
     // {
     //      if (c.x >= c1.x and c.y >= c1.y)
     //           return true;
     //      else
     //           return false;
     // }
     complex operator+(complex& c)
     {
          complex temp(0,0);
          temp.x = y + c.x;
          temp.y = y + c.y;
          return temp;
     }
};

int main()
{
    complex c1(10, 5),  c2(2, 4), c3(0,0);
    c3 = c1 + c2;
    c3.show();
}