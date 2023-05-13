package com.sparkcsv.conf;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;

public class SparkConnection {

    private static String appName = "Spark CSV sampler Application";

    // use this for local spark
    private static String sparkMaster = "local[2]";
    // use this for remote Master spark
//    private static String sparkMaster = "spark://10.100.25.237:7077";

    private static JavaSparkContext spContext = null;
    private static SparkSession sparkSession = null;
    // Change this to your temp directory{
    private static String tempDir = "file:///home/seroj/Documents/ML/course/temp_dir";

    private static void getConnection() {
        if (spContext == null) {
            SparkConf sparkConf = new SparkConf().setAppName(appName).setMaster(sparkMaster);
            spContext = new JavaSparkContext(sparkConf);
            sparkSession = SparkSession
                    .builder()
                    .appName(appName)
                    .master(sparkMaster)
                    .config("spark.sql.warehouse.dir", tempDir)
                    .getOrCreate();
        }
    }

    public static JavaSparkContext getContext() {
        if(spContext == null) {
            getConnection();
        }
        return spContext;
    }

    public static SparkSession getSession() {
        if(sparkSession == null) {
            getConnection();
        }
        return sparkSession;
    }

}
