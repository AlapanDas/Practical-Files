#include<stdio.h>
int main(){
    int a=5;
    int y=5;
    int b=++a;
    printf("%d\n",b);
     b+=a++;
    printf("%d\n",b);
     b+=--a;
    printf("%d\n",b);
    int x=++y + y++ + --y;
    printf("%d\n",x);
}