import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class output {
    public static void main(String[] args) {
        FileWriter writer = null;
        try{
            writer = new FileWriter("D:/Git/self_study/JAVA/file_java/output01.txt", true);
        } catch (IOException e) {
            System.out.println("파일 생성에 실패했습니다.");
            System.exit(1);            
        }

        System.out.println("종료하려면 입력 없이 엔터.");

        Scanner scanner = new Scanner(System.in);
        while(true){
            String input = scanner.nextLine();

            if(input.equals("")){
                System.out.println("파일 입력을 종료합니다.");
                break;
            }
            try {
                writer.write(input + "\n");
            } catch (IOException e) {
                System.out.println("파일에 데이터를 쓰는데 실패했습니다.");
                System.exit(2);
            }
        }
        try {
            writer.close();
        } catch (IOException e) {
            System.out.println("파일 닫기에 실패했습니다.");
        }
    }
}
