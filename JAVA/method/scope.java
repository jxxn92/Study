import java.util.Random;
import java.util.Scanner;

public class scope{
    public static int randomNumber;
    public static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        Random random = new Random();
        randomNumber = random.nextInt(256);
        
        int attempt = 0;

        while(attempt < 8){
            boolean isCorrect = play();

            if(isCorrect){
                break;
            }
            attempt++;
            System.out.println(attempt + "회 시도하였습니다.");
        }
        System.out.println("게임을 종료합니다.");
    }
    public static boolean play(){
        System.out.println("숫자를 입력하세요.");
        int input = scanner.nextInt();
        
        if(input == randomNumber){
            System.out.println("짝짝짝, 정답입니다.");
            return true;
        }
        else if(input > randomNumber){
            System.out.println("제가 생각한 숫자는 더 작습니다.");
        }
        else{
            System.out.println("제가 생각한 숫자는 더 큽니다.");
        }
        return false;
    }
}