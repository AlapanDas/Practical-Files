public class reverse {
     public String reverse_string(String str){
          String newstr="";
          for( int i=str.length();i>0;i--)
               newstr+=str.charAt(i);
          return newstr;
     }
     public static void main(String[] args) {
          String s="I am a Boy";
          String s1[]= s.split(" ");
          String temp;
          String ans="";
          reverse obj= new reverse();
          for( String i :s1){
               temp=obj.reverse_string(i);
               ans=ans.concat(temp);
          }
          System.out.println(ans);
     }
}
