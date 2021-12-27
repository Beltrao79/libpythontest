def read_csv(spark, path):
    spark.read.option("delimiter", ";").option("header", "true").csv(path)