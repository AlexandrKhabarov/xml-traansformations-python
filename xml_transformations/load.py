from pyspark.sql import DataFrame


def load(df: DataFrame, path: str) -> None:
    df.write.parquet(path, mode='overwrite')
