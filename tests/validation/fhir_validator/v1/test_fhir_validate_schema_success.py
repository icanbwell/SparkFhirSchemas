from spark_fhir_schemas.validation.fhir_validator.v1.fhir_validator import FhirValidator


def test_fhir_validate_schema_success() -> None:
    FhirValidator.validate_schema(
        {
            '$schema': 'http://json-schema.org/draft-04/schema',
            'type': 'string'
        }, 'hello'
    )
