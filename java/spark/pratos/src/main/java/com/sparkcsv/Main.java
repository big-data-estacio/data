package com.sparkcsv;

import java.util.Arrays;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;

import com.sparkcsv.common.SepalComputation;
import com.sparkcsv.common.cleanseRDD;
import com.sparkcsv.common.getKV;
import com.sparkcsv.common.sepalLength;
import com.sparkcsv.conf.SparkConnection;

import scala.Tuple2;

public class Main {

    public static void main(String[] args) {

        long startTime = System.currentTimeMillis();

        Logger.getLogger("org").setLevel(Level.ERROR);
        Logger.getLogger("akka").setLevel(Level.ERROR);
        JavaSparkContext spContext = SparkConnection.getContext();

		/*-------------------------------------------------------------------
		 * Loading and Storing Data
		 -------------------------------------------------------------------*/

        JavaRDD<String> pratosAllData = spContext.textFile("data/pratos.csv");
        System.out.println("Total Records in pratos : " + pratosAllData.count());
        for ( String s : pratosAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> pratosTsvData = pratosAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : pratosTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headerpratos = pratosAllData.first();
        JavaRDD<String> pratosData = pratosAllData.filter(s -> !s.equals(headerpratos));
        System.out.println("Spark Operations : remove header");
        for ( String s : pratosData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> pratosDataFilter = pratosData.filter(str -> str.contains("Coca"));
        System.out.println("Coca word counts : " + pratosDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : pratosDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordspratos = pratosDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Coca word counts : " + wordspratos.count());
        for ( String s : wordspratos.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // JavaRDD<String> floatizerpratos = pratosData.map(new cleanseRDD());
        // for(String s :  floatizerpratos.take(10)) {
        //     System.out.println(s);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // String shortestpratos = pratosData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        // System.out.println("The shortest string is : " + shortestpratos);

        // String totalpratos = pratosData.reduce(new sepalLength());
        // System.out.println("Average Sepal.Length is " + (Double.valueOf(totalpratos) / (pratosData.count() )));
        // System.out.println("-----------------------------------------------------------------------------------");


        // JavaPairRDD<String, Double[]> pratosKV
        //         = pratosData.mapToPair(new getKV());

        // System.out.println("KV RDD Demo - raw tuples :");
        // for (Tuple2<String, Double[]> kvList : pratosKV.take(5)) {
        //     System.out.println(kvList._1 + " - "
        //             + kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double[]> pratosCompareMinKV
        //         = pratosKV.reduceByKey(new SepalComputation.computeMinSepal());

        // System.out.println("KV RDD Demo - minimum sepal length");
        // for (Tuple2<String, Double[]> kvList : pratosCompareMinKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> pratosCompareMaxKV
        //         = pratosKV.reduceByKey(new SepalComputation.computeMaxSepal());

        // System.out.println("KV RDD Demo - maximum sepal length");
        // for (Tuple2<String, Double[]> kvList : pratosCompareMaxKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> pratosSumKV
        //         = pratosKV.reduceByKey(new SepalComputation.computeAvgSepal());

        // System.out.println("KV RDD Demo - Tuples after summarizing :");
        // for (Tuple2<String, Double[]> kvList : pratosSumKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double> pratosAvgKV
        //         = pratosSumKV.mapValues(x -> x[0] / x[1]);

        // System.out.println("KV RDD Demo - Tuples after averaging :");
        // for (Tuple2<String, Double> kvList : pratosAvgKV.take(5)) {
        //     System.out.println(kvList);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
