package com.sparkcsv.common;

import org.apache.spark.api.java.function.Function;

import java.util.Arrays;


public class cleanseRDD implements Function<String, String> {

    @Override
    public String call(String autoStr) throws Exception {
        String[] attList = autoStr.split(",");
        Integer[] arrList = new Integer[4];


        arrList[0] = (int) Math.ceil(Double.valueOf(attList[0]));
        arrList[1] = (int) Math.floor(Double.valueOf(attList[1]));
        arrList[2] = (int) Math.ceil(Double.valueOf(attList[2]));
        arrList[3] = (int) Math.floor(Double.valueOf(attList[3]));

        return Arrays.toString(arrList);
    }

}
