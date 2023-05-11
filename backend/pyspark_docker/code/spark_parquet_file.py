"""
This is a copy from official example src/examples/python
How to use it:
spark-submit /code/spark_parquet_file.py /data/json_as_parquet
"""

import sys

from pyspark.sql import SparkSession

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: spark_parquet_file.py <file>", file=sys.stderr)
        sys.exit(-1)
    spark = SparkSession \
        .builder \
        .appName("Python Spark parquet data") \
        .getOrCreate()
    parquet_file = sys.argv[1]

    # parquet file
    dfparquet = spark.read.parquet(parquet_file)
    dfparquet.show()
    # we partition the table by favorite color, it will create a directory accordingly
    dfparquet.write.partitionBy("age").format("parquet").save("/data/repartitionedByAge", mode="overwrite")
