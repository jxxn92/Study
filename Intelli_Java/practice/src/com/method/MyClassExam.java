package com.method;

public class MyClassExam {
    public static void main(String[] args) {
        MyClass mc = new MyClass();
        mc.method1();
        mc.method2(1);
        int var = mc.method3();
        System.out.println(var);
        mc.method4(2,3);
        int value = mc.method5(3);
        System.out.println(value);
    }
}
