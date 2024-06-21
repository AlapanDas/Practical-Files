import  java.util.Arrays;
import java.util.*;
public class prac2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();                
        for (int i = 0; i < t; i++) {
            int n=sc.nextInt();
            int arr[]=new int[n];
            for (int j=0;j<n;j++)
            {
                arr[j]=n-j;
            }
            for (int k = 1; k < n; k++) {
                System.out.println(Arrays.copyOfRange(arr, 0, n-k)+"1"+(Arrays.copyOfRange(arr, n-k, n-1)));
            }
        }
        sc.close();
    }
}
