package Practice;

import java.util.Scanner;

public class pro_1  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("-- 길이 변환 프로그램 --");
        System.out.println("변환 하고 싶은 길이를 입력하시오.(단위 :meter)");
        double length = sc.nextDouble();
        System.out.println("현재 길이(m) : " + (int)length+("m"));
        System.out.printf("변환 후 길이 = %f (km)",(length/1000));
    }
}
