package JavaIO;

import java.lang.reflect.Method;

public class MyHelloExam {

    public static void main(String[] args) {
        Myhello hello = new Myhello();

        try {
            Method method =  hello.getClass().getDeclaredMethod("hello");

            if (method.isAnnotationPresent(Conunt100.class)){
               for (int i = 0; i < 100; i++){
                   hello.Hello();
               }
            } else {
                hello.Hello();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}