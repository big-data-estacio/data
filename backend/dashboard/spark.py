import findspark

from pyspark.sql.functions import col, when,regexp_extract , translate ,regexp_replace ,substring,concat,max, last
from pyspark.sql.types import IntegerType,DecimalType,DateType,StringType, DoubleType
findspark.init()

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder \
  .appName('clean_products_magdiel') \
  .config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar') \
  .getOrCreate()

spark.conf.set("spark.sql.repl.eagerEval.enabled",True)

#name table products
table_products = "becade_mgutierrez.stg_products"

#load table to dataframe
stg_products = spark.read \
  .format("bigquery") \
  .option("table", table_products) \
  .load()

#show incoming lines
print("lines incoming: " , stg_products.count())

#show schema
stg_products.printSchema()


#select columns from table
raw_products = stg_products.select('product_id','country','app_sale_price','evaluate_rate','isbestseller','isprime','app_sale_price_currency')

#clean column app_sale_price drop values 'None'
raw_products = raw_products.where(raw_products.app_sale_price != 'None')

#show outgoing lines
print("lines clean outgoing: " , raw_products.count())

# fill empty rows evaluate_rate
df_raw_products= raw_products.withColumn("evaluate_rate", when(col("evaluate_rate")=="" ,None)  \
                               .otherwise(col("evaluate_rate"))) 
        
#clean column app_sale_price drop values 'None'
df_raw_products = df_raw_products.where(df_raw_products.evaluate_rate != "None")

#show outgoing lines
print("lines clean outgoing: " , df_raw_products.count())

#drop duplicates rows products
df_raw_products = df_raw_products.dropDuplicates()

#show outgoing lines
print("lines clean outgoing: " , df_raw_products.count())

#clean column evaluate_rate extract format {n.n} &&  replace characters {,} by {.}
df_clean_rate = df_raw_products \
                .withColumn('clean_rate', regexp_extract(col('evaluate_rate'), r'([0-9][\.\,][0-9])',1)) \
                .withColumn('clean_rate', translate(col('clean_rate'), ',', '.'))

#clean column app_sale_price delete characters && define format {n nnn.nn}
df_raw_price = df_clean_rate \
                .withColumn('app_raw_price', translate(col('app_sale_price'), ',￥', '.')) \
                .withColumn('decimal_price', regexp_extract(col('app_raw_price'), r'([\.][0-9]{2}+$)',1)) \
                .withColumn('raw_number_price', regexp_extract(col('app_raw_price'), r'([0-9][\.][0-9]{3}|[0-9]{2,3})',1)) \
                .withColumn('number_price', translate(col('raw_number_price'), '.', ''))
              
#Show row products             
df_raw_price.select('product_id','country','app_sale_price','app_raw_price','raw_number_price','number_price','decimal_price').show(5,truncate=False)

#concat columns  number_price + decimal_price = app_sale_price_us
df_clean_products_raw=df_raw_price.select('product_id','country','isbestseller','isprime','app_sale_price_currency','clean_rate',
                                          concat(df_raw_price.number_price,df_raw_price.decimal_price).alias("app_sale_price"))

#Show row products
df_clean_products_raw.show(5)

##########################################################
##extract table exhcange_rate from BigQuery Staging ######
############## PRODUCTS ALL COUNTRY CONTINUE #############

#name table exchange
table_exchange = "becade_mgutierrez.stg_tasas_cambio_pais_anual"

#load table
stg_exchange = spark.read \
  .format("bigquery") \
  .option("table", table_exchange) \
  .load()

#show schema
stg_exchange.printSchema()

#show incoming lines
print("lines incoming: " , stg_exchange.count())

#select columns from table
raw_exchange = stg_exchange.select('Alpha_2_code','Alpha_3_code','Country_name','Year','currency','value')

#rename columns
raw_exchange = raw_exchange.withColumnRenamed('Alpha_2_code','country_code') \
                           .withColumnRenamed('Alpha_3_code','country_code_iso') \
                           .withColumnRenamed('Country_name','country_name') \
                           .withColumnRenamed('Year','year_rate') \
                           .withColumnRenamed('currency','currency_name') \
                           .withColumnRenamed('value','value_rate')

#Show row exchange
raw_exchange.show(2)

#group by and select last value_rate 
df_group_rate = raw_exchange.select('country_code','year_rate','value_rate') \
        .groupBy('country_code',) \
        .agg(max('year_rate').alias('max_year'),last('value_rate').alias('value_exchange')) \
        .orderBy('country_code',asceding=False)
     
#show outgoing lines
print("lines clean outgoing: " , df_group_rate.count())

#Show row exchange
df_group_rate.show(5)

#join dataframe df_clean_products_raw && df_exchange_group
df_merge_rows = df_group_rate.alias('rate') \
                .join(df_clean_products_raw.alias('price'), col('price.country') == col('rate.country_code'), "inner")

#Show first 20 rows
df_merge_rows = df_merge_rows.select('product_id','isbestseller','isprime','app_sale_price_currency','clean_rate','app_sale_price','country_code','value_exchange') 

#show outgoing lines
print("lines clean outgoing: " , df_merge_rows.count())

#Show row mergedf_merge_rows
df_merge_rows.show(5)

##equivalente en dólares del precio de cada uno de los productos
df_raw_products=df_merge_rows.withColumn('app_sale_price_us', col('app_sale_price')/col('value_exchange'))

#Show first 2 rows
df_raw_products.show(n=2, truncate=False)

#Display Schema
df_raw_products.printSchema()

#renamed columns 
df_full_products = df_raw_products.withColumnRenamed('isprime','product_is_prime') \
                           .withColumnRenamed('app_sale_price_currency','product_price_currency') \
                           .withColumnRenamed('isbestseller','product_is_bestseller') \
                           .withColumnRenamed('clean_rate','product_rate') \
                           .withColumnRenamed('app_sale_price','product_price') \
                           .withColumnRenamed('country_code','product_country') \
                           .withColumnRenamed('app_sale_price_us','product_price_us')

#Show row exchange
df_full_products.show(2)

#drop columns value_exchange
df_full_products= df_full_products.drop('value_exchange')

df_full_products = df_full_products.withColumn("product_price",df_full_products.product_price.cast(DoubleType()))  \
                                    .withColumn("product_rate",df_full_products.product_rate.cast(DoubleType())) \
                                    .withColumn("product_is_bestseller",df_full_products.product_is_bestseller.cast(StringType())) \
                                    .withColumn("product_is_prime",df_full_products.product_is_prime.cast(StringType())) 
#Display Schema
df_full_products.printSchema()

df_full_products.show(5)

#####################################################################
########insert table pr_products to BigQuery Production #############
####################Products price US ###############################

df_full_products.write \
  .format("bigquery") \
  .option("table","becade_mgutierrez.pr_products_standard_price") \
  .option("temporaryGcsBucket", "amazon_magdielgutierrez") \
  .mode('overwrite') \
  .save()