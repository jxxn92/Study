package Practice;

public class pra4_for {
    public static void main(String[] args) {

        for (int i = 0; i <= 10; i++){
            for (int j = 0; j <= 10; j++){
                if (2*i + 4*j == 10) {
                    System.out.printf("%d %d", i, j);
                    System.out.println();
                } else {
                    continue;
                }
            }
        }
    }
}
