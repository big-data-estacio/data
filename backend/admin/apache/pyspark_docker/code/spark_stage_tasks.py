"""
SSH into the master node then run "spark-submit --master spark://master:7077 spark_stage_tasks.py"

This job will count number of info, warning and error and empty logs in the file.

"""

from pyspark import SparkContext

if __name__ == '__main__':
    sc = SparkContext(appName="log_counts_2")
    input = sc.textFile("/tmp/data/logs.txt")
    tokenized = input.map(lambda line: line.split(" ")).filter(lambda words: len(words) > 0)
    counts = tokenized.map(lambda words: (words[0], 1)).reduceByKey(lambda a, b: a + b)
    # print msg will be available as driver log
    print(counts.collect())
    counts.saveAsTextFile("/tmp/data/logsout")
