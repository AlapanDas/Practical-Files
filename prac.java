import java.util.Scanner;
class solution{
void Solution(){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for (int i = 0; i < t; i++) {
                int n=sc.nextInt();
                int c=sc.nextInt();
                show(n,c);
        }
    }
static void show(int n,int c){
    for (int row = 0; row <(2*n)+1; row++) {
        for (int col = 0; col <=2*c; col++) {
            if((row==0&&col==0)||(row==0&&col==1)||(row==1&&col==1)||(row==1&&col==0)){
                System.out.print('.');
            }
            else if((row%2!=0&&col%2!=0))
                System.out.print('.');
            else if((row%2!=0&&col%2==0))
                System.out.print('|');
            else if((row%2==0&&col%2==0))
                System.out.print('+');
            else if((row%2==0&&col%2!=0))
                System.out.print('-');
        }
        System.out.println("");
    }
}
}