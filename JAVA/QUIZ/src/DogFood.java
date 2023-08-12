import java.util.Scanner;

public class DogFood{
    public static void main(String[] args) {
        System.out.println("강아지의 몸무게를 입력하세요. (단위 : 킬로그램)");
        Scanner scanner = new Scanner(System.in);

        String weightOfDogString = scanner.nextLine();
        Double weightOfDog = Double.parseDouble(weightOfDogString);

        Double gramWeightOfDog = weightOfDog * 1000;

        System.out.println("하루 권장 사료 공급량 : " + gramWeightOfDog / 100. + "(그램)");
    }

}