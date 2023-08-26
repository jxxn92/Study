package com.calculator;

public class NewClass2 {
    static class Cal {
        int val = 0;
        public void plus(){
            val++;
        }
    }

    public static void main(String[] args) {
        NewClass2.Cal c = new NewClass2.Cal();
        c.plus();
        System.out.println(c.val);
    }
}
