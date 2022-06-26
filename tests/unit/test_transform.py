import pytest
from pyspark.sql import types as st

from xml_transformations.transform import transform

_SOURCE_COLUMN_NAME = 'xml'
_TARGET_COLUMN_NAME = 'some_attrs'


@pytest.mark.parametrize(
    (
        'test_paths',
        'test_data',
        'expected_data',
    ),
    [
        (
            {
                _TARGET_COLUMN_NAME: 'attr/some_attr',
            },
            {
                (_SOURCE_COLUMN_NAME, st.StringType()): [],
            },
            {
                (_TARGET_COLUMN_NAME, st.ArrayType(st.StringType())): [],
            },
        ),
        (
            {
                _TARGET_COLUMN_NAME: 'attr/some_attr',
            },
            {
                (_SOURCE_COLUMN_NAME, st.StringType()): [
                    '<?xml version="1.0"?>'
                    + '<attr>'
                    + '<some_attr>1</some_attr>'
                    + '<some_attr>2</some_attr>'
                    + '<some_attr>3</some_attr>'
                    + '</attr>',
                ],
            },
            {
                (_TARGET_COLUMN_NAME, st.ArrayType(st.StringType())): [['1', '2', '3']],
            },
        ),
        (
            {
                _TARGET_COLUMN_NAME: 'attr/some/some_attr',
                'another_attr': 'attr/another_attr',
            },
            {
                (_SOURCE_COLUMN_NAME, st.StringType()): [
                    '<?xml version="1.0"?>'
                    + '<attr>'
                    + '<some>'
                    + '<some_attr>1</some_attr>'
                    + '<some_attr>2</some_attr>'
                    + '<some_attr>3</some_attr>'
                    + '</some>'
                    + '<another_attr>1</another_attr>'
                    + '</attr>',
                ],
            },
            {
                (_TARGET_COLUMN_NAME, st.ArrayType(st.StringType())): [['1', '2', '3']],
                ('another_attr', st.ArrayType(st.StringType())): [['1']],
            },
        ),
    ],
)
def test_transform(
    test_paths,
    test_data,
    expected_data,
    create_dataframe,
    assert_dataframes,
):
    actual_df = transform(
        create_dataframe(test_data),
        'xml',
        test_paths,
    )
    assert_dataframes(
        expected_df=create_dataframe(
            expected_data,
        ),
        actual_df=actual_df,
    )
