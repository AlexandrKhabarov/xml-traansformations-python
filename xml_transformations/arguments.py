import json
import sys

from xml_transformations.entities import Arguments


def parse_arguments() -> Arguments:
    if len(sys.argv) != 5:
        sys.exit(1)

    return Arguments(
        input_path=sys.argv[1],
        output_path=sys.argv[2],
        column_name=sys.argv[3],
        paths=json.loads(sys.argv[4]),
    )
