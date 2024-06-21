#include <stdio.h>
#include <string.h>
void prog1(){
    int marks;
    printf("Enter Marks\n");
    scanf("%d",&marks);
    printf((marks>=0 && marks<=100)?(marks>50)?"Pass\n":"Fail\n":"Wrong Input\n");
     
}
void prog2(){        
    printf("Enter Character\n");
    char k;
    scanf("%c",&k);
    printf((k=='a'||k=='e'||k=='o'||k=='i'||k=='u')?"Vowel\n":"Consonant\n");
}
void prog3(){    
    printf("Enter Character\n");
    char k;
    scanf("%c",&k);    
    printf(((k >= 'a' && k <= 'z') || (k >= 'A' && k <= 'Z') )?"Alphabets\n":"Special Character\n");
     
}
void prog4(){
    int i;
    printf("Enter Number\n");
    scanf("%d",&i);
    printf(((i&1) == 1)?"Odd":"Even");
     
}
void prog5()
{
    int n,max=0;
    printf("How many numbers?\n");
    scanf("%d",&n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        int k;
        scanf("%d",&k);
        if (k>max) max=k;
        arr[i]=k;
    }
    printf("Maximum=%d\n",max);
     
}
void prog6(){
    int num;
    printf("Enter Number\n");
    scanf("%d",&num);
    for (int i = 1; i <11; i++)
    {
        printf("%d*%d=%d\n",i,num,(i*num));
    }
     
}
void prog7(){
    char ch;
    printf("Enter Character\n");
    scanf("%c",&ch);
    printf((ch>='a' && ch<='z')?"Lower":"Upper");
     
}
void prog8(){
    printf("Sum of 1st 10 numbers =55");
     
}
int main(){
    printf("\n");
    prog8();
    printf("\n");
    return 0;
}
