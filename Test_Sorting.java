import java.util.*;
import Ascending.A_Sort;
import Descending.D_Sort;

public class Test_Sorting implements A_Sort, D_Sort {
    public static void main(String[] args){
        var sc = new Scanner(System.in);
        int n = sc.nextInt();
        Integer[] arr = new Integer[n];
        for(int i = 0; i < n; i++){
            String s = sc.next();
            arr[i] = Integer.parseInt(s);
        }
        Test_Sorting ts = new Test_Sorting();
        ts.sort(arr);
        sc.close();
    }

    @Override
    public void sort(Integer[] arr) {
        System.out.println("Ascending Sort");
        A_Sort.super.sort(arr);
        System.out.println("Descending Sort");
        D_Sort.super.sort(arr);
    }
}
