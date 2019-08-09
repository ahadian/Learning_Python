import java.util.concurrent.TimeUnit;
import java.math.BigInteger; 

public class loop
{
  static long test(long x)
  {
	long i = 0;
	long a = 0;
	long startTime = System.nanoTime();

	for(i = 0; i < x; i++){
	   a++;
	}

	long endTime = System.nanoTime();
	double timeElapsed = (double) (endTime - startTime) / 1_000_000_000;
	System.out.println("Time for "+x+"  : " + timeElapsed);
	//System.out.println("Execution time in milliseconds : " + timeElapsed / 1000000);
    	return a;
  }


  public static void main(String args[])
  {
	System.out.println(test(990000000));
  }
}
