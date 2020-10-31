from spark_fhir_schemas.r4.complex_types.address import Address
from spark_fhir_schemas.r4.resources.patient import Patient


def test_simple() -> None:
    Patient.get_schema()

    Address.get_schema()

    assert 1 == 1
