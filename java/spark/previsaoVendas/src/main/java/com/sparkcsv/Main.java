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

        JavaRDD<String> previsaoVendasAllData = spContext.textFile("data/previsaoVendas.csv");
        System.out.println("Total Records in previsaoVendas : " + previsaoVendasAllData.count());
        for ( String s : previsaoVendasAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> previsaoVendasTsvData = previsaoVendasAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : previsaoVendasTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headerprevisaoVendas = previsaoVendasAllData.first();
        JavaRDD<String> previsaoVendasData = previsaoVendasAllData.filter(s -> !s.equals(headerprevisaoVendas));
        System.out.println("Spark Operations : remove header");
        for ( String s : previsaoVendasData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> previsaoVendasDataFilter = previsaoVendasData.filter(str -> str.contains("Coca"));
        System.out.println("Coca word counts : " + previsaoVendasDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : previsaoVendasDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordsprevisaoVendas = previsaoVendasDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Coca word counts : " + wordsprevisaoVendas.count());
        for ( String s : wordsprevisaoVendas.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // JavaRDD<String> floatizerprevisaoVendas = previsaoVendasData.map(new cleanseRDD());
        // for(String s :  floatizerprevisaoVendas.take(10)) {
        //     System.out.println(s);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // String shortestprevisaoVendas = previsaoVendasData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        // System.out.println("The shortest string is : " + shortestprevisaoVendas);

        // String totalprevisaoVendas = previsaoVendasData.reduce(new sepalLength());
        // System.out.println("Average Sepal.Length is " + (Double.valueOf(totalprevisaoVendas) / (previsaoVendasData.count() )));
        // System.out.println("-----------------------------------------------------------------------------------");


        // JavaPairRDD<String, Double[]> previsaoVendasKV
        //         = previsaoVendasData.mapToPair(new getKV());

        // System.out.println("KV RDD Demo - raw tuples :");
        // for (Tuple2<String, Double[]> kvList : previsaoVendasKV.take(5)) {
        //     System.out.println(kvList._1 + " - "
        //             + kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double[]> previsaoVendasCompareMinKV
        //         = previsaoVendasKV.reduceByKey(new SepalComputation.computeMinSepal());

        // System.out.println("KV RDD Demo - minimum sepal length");
        // for (Tuple2<String, Double[]> kvList : previsaoVendasCompareMinKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> previsaoVendasCompareMaxKV
        //         = previsaoVendasKV.reduceByKey(new SepalComputation.computeMaxSepal());

        // System.out.println("KV RDD Demo - maximum sepal length");
        // for (Tuple2<String, Double[]> kvList : previsaoVendasCompareMaxKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> previsaoVendasSumKV
        //         = previsaoVendasKV.reduceByKey(new SepalComputation.computeAvgSepal());

        // System.out.println("KV RDD Demo - Tuples after summarizing :");
        // for (Tuple2<String, Double[]> kvList : previsaoVendasSumKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double> previsaoVendasAvgKV
        //         = previsaoVendasSumKV.mapValues(x -> x[0] / x[1]);

        // System.out.println("KV RDD Demo - Tuples after averaging :");
        // for (Tuple2<String, Double> kvList : previsaoVendasAvgKV.take(5)) {
        //     System.out.println(kvList);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
