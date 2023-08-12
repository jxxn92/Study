import java.util.Scanner;

public class exception {
    public static void main(String[] args) {
        System.out.println("숫자를 하나 입력해주세요.");
        Scanner scanner = new Scanner(System.in);
        String intInput = scanner.nextLine();
        try{
            int intValue = Integer.parseInt(intInput);
            System.out.println(intValue);

        } catch(Exception e){
            System.out.println("숫자만 입력 가능합니다.");
        }
    }
}
