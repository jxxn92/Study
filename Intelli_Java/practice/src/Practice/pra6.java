package Practice;

import java.util.Scanner;

public class pra6 {
    public static void main(String[] args) {

        int answer = (int)(Math.random() * 100 + 1 );
        int input = 0;
        int count = 0;
        boolean correct = false;

        System.out.println(answer);
        Scanner in = new Scanner(System.in);

        do{
            count++;
            System.out.println("1 과 100 사이에 값을 입력하세요.");
            input = in.nextInt();

            if ( input < answer) {
                System.out.println("더 큰 수를 입력하세요.");
                correct = false;
            } else if (input > answer){
                System.out.println("더 작은 값을 입력하세요");
                correct = false;
            } else {
                System.out.println("정답입니다. 축하합니다!");
                correct = true;
            }
        } while (!correct);

        System.out.println(answer);
    }
}
