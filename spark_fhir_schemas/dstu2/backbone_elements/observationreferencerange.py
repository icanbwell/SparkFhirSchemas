from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ObservationReferenceRangeSchema:
    """
    Measurements and simple assertions made about a patient, device or other
    subject.
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
        Measurements and simple assertions made about a patient, device or other
        subject.


            id: None
            extension: May be used to represent additional information that is not part of the basic
        definition of the element. In order to make the use of extensions safe and
        manageable, there is a strict set of governance  applied to the definition and
        use of extensions. Though any implementer is allowed to define an extension,
        there is a set of requirements that SHALL be met as part of the definition of
        the extension.
            modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element, and that modifies the understanding of the element
        that contains it. Usually modifier elements provide negation or qualification.
        In order to make the use of extensions safe and manageable, there is a strict
        set of governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.
            low: The value of the low bound of the reference range.  The low bound of the
        reference range endpoint is inclusive of the value (e.g.  reference range is
        >=5 - <=9).   If the low bound is omitted,  it is assumed to be meaningless
        (e.g. reference range is <=2.3).
            high: The value of the high bound of the reference range.  The high bound of the
        reference range endpoint is inclusive of the value (e.g.  reference range is
        >=5 - <=9).   If the high bound is omitted,  it is assumed to be meaningless
        (e.g. reference range is >= 2.3).
            meaning: Code for the meaning of the reference range.
            age: The age at which this reference range is applicable. This is a neonatal age
        (e.g. number of weeks at term) if the meaning says so.
            text: Text based reference range in an observation which may be used when a
        quantitative range is not appropriate for an observation.  An example would be
        a reference value of "Negative" or a list or table of 'normals'.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # low
        from spark_fhir_schemas.dstu2.complex_types.simplequantity import (
            SimpleQuantitySchema,
        )

        # meaning
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        # age
        from spark_fhir_schemas.dstu2.complex_types.range import RangeSchema

        if (
            max_recursion_limit
            and nesting_list.count("ObservationReferenceRange") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ObservationReferenceRange"]
        schema = StructType(
            [
                # None
                StructField(
                    "id",
                    idSchema.get_schema(
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
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField(
                    "modifierExtension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The value of the low bound of the reference range.  The low bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9).   If the low bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is <=2.3).
                StructField(
                    "low",
                    SimpleQuantitySchema.get_schema(
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
                # The value of the high bound of the reference range.  The high bound of the
                # reference range endpoint is inclusive of the value (e.g.  reference range is
                # >=5 - <=9).   If the high bound is omitted,  it is assumed to be meaningless
                # (e.g. reference range is >= 2.3).
                StructField(
                    "high",
                    SimpleQuantitySchema.get_schema(
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
                # Code for the meaning of the reference range.
                StructField(
                    "meaning",
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
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age",
                    RangeSchema.get_schema(
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
                # Text based reference range in an observation which may be used when a
                # quantitative range is not appropriate for an observation.  An example would be
                # a reference value of "Negative" or a list or table of 'normals'.
                StructField("text", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        return schema