import java.util.ArrayList;

class GfG {
    static ArrayList<Integer> findUnion(int[] a, int[] b) {
        ArrayList<Integer> res = new ArrayList<>();

        
       
        for (int num : a) {

           
            if (!res.contains(num)) {
                res.add(num);
            }
        }

       
        for (int num : b) {

           
            if (!res.contains(num)) {
                res.add(num);
            }
        }
        return res;
    }

    public static void main(String[] args) {
      
        int[] a = { 1, 2, 3, 2, 1 };
        int[] b = { 3, 2, 2, 3, 3, 2 };

        ArrayList<Integer> res = findUnion(a, b);

        for (int num : res) {
            System.out.print(num + " ");
        }
    }
}
