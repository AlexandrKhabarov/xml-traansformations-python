#!/bin/bash

set -e

poetry build

JOB="entrypoints/xml.py"
INPUT_FILE_PATH="./resources/xml/"
OUTPUT_PATH="./output"
COLUMN_NAME="response_xml"
PATHS="{\"INQ_PERIOD\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_PERIOD\", \"INQ_PURPOSE\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_PURPOSE\", \"INQ_AMT\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_AMT\", \"INQ_CURRENCY\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_CURRENCY\", \"INQ_QTY\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_QTY\", \"INQ_OWN\": \"/SINGLE_FORMAT/INQUIRIES/INQUIRY/INQ_OWN\"}"

rm -rf $OUTPUT_PATH

poetry run spark-submit \
    --master local \
    --py-files dist/xml_transformations-*.whl \
    $JOB \
    $INPUT_FILE_PATH \
    $OUTPUT_PATH \
    $COLUMN_NAME \
    $PATHS
