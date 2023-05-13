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

        JavaRDD<String> vendasAllData = spContext.textFile("data/vendas.csv");
        System.out.println("Total Records in vendas : " + vendasAllData.count());
        for ( String s : vendasAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> vendasTsvData = vendasAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : vendasTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headervendas = vendasAllData.first();
        JavaRDD<String> vendasData = vendasAllData.filter(s -> !s.equals(headervendas));
        System.out.println("Spark Operations : remove header");
        for ( String s : vendasData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> vendasDataFilter = vendasData.filter(str -> str.contains("Coca"));
        System.out.println("Coca word counts : " + vendasDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : vendasDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordsvendas = vendasDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Coca word counts : " + wordsvendas.count());
        for ( String s : wordsvendas.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // JavaRDD<String> floatizervendas = vendasData.map(new cleanseRDD());
        // for(String s :  floatizervendas.take(10)) {
        //     System.out.println(s);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // String shortestvendas = vendasData.reduce((Function2<String, String, String>) (v1, v2) -> (v1.length() < v2.length() ? v1 : v2));
        // System.out.println("The shortest string is : " + shortestvendas);

        // String totalvendas = vendasData.reduce(new sepalLength());
        // System.out.println("Average Sepal.Length is " + (Double.valueOf(totalvendas) / (vendasData.count() )));
        // System.out.println("-----------------------------------------------------------------------------------");


        // JavaPairRDD<String, Double[]> vendasKV
        //         = vendasData.mapToPair(new getKV());

        // System.out.println("KV RDD Demo - raw tuples :");
        // for (Tuple2<String, Double[]> kvList : vendasKV.take(5)) {
        //     System.out.println(kvList._1 + " - "
        //             + kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double[]> vendasCompareMinKV
        //         = vendasKV.reduceByKey(new SepalComputation.computeMinSepal());

        // System.out.println("KV RDD Demo - minimum sepal length");
        // for (Tuple2<String, Double[]> kvList : vendasCompareMinKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> vendasCompareMaxKV
        //         = vendasKV.reduceByKey(new SepalComputation.computeMaxSepal());

        // System.out.println("KV RDD Demo - maximum sepal length");
        // for (Tuple2<String, Double[]> kvList : vendasCompareMaxKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");

        // JavaPairRDD<String, Double[]> vendasSumKV
        //         = vendasKV.reduceByKey(new SepalComputation.computeAvgSepal());

        // System.out.println("KV RDD Demo - Tuples after summarizing :");
        // for (Tuple2<String, Double[]> kvList : vendasSumKV.take(5)) {
        //     System.out.println(kvList._1 + " - " +
        //             kvList._2[0] + " ,  " + kvList._2[1]);
        // }

        // JavaPairRDD<String, Double> vendasAvgKV
        //         = vendasSumKV.mapValues(x -> x[0] / x[1]);

        // System.out.println("KV RDD Demo - Tuples after averaging :");
        // for (Tuple2<String, Double> kvList : vendasAvgKV.take(5)) {
        //     System.out.println(kvList);
        // }
        // System.out.println("-----------------------------------------------------------------------------------");


        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
