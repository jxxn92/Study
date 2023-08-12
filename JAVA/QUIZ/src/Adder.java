import java.util.Scanner;

public class Adder {
    public static void main(String[] args) throws Exception {
        System.out.println("두 개의 숫자를 입력해 주세요 (띄어쓰기로 구분)");
        
        Scanner scanner = new Scanner(System.in);

        String input1 = scanner.next();
        String input2 = scanner.next();

        int intValue1 = Integer.parseInt(input1);
        int intValue2 = Integer.parseInt(input2);

        System.out.println(intValue1 + intValue2);
    }
}
