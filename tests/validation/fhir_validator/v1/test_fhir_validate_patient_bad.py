import json
from pathlib import Path

from fastjsonschema import JsonSchemaValueException
import pytest
from spark_fhir_schemas.validation.fhir_validator.v1.fhir_validator import FhirValidator


def test_fhir_validate_patient_bad() -> None:
    data_dir: Path = Path(__file__).parent.joinpath('./')
    patient_bad_path: Path = data_dir.joinpath("testfiles/patient_bad.json")

    with open(patient_bad_path, "r") as file:
        with pytest.raises(JsonSchemaValueException):
            FhirValidator().validate(json.loads(file.read()))
