package com.inter;

public class LedExam implements TV {


    @Override
    public void turnOn() {
        System.out.println("TV를 실행했습니다.");
    }

    @Override
    public void turnOff() {
        System.out.println("TV를 종료했습니다.");
    }


    @Override
    public void ChangeVolume(int volume) {
        System.out.println("볼륨을 조정했습니다.");
    }

    @Override
    public void ChangeChannel(int channel) {
        System.out.println("채널을 조정했습니다. ");
    }

}
