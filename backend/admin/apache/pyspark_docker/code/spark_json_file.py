"""
This is a copy from official example src/examples/python
How to use it:
spark-submit /code/spark_json_file.py /data/people.json
"""

import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: spark_json_file.py <file>", file=sys.stderr)
        sys.exit(-1)
    spark = SparkSession \
        .builder \
        .appName("spark JSON file processing") \
        .getOrCreate()
    people_json_file = sys.argv[1]
    # json file
    # The schema is encoded in a string.
    fields = [StructField("name", StringType(), nullable=True),
              StructField("age", StringType(), nullable=True)]
    schema = StructType(fields)
    df = spark.read.json(people_json_file, schema=schema)
    df.show()
    df.createOrReplaceTempView("people")
    sqldf = spark.sql("select * from people where age > 20")
    sqldf.show()
