import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;


public class input {
    public static void main(String[] args) {
        FileInputStream inputStream =  null;
        
        try{
            inputStream = new FileInputStream("D:/Git/self_study/JAVA/file_java/acronym.txt");
        } catch ( FileNotFoundException e){
            e.printStackTrace();
        }

        Scanner scanner = new Scanner(inputStream);
        
        while(scanner.hasNextLine()){
            String line = scanner.nextLine();
            System.out.println(line);
        }

    }    
}