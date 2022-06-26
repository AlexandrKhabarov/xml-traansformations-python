from pyspark.sql import SparkSession

from xml_transformations.arguments import parse_arguments
from xml_transformations.extract import extract
from xml_transformations.load import load  # noqa: WPS347
from xml_transformations.transform import transform


def main(spark: SparkSession) -> None:
    arguments = parse_arguments()
    df = extract(spark, arguments.input_path)
    df = transform(df, arguments.column_name, arguments.paths)
    load(df, arguments.output_path)
