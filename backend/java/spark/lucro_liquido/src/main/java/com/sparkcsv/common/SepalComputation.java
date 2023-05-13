package com.sparkcsv.common;

import org.apache.spark.api.java.function.Function2;

public class SepalComputation {

    // Class to compute Minimum Sepal Length by flower sort
    public static class computeMinSepal implements
            Function2<Double[], Double[], Double[]> {

        @Override
        public Double[] call(Double[] v1, Double[] v2) throws Exception {

            Double[] result = { (v1[0] < v2[0] ? v1[0] : v2[0]), v1[1] + v2[1] };
            return result;

        }
    }

    // Class to compute Maximum Sepal Length by flower sort
    public static class computeMaxSepal implements
            Function2<Double[], Double[], Double[]> {

        @Override
        public Double[] call(Double[] v1, Double[] v2) throws Exception {

            Double[] result = { (v1[0] > v2[0] ? v1[0] : v2[0]), v1[1] + v2[1] };
            return result;

        }
    }

    public static class computeAvgSepal implements
            Function2<Double[], Double[], Double[]> {

        @Override
        public Double[] call(Double[] v1, Double[] v2) throws Exception {

            Double[] result = {v1[0] + v2[0], v1[1] + v2[1]};

            return result;
        }
    }
}
