package Practice;

public class pra8 {
    public static void main(String[] args) {

    int number = 12321;
    int tmp = number;

    int result = 0;

    while (tmp != 0){

        result *= 10;
        result += tmp%10;
        tmp/=10;
        System.out.print(result + "   ");
        System.out.print(tmp + "   ");
        System.out.println(result + "   ");
    }
    if (number == result)
        System.out.println(number+ "는 회문수 입니다.");
    else
        System.out.println(number + "는 회문수가 아닙니다.");
    }
}
