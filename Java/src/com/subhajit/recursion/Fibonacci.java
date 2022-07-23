package com.subhajit.recursion;

import java.util.*;

public class Fibonacci {
    public static int fibonacci (int num){
        if (num <= 1)
            return num;
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a positive number: ");
        int no = sc.nextInt();
        if (no < 0)
            throw new Exception("Number can not be negative");

        for(int i = 0; i < no; i++) {
            System.out.print(fibonacci(i)+" ");
        }
    }
}
