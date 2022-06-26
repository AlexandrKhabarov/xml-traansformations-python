from pyspark.sql import DataFrame, SparkSession


def extract(spark: SparkSession, path: str) -> DataFrame:
    return (
        spark
        .read
        .parquet(path)
    )
