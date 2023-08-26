package com.calculator;

public interface Calcul {
    public void plus(int x, int y);

    public void multi(int x, int y);

    public void minus(int x, int y);

    public void divide(int x, int y);

    default int exec(int x, int y){
        System.out.println("이게 맞나?");
        return x + y;
    }
}
