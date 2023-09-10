package Practice;

public class pra16 {
    public static boolean isNumber(String str){
        boolean ret = true;

        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) >= '0' && str.charAt(i) <= '9'){
                continue;
            } else {
                ret = false;
                break;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        String str = "123";
        System.out.println(str + "는 숫자입니까? " + isNumber(str));

        str = "1234o";
        System.out.println(str + "는 숫자입니까? " + isNumber(str));
    }
}
