import java.util.Scanner;

public class basic_input {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.println("달러 환율을 입력하세요.");
        String exchangeString = scanner.nextLine();

        System.out.println("순대국 값을 입력하세요.");
        String priceOfSoupString = scanner.nextLine();

        Double exchange = Double.parseDouble(exchangeString);
        Double PriceOfSoup = Double.parseDouble(priceOfSoupString);

        String result = String.format("%.2f",(PriceOfSoup / exchange));

        System.out.println("순대국은 " + result + "달러입니다.");
    }
}
