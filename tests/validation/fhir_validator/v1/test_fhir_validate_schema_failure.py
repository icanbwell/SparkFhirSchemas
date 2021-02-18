from fastjsonschema import JsonSchemaValueException
import pytest
from spark_fhir_schemas.validation.fhir_validator.v1.fhir_validator import FhirValidator


def test_fhir_validate_schema_failure() -> None:
    with pytest.raises(JsonSchemaValueException):
        FhirValidator.validate_schema(
            {
                '$schema': 'http://json-schema.org/draft-04/schema',
                'type': 'string'
            }, 1
        )
