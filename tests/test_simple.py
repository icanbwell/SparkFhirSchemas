from spark_fhir_schemas.r4.complex_types.address import AddressSchema
from spark_fhir_schemas.r4.resources.patient import PatientSchema


def test_simple() -> None:
    PatientSchema.get_schema()

    AddressSchema.get_schema()

    assert 1 == 1
