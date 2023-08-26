package com.inter;

public class LedTV {
    public static void main(String[] args) {
        LedExam l1 = new LedExam();

        l1.turnOn();
        l1.ChangeChannel(30);
        l1.ChangeVolume(20);
        l1.turnOff();
    }
}
