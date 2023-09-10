package Practice;

public class pra3 {
    public static void main(String[] args) {
        char ch = 'B';

        char lowerCase = ((ch >= 'A' && ch <= 'Z')) ? ((char)((int)ch+32)) : ch;

        System.out.println("ch = " + ch);
        System.out.println("lowerCase = " + lowerCase);
    }
}
