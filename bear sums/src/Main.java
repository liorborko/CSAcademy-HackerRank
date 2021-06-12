import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Set data structure does has NO ordering NOR duplicates
        Set<Integer> workingSet = new HashSet<>();
        Scanner myScanner = new Scanner(System.in);
//        System.out.print("Please enter number of tests: ");
        int numOfTests = myScanner.nextInt(); // number of tests
        for (int i = 0; i < numOfTests; i++) {
            // conduct each test
//            System.out.print("Please enter the sum for test " + (i + 1) + ": ");
            int sum = myScanner.nextInt(); // sum for test
//            System.out.print("Please enter the number of elements for test " + (i + 1) + ": ");
            Integer num1 = null;
            Integer num2 = null; // initialization is redundant. However, it is common practice
            int numOfElements = myScanner.nextInt(); // number of elements
            int intArray[] = new int[numOfElements];

//          input elements check
            for (int k=0; k< numOfElements; k++){
//                System.out.print("Please enter element number: " + (k + 1) + ": ");
                intArray[k] = myScanner.nextInt();
            }
            for (int e = 0; e < numOfElements; e++) {

                if (num1 == null) {
                    if (workingSet.contains(intArray[e])) { // O(1) for searching
                        num1 = intArray[e];
                        break;
                    } else {
                        workingSet.add(sum - intArray[e]);
                    }
                }
            }
            if (num1 == null) {// no pair was found
                System.out.println("!OK");
                workingSet.clear();
            }

            else {
                num2 = sum - num1;
                workingSet.clear();

                if (num2 > num1) {
                    System.out.println(num1 + " " + num2);

                }
                else {
                    System.out.println(num2 + " " + num1);
                }

            }
        }
    }
}