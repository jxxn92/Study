package com.method;

public class MyClass {

    public void method1(){
        System.out.println("단순히 이용해서 만든 method1 모델입니다.");
    }

    public void method2(int x){
        System.out.println(x + "단순히 이용해서 만든 method2 모델입니다.");
    }

    public int method3(){
        System.out.println("단순히 이용해서 만든 method3 모델입니다.");
        return 5;
    }

    public void method4(int x, int y){
        System.out.println(x+y+"단순히 이용해서 만든 method4 모델입니다.");
    }

    public int method5(int x){
        System.out.println(x+"단순히 이용해서 만든 method5 모델입니다.");
        return x*2;
    }
}
