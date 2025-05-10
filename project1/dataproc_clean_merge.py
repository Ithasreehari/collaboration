from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CleanAndMergeTransactions").getOrCreate()
df = spark.read.csv("gs://itha-bucket/scripts/*.csv", header=True, inferSchema=True)

df_clean = df.na.drop()
df_clean = df_clean.filter("transaction_id != ''")

df_clean.write.csv("gs://itha-bucket/processed/cleaned_transactions.csv", header=True, mode='overwrite')
spark.stop()