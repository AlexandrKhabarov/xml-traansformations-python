from typing import Dict, List

from pyspark.sql import DataFrame


def transform(df: DataFrame, source_column: str, columns_to_paths: Dict[str, str]) -> DataFrame:
    return (
        df.selectExpr(
            *_format_expr(
                source_column,
                columns_to_paths,
            ),
        )
        .coalesce(1)
    )


def _format_expr(source_column: str, columns_to_paths: Dict[str, str]) -> List[str]:
    return [
        "xpath({source_column}, '{path}/text()') as {column}".format(
            source_column=source_column,
            path=path.strip('/'),
            column=column,
        )
        for column, path in columns_to_paths.items()
    ]
