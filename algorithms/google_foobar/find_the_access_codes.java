package com.google.challenges;

public class Answer {
    public static int answer(int[] l) {

        int noOfCombinations = 0;
        int[] noOfDoubles = new int[l.length];

        for( int i = 1; i < l.length-1; ++i){
            for( int j = 0; j < i; ++j){
                if( l[i] % l[j] == 0)
                    ++noOfDoubles[i];
            }
        }

        for( int i = 2; i < l.length; i++){
            for( int j = 1; j < i; ++j){
                if( l[i] % l[j] == 0)
                    noOfCombinations += noOfDoubles[j];
            }
        }
        return noOfCombinations;
    }
}