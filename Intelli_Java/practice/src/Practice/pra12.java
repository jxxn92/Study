package Practice;

public class pra12 {
    public static void main(String[] args) {

        char[] abcCode = {
                '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '[',
                ']', '{', '}', ';', ':', ',', '.', '/' };
        char[] numCode = { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p' };

        String src = "jxxn92";
        String result = "";

        for( int i = 0; i <src.length(); i++){
            char ch = src.charAt(i);

            if (ch >= 'a' && ch <= 'z'){
                result += abcCode[ch-'a'];
            } else if (ch >= '1' && ch <= '9') {
                result += numCode[ch-'0'];
            }
        }
        System.out.println("Src : " + src);
        System.out.println("Result : " + result);
    }
}