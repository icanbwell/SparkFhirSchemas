import json
from pathlib import Path

from spark_fhir_schemas.validation.fhir_validator.v1.fhir_validator import FhirValidator


def test_fhir_validate_patient() -> None:
    data_dir: Path = Path(__file__).parent.joinpath('./')
    patient_good_path: Path = data_dir.joinpath("testfiles/patient_good.json")

    with open(patient_good_path, "r") as file:
        FhirValidator().validate(json.loads(file.read()))
