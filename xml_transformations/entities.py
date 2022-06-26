from dataclasses import dataclass
from typing import Dict


@dataclass
class Arguments:
    input_path: str
    output_path: str
    column_name: str
    paths: Dict[str, str]
