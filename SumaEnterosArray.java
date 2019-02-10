
import java.util.Arrays;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;


public class SumaEnterosArray

{

  public static int [] suma(int [] sumandoA, int [] sumandoB){

    int [] fnum = new int [sumandoA.length]; //this is the final array, its length must be the same as the biggest number
    int [] rem = new int [sumandoA.length]; //accumuator array

    for (int i = 0; i < sumandoB.length; i++){

      int sum1 = sumandoA[sumandoA.length - (i+1)];
      int sum2 = sumandoB[sumandoB.length - (i+1)];

      int result = sum1 + sum2;

      if (result < 9){

        fnum[fnum.length - (i+1)] = result + rem[rem.length - 1];
        rem[rem.length-1] = 0; //insert a 0 in the accumuator array to avoid add the accumuator to others values

      } else {

          int quotient = result / 10;
          int remainder = result % 10;

          fnum[fnum.length - (i+1)] = quotient;
          rem[rem.length - 1] = remainder;

      }

    }
    return  fnum;
  }

  public static void main(String[] args)
  {

    int [] a = {1, 2, 3};  //This is the first number, must be the biggest

    int [] b = new int [a.length]; //the 2nd number is going to be like [0, 1, 0]

    int last_pos = 2;

    b [b.length - 1] = 0;
    b [b.length - last_pos] = 1;

    //this loop is for insert 0 at the beginning of the array in order to have the same length in both arrays
    for (int q = 0; q < (b.length - last_pos); q++){
      b[q] = 0;
    }

     StdOut.println(Arrays.toString((suma(a, b))));
  }
}
