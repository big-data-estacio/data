package com.sparkcsv.common;

import org.apache.spark.api.java.function.Function2;

public class sepalLength implements Function2<String, String, String> {

        @Override
        public String call(String arg0, String arg1) throws Exception {

            double firstVal = 0;
            double secondVal = 0;

            // First parameter - might be a numeric or string. handle appropriately
            firstVal = (isNumeric(arg0) ?
                    Double.valueOf(arg0) : getSepalLengthValue(arg0));
            // Second parameter.
            secondVal = (isNumeric(arg1) ?
                    Double.valueOf(arg1) : getSepalLengthValue(arg1));

            return Double.valueOf(firstVal + secondVal).toString();
        }

        // Internal function to extract Sepal Length
        private double getSepalLengthValue(String str) {
            // System.out.println(str);
            String[] attList = str.split(",");
            if (isNumeric(attList[0])) {
                return Double.valueOf(attList[0]);
            } else {
                return Double.valueOf(0);
            }
        }

        // Internal function to check if value is numeric
        private boolean isNumeric(String s) {
            return s.matches("[-+]?\\d*\\.?\\d+");
        }

}
