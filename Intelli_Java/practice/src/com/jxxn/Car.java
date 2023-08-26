package com.jxxn;

import javax.sound.midi.Soundbank;
import javax.sql.rowset.serial.SQLOutputImpl;

public class Car {

    String name;
    int speed;
    int price;

    public Car(){
        this.name = "None";
        this.speed = 0;
        this.price = 0;
    }
    public Car(String name){
        this.name = name;
    }
    public Car(String name, int speed){
//        this.name = name;
//        this.speed = speed;
        this("None", 0, 0);
    }

    public Car(String name, int speed, int price){
        this.name = name;
        this.speed = speed;
        this.price = price;
    }

    public void run(){
        System.out.println("달리다.");
    }
}
