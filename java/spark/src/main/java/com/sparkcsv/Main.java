package com.sparkcsv;

import com.sparkcsv.common.SepalComputation;
import com.sparkcsv.common.cleanseRDD;
import com.sparkcsv.common.getKV;
import com.sparkcsv.common.sepalLength;
import com.sparkcsv.conf.SparkConnection;
import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import scala.Tuple2;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        long startTime = System.currentTimeMillis();


        Logger.getLogger("org").setLevel(Level.ERROR);
        Logger.getLogger("akka").setLevel(Level.ERROR);
        JavaSparkContext spContext = SparkConnection.getContext();

		/*-------------------------------------------------------------------
		 * Loading and Storing Data
		 -------------------------------------------------------------------*/

        // Create a RDD from a file
        JavaRDD<String> irisAllData = spContext.textFile("data/iris.csv");
        System.out.println("Total Records in Iris : " + irisAllData.count());
        for ( String s : irisAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> irisTsvData = irisAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : irisTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");


        // remove header example
        String header = irisAllData.first();
        JavaRDD<String> irisData = irisAllData.filter(s -> !s.equals(header));
        System.out.println("Spark Operations : remove header");
        for ( String s : irisData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");


        // Filter example
        JavaRDD<String> toyotaData = irisData.filter(str -> str.contains("versicolor"));
        System.out.println("Versicolor word counts : " + toyotaData.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : toyotaData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        // FlatMap
        JavaRDD<String> words = toyotaData.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Toyota word counts : " + words.count());
        for ( String s : words.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");


        // Functions for Map (external)
        JavaRDD<String> floatizer = irisData.map(new cleanseRDD());
        for(String s :  floatizer.take(10)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");


        // Functions for Map
        String shortest = irisData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        System.out.println("The shortest string is : " + shortest);



        // ------------------------------------------------------------
        // Find the average Sepal.Length for all flowers in the irisRDD
        // ------------------------------------------------------------
        String totalSepalLength = irisData.reduce(new sepalLength());
        System.out.println("Average Sepal.Length is " + (Double.valueOf(totalSepalLength) / (irisData.count() )));
        System.out.println("-----------------------------------------------------------------------------------");



        // ------------------------------------------------------------
        // Create a Key-value RDD where Species is the key and Sepal.Length is the value
        // ------------------------------------------------------------
        JavaPairRDD<String, Double[]> irisKV
                = irisData.mapToPair(new getKV());

        System.out.println("KV RDD Demo - raw tuples :");
        for (Tuple2<String, Double[]> kvList : irisKV.take(5)) {
            System.out.println(kvList._1 + " - "
                    + kvList._2[0] + " ,  " + kvList._2[1]);
        }



        // Find the minimum of Sepal.Length by each Species
        JavaPairRDD<String, Double[]> irisCompareMinKV
                = irisKV.reduceByKey(new SepalComputation.computeMinSepal());

        System.out.println("KV RDD Demo - minimum sepal length");
        for (Tuple2<String, Double[]> kvList : irisCompareMinKV.take(5)) {
            System.out.println(kvList._1 + " - " +
                    kvList._2[0] + " ,  " + kvList._2[1]);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Find the maximum of Sepal.Length by each Species
        JavaPairRDD<String, Double[]> irisCompareMaxKV
                = irisKV.reduceByKey(new SepalComputation.computeMaxSepal());

        System.out.println("KV RDD Demo - maximum sepal length");
        for (Tuple2<String, Double[]> kvList : irisCompareMaxKV.take(5)) {
            System.out.println(kvList._1 + " - " +
                    kvList._2[0] + " ,  " + kvList._2[1]);
        }
        System.out.println("-----------------------------------------------------------------------------------");



        JavaPairRDD<String, Double[]> irisSumKV
                = irisKV.reduceByKey(new SepalComputation.computeAvgSepal());

        System.out.println("KV RDD Demo - Tuples after summarizing :");
        for (Tuple2<String, Double[]> kvList : irisSumKV.take(5)) {
            System.out.println(kvList._1 + " - " +
                    kvList._2[0] + " ,  " + kvList._2[1]);
        }

        JavaPairRDD<String, Double> irisAvgKV
                = irisSumKV.mapValues(x -> x[0] / x[1]);

        System.out.println("KV RDD Demo - Tuples after averaging :");
        for (Tuple2<String, Double> kvList : irisAvgKV.take(5)) {
            System.out.println(kvList);
        }
        System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
