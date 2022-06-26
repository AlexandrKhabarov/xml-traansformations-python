import json

from pyspark.sql import types as st

from xml_transformations.main import main


def test_main(
    mocker,
    tmp_path,
    fake_spark,
    create_dataframe,
    assert_dataframes,
):
    input_path, output_path = (
        str(tmp_path / 'test'),
        str(tmp_path / 'expected'),
    )

    create_dataframe({
        ('xml', st.StringType()): [
            '<?xml version="1.0"?>'
            + '<attr>'
            + '<some>'
            + '<some_attr>1</some_attr>'
            + '<some_attr>2</some_attr>'
            + '<some_attr>3</some_attr>'
            + '</some>'
            + '<another_attr>1</another_attr>'
            + '</attr>'
        ],
    }).write.parquet(input_path)

    mocker.patch(
        'sys.argv',
        [
            'test_main.py',
            input_path,
            output_path,
            'xml',
            json.dumps({
                'some_attrs': 'attr/some/some_attr',
                'another_attr': 'attr/another_attr',
            })
        ],
    )

    main(fake_spark)

    assert_dataframes(
        expected_df=create_dataframe({
            ('some_attrs', st.ArrayType(st.StringType())): [['1', '2', '3']],
            ('another_attr', st.ArrayType(st.StringType())): [['1']],
        }),
        actual_df=fake_spark.read.parquet(output_path),
    )
