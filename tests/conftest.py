from typing import Any, Dict, List, Tuple

import pytest
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import types as st


@pytest.fixture(name='fake_spark', scope='session')
def spark():
    session = (
        SparkSession
        .builder
        .master('local')
        .appName('tests')
        .getOrCreate()
    )

    yield session

    session.stop()


@pytest.fixture()
def create_dataframe(fake_spark: SparkSession):
    def factory(fields: Dict[Tuple[str, st.DataType], List[Any]]) -> DataFrame:
        return fake_spark.createDataFrame(
            list(zip(*fields.values())),
            schema=st.StructType([
                st.StructField(
                    column_name,
                    column_type,
                )
                for column_name, column_type in fields.keys()
            ]),
        )

    return factory


@pytest.fixture
def assert_dataframes():
    def factory(*, expected_df: DataFrame, actual_df: DataFrame) -> None:
        expected_schema = [field.simpleString() for field in expected_df.schema]
        actual_schema = [field.simpleString() for field in actual_df.schema]

        assert sorted(expected_schema) == sorted(actual_schema)

        sorted_expected_df = (
            expected_df
            .select(actual_df.columns)
            .orderBy(actual_df.columns)
            .collect()
        )

        sorted_actual_df = (
            actual_df
            .orderBy(actual_df.columns)
            .collect()
        )

        assert sorted_expected_df == sorted_actual_df

    return factory
