from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TestScript_FixtureSchema:
    """
    A structured set of tests against a FHIR server implementation to determine
    compliance against the FHIR specification.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        A structured set of tests against a FHIR server implementation to determine
        compliance against the FHIR specification.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        autocreate: Whether or not to implicitly create the fixture during setup. If true, the
            fixture is automatically created on each server being tested during setup,
            therefore no create operation is required for this fixture in the
            TestScript.setup section.

        autodelete: Whether or not to implicitly delete the fixture during teardown. If true, the
            fixture is automatically deleted on each server being tested during teardown,
            therefore no delete operation is required for this fixture in the
            TestScript.teardown section.

        resource: Reference to the resource (containing the contents of the resource needed for
            operations).

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema

        if (
            max_recursion_limit
            and nesting_list.count("TestScript_Fixture") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Fixture"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Whether or not to implicitly create the fixture during setup. If true, the
                # fixture is automatically created on each server being tested during setup,
                # therefore no create operation is required for this fixture in the
                # TestScript.setup section.
                StructField("autocreate", BooleanType(), True),
                # Whether or not to implicitly delete the fixture during teardown. If true, the
                # fixture is automatically deleted on each server being tested during teardown,
                # therefore no delete operation is required for this fixture in the
                # TestScript.teardown section.
                StructField("autodelete", BooleanType(), True),
                # Reference to the resource (containing the contents of the resource needed for
                # operations).
                StructField(
                    "resource",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                (
                    c
                    if c.name != "extension"
                    else StructField("extension", StringType(), True)
                )
                for c in schema.fields
            ]

        return schema
