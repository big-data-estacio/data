package com.sparkcsv;

import java.lang.reflect.Field;
import java.util.Arrays;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;

import com.sparkcsv.conf.SparkConnection;

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

        JavaRDD<String> vendasCategoriasAllData = spContext.textFile("data/vendasCategorias.csv");
        System.out.println("Total Records in vendasCategorias : " + vendasCategoriasAllData.count());
        for ( String s : vendasCategoriasAllData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> vendasCategoriasTsvData = vendasCategoriasAllData
                .map(str -> str.replace(",", "\t"));
        System.out.println("Spark Operations : MAP");
        for ( String s : vendasCategoriasTsvData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        String headervendasCategorias = vendasCategoriasAllData.first();
        JavaRDD<String> vendasCategoriasData = vendasCategoriasAllData.filter(s -> !s.equals(headervendasCategorias));
        System.out.println("Spark Operations : remove header");
        for ( String s : vendasCategoriasData.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> vendasCategoriasDataFilter = vendasCategoriasData.filter(str -> str.contains("Bebida"));
        System.out.println("Coca word counts : " + vendasCategoriasDataFilter.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : vendasCategoriasDataFilter.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        JavaRDD<String> vendasCategoriasDataFilterSobremesa = vendasCategoriasData.filter(str -> str.contains("Sobremesa"));
        System.out.println("Coca word counts : " + vendasCategoriasDataFilterSobremesa.count());
        System.out.println("Spark Operations : FILTER");
        for ( String s : vendasCategoriasDataFilterSobremesa.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        // Distinct example
//        System.out.println("Spark distinct example : " + xxxx.distinct().collect());

        JavaRDD<String> wordsvendasCategorias = vendasCategoriasDataFilter.flatMap((FlatMapFunction<String, String>) s -> Arrays.asList(s.split(",")).iterator());
        System.out.println("Bebida counts : " + wordsvendasCategorias.count());
        for ( String s : wordsvendasCategorias.take(11)) {
            System.out.println(s);
        }
        System.out.println("-----------------------------------------------------------------------------------");

        long endTime = System.currentTimeMillis();
        System.out.println("\n\n *-----------* Spark operations took : " + ((endTime-startTime)/1000) + " seconds");

    }

}
