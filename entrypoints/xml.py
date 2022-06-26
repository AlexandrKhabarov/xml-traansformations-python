from pyspark.sql import SparkSession

from xml_transformations.main import main

if __name__ == '__main__':
    spark = SparkSession.builder.appName('XML').getOrCreate()
    main(spark)
    spark.stop()
