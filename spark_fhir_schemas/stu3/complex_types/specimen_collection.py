from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DataType,
    TimestampType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Specimen_CollectionSchema:
    """
    A sample to be used for analysis.
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
        A sample to be used for analysis.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        collector: Person who collected the specimen.

        collectedDateTime: Time when specimen was collected from subject - the physiologically relevant
            time.

        collectedPeriod: Time when specimen was collected from subject - the physiologically relevant
            time.

        quantity: The quantity of specimen collected; for instance the volume of a blood sample,
            or the physical measurement of an anatomic pathology sample.

        method: A coded value specifying the technique that is used to perform the procedure.

        bodySite: Anatomical location from which the specimen was collected (if subject is a
            patient). This is the target site.  This element is not used for environmental
            specimens.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Specimen_Collection") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Specimen_Collection"]
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
                # Person who collected the specimen.
                StructField(
                    "collector",
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
                # Time when specimen was collected from subject - the physiologically relevant
                # time.
                StructField("collectedDateTime", TimestampType(), True),
                # Time when specimen was collected from subject - the physiologically relevant
                # time.
                StructField(
                    "collectedPeriod",
                    PeriodSchema.get_schema(
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
                # The quantity of specimen collected; for instance the volume of a blood sample,
                # or the physical measurement of an anatomic pathology sample.
                StructField(
                    "quantity",
                    QuantitySchema.get_schema(
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
                # A coded value specifying the technique that is used to perform the procedure.
                StructField(
                    "method",
                    CodeableConceptSchema.get_schema(
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
                # Anatomical location from which the specimen was collected (if subject is a
                # patient). This is the target site.  This element is not used for environmental
                # specimens.
                StructField(
                    "bodySite",
                    CodeableConceptSchema.get_schema(
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
