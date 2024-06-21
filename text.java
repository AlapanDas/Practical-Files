import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;

class custom_thread extends Thread
{
  List < Integer > input_array;
  List < Integer > res_array;
  int m_code;
  int status = 0;
  int sum = 0;
  int temp=0,r=0;


    custom_thread (int code, List < Integer > array)
  {
    input_array = new ArrayList < Integer > (array);
    ++status;
    m_code = code;
    start ();
  }

  public void run ()
  {
    res_array = new ArrayList < Integer > ();
    if (m_code == 1)
      {
      for (int i:input_array)
	  {
	    if (i % 7 == 0)
	      res_array.add (i);
	  }
	++status;
      }
    else if (m_code == 2)
      {
      for (int i:input_array)
	  { 
	    
	    temp = i;
	    sum=0;
	    while (i > 0)
	      {
		r = i % 10;
		sum = sum + (r * r * r);
		i = i / 10;
	      }
	      
	    if (temp==sum)
	      res_array.add (1);
	    else
	      res_array.add (0);
	  }
	++status;
      }
    else
      System.out.println ("Wrong code");
  }

  List < Integer > get_res_array ()
  {
    if (status == 2)
      return res_array;
    else
      {
	System.out.println ("Something went wrong");
	return new ArrayList < Integer > ();
      }
  }

}

class Main
{
  public static void main (String args[])
  {
    try
    {
      File file = new File ("test.txt");
      FileReader fr = new FileReader (file);
      BufferedReader br = new BufferedReader (fr);
      String s;
        List < Integer > array = new ArrayList <> ();
      while ((s = br.readLine ()) != null)
	array.add (Integer.parseInt (s));
        fr.close ();
        try
      {
	custom_thread thread1 = new custom_thread (1, array);
	  thread1.join ();
	custom_thread thread2 =
	  new custom_thread (2, thread1.get_res_array ());
	  thread2.join ();
	  List < Integer > res_array1 = thread1.get_res_array ();
	for (int i:res_array1)
	    System.out.println (i + " is divisible by 7");
	  List < Integer > res_array2 = thread2.get_res_array ();
	for (int i = 0; i < res_array2.size (); ++i)
	  if (res_array2.get (i) != 0)
	      System.out.println (res_array1.get (i) + " is Armstrong number");
      }
      catch (Exception e)
      {
	throw e;
      }
    }
    catch (Exception e)
    {
      e.printStackTrace ();
    }
  }
}