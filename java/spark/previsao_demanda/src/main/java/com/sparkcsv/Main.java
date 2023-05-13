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

        JavaRDD<String> previsao_demandaAllData = spContext.textFile("data/previsao_demanda.csv");
        System.out.println("Total Records in previsao_demanda : " + previsao_demandaAllData.count());
        for ( String s : previsao_demandaAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> previsao_demandaTsvData = previsao_demandaAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : previsao_demandaTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headerprevisao_demanda = previsao_demandaAllData.first();
        JavaRDD<String> previsao_demandaData = previsao_demandaAllData.filter(s -> !s.equals(headerprevisao_demanda));
        System.out.println("Spark Operations : remove header");
        for ( String s : previsao_demandaData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> previsao_demandaDataFilter = previsao_demandaData.filter(str -> str.contains("Coca"));
        System.out.println("Coca word counts : " + previsao_demandaDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : previsao_demandaDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordsprevisao_demanda = previsao_demandaDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Coca word counts : " + wordsprevisao_demanda.count());
        for ( String s : wordsprevisao_demanda.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // JavaRDD<String> floatizerprevisao_demanda = previsao_demandaData.map(new cleanseRDD());
        // for(String s :  floatizerprevisao_demanda.take(10)) {
        //     System.out.println(s);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // String shortestprevisao_demanda = previsao_demandaData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        // System.out.println("The shortest string is : " + shortestprevisao_demanda);

        // String totalprevisao_demanda = previsao_demandaData.reduce(new sepalLength());
        // System.out.println("Average Sepal.Length is " + (Double.valueOf(totalprevisao_demanda) / (previsao_demandaData.count() )));
        // System.out.println("-----------------------------------------------------------------------------------");


        // JavaPairRDD<String, Double[]> previsao_demandaKV
        //         = previsao_demandaData.mapToPair(new getKV());

        // System.out.println("KV RDD Demo - raw tuples :");
        // for (Tuple2<String, Double[]> kvList : previsao_demandaKV.take(5)) {
        //     System.out.println(kvList._1 + " - "
        //             + kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double[]> previsao_demandaCompareMinKV
        //         = previsao_demandaKV.reduceByKey(new SepalComputation.computeMinSepal());

        // System.out.println("KV RDD Demo - minimum sepal length");
        // for (Tuple2<String, Double[]> kvList : previsao_demandaCompareMinKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> previsao_demandaCompareMaxKV
        //         = previsao_demandaKV.reduceByKey(new SepalComputation.computeMaxSepal());

        // System.out.println("KV RDD Demo - maximum sepal length");
        // for (Tuple2<String, Double[]> kvList : previsao_demandaCompareMaxKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> previsao_demandaSumKV
        //         = previsao_demandaKV.reduceByKey(new SepalComputation.computeAvgSepal());

        // System.out.println("KV RDD Demo - Tuples after summarizing :");
        // for (Tuple2<String, Double[]> kvList : previsao_demandaSumKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double> previsao_demandaAvgKV
        //         = previsao_demandaSumKV.mapValues(x -> x[0] / x[1]);

        // System.out.println("KV RDD Demo - Tuples after averaging :");
        // for (Tuple2<String, Double> kvList : previsao_demandaAvgKV.take(5)) {
        //     System.out.println(kvList);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
