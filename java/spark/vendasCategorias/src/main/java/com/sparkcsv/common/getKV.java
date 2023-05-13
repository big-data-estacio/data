package com.sparkcsv.common;

import org.apache.spark.api.java.function.PairFunction;
import scala.Tuple2;

public class getKV implements PairFunction<String, String, Double[]> {
    @Override
    public Tuple2<String, Double[]> call(String s) throws Exception {
        String[] attList = s.split(",");

        // Handle header line
        Double[] hpVal = { (attList[2].equals("PetalLength") ?
                0 : Double.valueOf(attList[2])), 1d};
        return new Tuple2<String, Double[]>(attList[4], hpVal);

    }

}
