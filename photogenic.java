import java.util.Scanner;

class photogenic
{
    
    void main()
    {
        Scanner sc=new Scanner(System.in);
        int t=0;
        int k,ce=0,co=0;
        t=sc.nextInt();
        int[] l=new int[t];
        for (int i=0;i<=t;i++)
        {
            k=l[i];
            if (k%2==0)
            {
                ce++;
            }
            else
            {
                co++;
            }
        }
        System.out.println(ce+" "+co);
sc.close();
    }
}