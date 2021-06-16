from spark_fhir_schemas.r4.resources.patient import PatientSchema


def test_control_extensions() -> None:
    # schema = PatientSchema.get_schema()
    # assert schema["extension"].dataType == StringType()
    # schema_extensions = PatientSchema.get_schema(include_extension=True)
    # assert schema_extensions["extension"].dataType != StringType()
    # schema_with_extensions_nested_2 = PatientSchema.get_schema(
    #     include_extension=True, max_extension_depth=2
    # )
    # assert schema_with_extensions_nested_2.fields[7].dataType.elementType.fields[1].dataType.elementType.fields[
    #            1].dataType.elementType.fields[0].dataType == StringType()
    schema_with_extensions_subset = PatientSchema.get_schema(
        include_extension=True,
        max_extension_depth=2,
        extension_fields=["valueString", "valueCode"],
    )
    print("ff")
