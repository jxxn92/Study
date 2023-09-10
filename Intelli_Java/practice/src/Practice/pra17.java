package Practice;

public class pra17 {
    public static int max(int[] arr){
        int max_num = 0;
        if (arr == null || arr.length == 0){
            return -999999;
        } else {
            max_num = arr[0];
            for (int i = 1; i < arr.length; i++){
                if(max_num <= arr[i]){
                    max_num = arr[i];
                }
            }
        }
        return max_num;
    }


    public static void main(String[] args) {
        int [] data = {3, 2, 9, 4, 7};
        System.out.println(java.util.Arrays.toString(data));
        System.out.println("최댓값 : " + max(data));
        System.out.println("최댓값 : " + max(null));
        System.out.println("최댓값 : " + max(new int []{}));
    }
}
