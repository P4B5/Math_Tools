//this code calculate the 90 first numbers of the fibonacci secuence 

import edu.princeton.cs.algs4.*;

public class FibonacciMemo {

  public static long  fibonacci() {

    long [] fibo = new long [90];

    fibo[0]=0;
    fibo[1]=1;

    StdOut.println(0 + " " + fibo[0]);
    StdOut.println(1 + " " + fibo[1]);

    for (int n = 2; n<fibo.length; n++){

      fibo[n] = fibo[n-2] + fibo[n-1];

      StdOut.println(n + " " + fibo[n]);

    }
    return fibo[fibo.length-1];
  }

  public static void main(String[] args){
    StdOut.println(fibonacci());

  }
}
