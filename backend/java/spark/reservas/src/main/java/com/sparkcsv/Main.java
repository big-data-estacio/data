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

import java.lang.reflect.Field;
import sun.misc.Unsafe;


public class Main {

    public static void main(String[] args) {

      try {
        // Configurar a opção de illegal-access antes de iniciar o Spark
        Field theUnsafe = Unsafe.class.getDeclaredField("theUnsafe");
        theUnsafe.setAccessible(true);
        Unsafe u = (Unsafe) theUnsafe.get(null);

        Class<?> cls = Class.forName("jdk.internal.module.IllegalAccessLogger");
        Field logger = cls.getDeclaredField("logger");
        u.putObjectVolatile(cls, u.staticFieldOffset(logger), null);
        } catch (Exception e) {
            // Lidar com a exceção, se necessário
        }

        long startTime = System.currentTimeMillis();

        Logger.getLogger("org").setLevel(Level.ERROR);
        Logger.getLogger("akka").setLevel(Level.ERROR);
        JavaSparkContext spContext = SparkConnection.getContext();

		/*-------------------------------------------------------------------
		 * Loading and Storing Data
		 -------------------------------------------------------------------*/

        JavaRDD<String> reservasAllData = spContext.textFile("data/reservas.csv");
        System.out.println("Total Records in reservas : " + reservasAllData.count());
        for ( String s : reservasAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> reservasTsvData = reservasAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : reservasTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headerreservas = reservasAllData.first();
        JavaRDD<String> reservasData = reservasAllData.filter(s -> !s.equals(headerreservas));
        System.out.println("Spark Operations : remove header");
        for ( String s : reservasData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> reservasDataFilter = reservasData.filter(str -> str.contains("Coca"));
        System.out.println("Coca word counts : " + reservasDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : reservasDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordsreservas = reservasDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Coca word counts : " + wordsreservas.count());
        for ( String s : wordsreservas.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // JavaRDD<String> floatizerreservas = reservasData.map(new cleanseRDD());
        // for(String s :  floatizerreservas.take(10)) {
        //     System.out.println(s);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // String shortestreservas = reservasData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        // System.out.println("The shortest string is : " + shortestreservas);

        // String totalreservas = reservasData.reduce(new sepalLength());
        // System.out.println("Average Sepal.Length is " + (Double.valueOf(totalreservas) / (reservasData.count() )));
        // System.out.println("-----------------------------------------------------------------------------------");


        // JavaPairRDD<String, Double[]> reservasKV
        //         = reservasData.mapToPair(new getKV());

        // System.out.println("KV RDD Demo - raw tuples :");
        // for (Tuple2<String, Double[]> kvList : reservasKV.take(5)) {
        //     System.out.println(kvList._1 + " - "
        //             + kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double[]> reservasCompareMinKV
        //         = reservasKV.reduceByKey(new SepalComputation.computeMinSepal());

        // System.out.println("KV RDD Demo - minimum sepal length");
        // for (Tuple2<String, Double[]> kvList : reservasCompareMinKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> reservasCompareMaxKV
        //         = reservasKV.reduceByKey(new SepalComputation.computeMaxSepal());

        // System.out.println("KV RDD Demo - maximum sepal length");
        // for (Tuple2<String, Double[]> kvList : reservasCompareMaxKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> reservasSumKV
        //         = reservasKV.reduceByKey(new SepalComputation.computeAvgSepal());

        // System.out.println("KV RDD Demo - Tuples after summarizing :");
        // for (Tuple2<String, Double[]> kvList : reservasSumKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double> reservasAvgKV
        //         = reservasSumKV.mapValues(x -> x[0] / x[1]);

        // System.out.println("KV RDD Demo - Tuples after averaging :");
        // for (Tuple2<String, Double> kvList : reservasAvgKV.take(5)) {
        //     System.out.println(kvList);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
