from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

df = spark.read.csv("../data/employees.csv", header=True, inferSchema=True)

df = df.withColumn("bonus", df["salary"] * 0.2)
df = df.filter(df["department"] == "IT")

df.write.mode("overwrite").csv("../data/spark_output", header=True)

print("PySpark ETL completed successfully")

spark.stop()