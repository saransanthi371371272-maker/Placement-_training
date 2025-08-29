
public class SubArray {
  
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

       
        int a = 1;       // Start index (inclusive)
        int b = 4;       // End index (exclusive)

        
        int[] sub = new int[b - a];
        for (int i = a; i < b; i++) {
            sub[i - a] = arr[i];
        }

        System.out.print("");
        for (int n : sub) {
            System.out.print(n + " ");
        }
    }
}
