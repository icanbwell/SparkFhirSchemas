import json
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict

import fastjsonschema


class FhirValidator:
    def __init__(self) -> None:
        data_dir: Path = Path(__file__).parent.joinpath('./')
        fhir_schema_path: Path = data_dir.joinpath(
            '../../../r4/fhir.schema.json'
        )
        with open(fhir_schema_path, "r") as file:
            schema_text = file.read()
            schema_json = json.loads(schema_text)
            self.schema_validator: Callable[
                [Any], None] = fastjsonschema.compile(schema_json)

    def validate(self, content: Any) -> bool:
        """
        Checks the content against schema and throws error if validation fails
        :param content:
        """
        self.schema_validator(content)
        return True

    @staticmethod
    def validate_schema(schema: Dict[str, Any], content: Any) -> bool:
        """
        Checks the content against schema and throws error if validation fails
        :param schema:
        :param content:
        """
        validate = fastjsonschema.compile(schema)
        validate(content)
        return True
