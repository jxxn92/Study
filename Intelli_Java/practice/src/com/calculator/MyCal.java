package com.calculator;

public class MyCal implements Calcul{

    @Override
    public void plus(int x, int y) {
        System.out.println("계산결과는 "+(x+y)+"입니다.");
    }

    @Override
    public void multi(int x, int y) {
        System.out.println("계산결과는 "+(x*y)+"입니다.");
    }

    @Override
    public void minus(int x, int y) {
        System.out.println("계산결과는 "+(x-y)+"입니다.");
    }

    @Override
    public void divide(int x, int y) {
        System.out.println("계산결과는 "+(x/y)+"입니다.");
    }
}
