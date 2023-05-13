import findspark
findspark.init()

from pyspark.sql import SparkSession

# Aqui, substitua "local" pelo endereço do seu gerenciador de cluster.
# Por exemplo, se você estiver usando o gerenciador de cluster autônomo do Spark, poderia ser algo como "spark://master:7077"
spark = SparkSession.builder \
    .master("spark://estevam.localdomain:7077") \
    .appName("big-data") \
    .getOrCreate()

df = spark.createDataFrame([(1, 'John', 'Doe', 50),
                            (2, 'Jane', 'Doe', 45),
                            (3, 'Mike', 'Smith', 32)],
                           ['ID', 'First Name', 'Last Name', 'Age'])
df.show()
