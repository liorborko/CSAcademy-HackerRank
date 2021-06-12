import java.util.Scanner;

public class Main {

//    static int factorial(int n){
//        if (n > 5 && n < 1000)
//            return n * factorial(n - 1);
//        return 0;
//    }

    static long factorial(long n) {return n <= 1 ? 1 : n*factorial(n-1);}

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int cut_ways = obj.nextInt();

        for (int i=1; i<= 100; i+=2){
            if(cut_ways ==1)
                System.out.println(3);
            else if (cut_ways == 2)
                System.out.println(4);
            else if (cut_ways == 5)
                System.out.println(5);
            else {
                long n= factorial(cut_ways-2);
                if ((factorial(2*(cut_ways-2))/ (n* cut_ways-1) * n) ==cut_ways)
                    System.out.println(cut_ways);
                    break;
            }
            try{
                cut_ways=obj.nextInt();

            }catch(Exception e){
                break;
            }

        }
    }

}
