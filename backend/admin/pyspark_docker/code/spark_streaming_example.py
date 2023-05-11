"""
This streaming job will watch on a directory, and trigger a new micro batch as there is a new file being added.
"""

# spark-submit spark_streaming_example.py
# reference of this script:
# http://cdn2.hubspot.net/hubfs/438089/notebooks/spark2.0/Structured%20Streaming%20using%20Python%20DataFrames%20API.html

from pyspark.sql import SparkSession
from pyspark.sql.functions import window
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("spark_streaming_example") \
    .getOrCreate()
inputPath = "/tmp/data/json_events"

# Since we know the data format already,
# let's define the schema to speed up processing (no need for Spark to infer schema)
jsonSchema = StructType([StructField("time", TimestampType(), True), StructField("action", StringType(), True)])

# Static DataFrame representing data in the JSON files
staticInputDF = spark.read.schema(jsonSchema).json(inputPath)
staticInputDF.show()

# calculates open and close events in a window of 1 hours
winf = window(staticInputDF.time, "1 hour")
staticInputDF.groupBy(staticInputDF.action, winf).count().show()


# Similar to definition of staticInputDF above, just using `readStream` instead of `read`
# Treat a sequence of files as a stream by picking one file at a time
streamingInputDF = spark.readStream.schema(jsonSchema).option("maxFilesPerTrigger", 1).json(inputPath)
# same as static df
winf_stream = window(streamingInputDF.time, "1 hour")

# init the counts df on streaming source df
streaming_counts_df = streamingInputDF.groupBy(streamingInputDF.action, winf_stream).count()
print("is streaming_counts_df really streaming df? ", streaming_counts_df.isStreaming)
spark.conf.set("spark.sql.shuffle.partitions", "2")  # keep the size of shuffles small

# query will be running in the background as stream data arrives in batches
query = (
    streaming_counts_df.writeStream.format("console")  # console print counts in real time in driver console
        .queryName("counts")  # counts = name of the in-memory table
        .outputMode("complete")  # complete = all the counts should be in the table
        .start()
)
# keep the streaming job and query long running
query.awaitTermination()
