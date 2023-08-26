package com.calculator;

public class NewClass {
    class Cal {
        int val = 0;
        public void plus(){
            val++;
        }
    }

    public static void main(String[] args) {
        NewClass n = new NewClass();

        NewClass.Cal c = n.new Cal();

        c.plus();
        System.out.println(c.val);

    }
}