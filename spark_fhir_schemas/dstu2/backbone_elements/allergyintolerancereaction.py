from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class AllergyIntoleranceReactionSchema:
    """
    Risk of harmful or undesirable, physiological response which is unique to an
    individual and associated with exposure to a substance.
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
        Risk of harmful or undesirable, physiological response which is unique to an
        individual and associated with exposure to a substance.


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
            substance: Identification of the specific substance considered to be responsible for the
        Adverse Reaction event. Note: the substance for a specific reaction may be
        different to the substance identified as the cause of the risk, but must be
        consistent with it. For instance, it may be a more specific substance (e.g. a
        brand medication) or a composite substance that includes the identified
        substance. It must be clinically safe to only process the
        AllergyIntolerance.substance and ignore the
        AllergyIntolerance.event.substance.
            certainty: Statement about the degree of clinical certainty that the specific substance
        was the cause of the manifestation in this reaction event.
            manifestation: Clinical symptoms and/or signs that are observed or associated with the
        adverse reaction event.
            description: Text description about the reaction as a whole, including details of the
        manifestation if required.
            onset: Record of the date and/or time of the onset of the Reaction.
            severity: Clinical assessment of the severity of the reaction event as a whole,
        potentially considering multiple different manifestations.
            exposureRoute: Identification of the route by which the subject was exposed to the substance.
            note: Additional text about the adverse reaction event not captured in other fields.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # substance
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        # certainty
        # type = code
        # onset
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema

        # note
        from spark_fhir_schemas.dstu2.complex_types.annotation import AnnotationSchema

        if (
            max_recursion_limit
            and nesting_list.count("AllergyIntoleranceReaction") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["AllergyIntoleranceReaction"]
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
                # Identification of the specific substance considered to be responsible for the
                # Adverse Reaction event. Note: the substance for a specific reaction may be
                # different to the substance identified as the cause of the risk, but must be
                # consistent with it. For instance, it may be a more specific substance (e.g. a
                # brand medication) or a composite substance that includes the identified
                # substance. It must be clinically safe to only process the
                # AllergyIntolerance.substance and ignore the
                # AllergyIntolerance.event.substance.
                StructField(
                    "substance",
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
                # Statement about the degree of clinical certainty that the specific substance
                # was the cause of the manifestation in this reaction event.
                StructField("certainty", StringType(), True),
                # Clinical symptoms and/or signs that are observed or associated with the
                # adverse reaction event.
                StructField(
                    "manifestation",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
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
                # Text description about the reaction as a whole, including details of the
                # manifestation if required.
                StructField("description", StringType(), True),
                # Record of the date and/or time of the onset of the Reaction.
                StructField(
                    "onset",
                    dateTimeSchema.get_schema(
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
                # Clinical assessment of the severity of the reaction event as a whole,
                # potentially considering multiple different manifestations.
                StructField("severity", StringType(), True),
                # Identification of the route by which the subject was exposed to the substance.
                StructField(
                    "exposureRoute",
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
                # Additional text about the adverse reaction event not captured in other fields.
                StructField(
                    "note",
                    AnnotationSchema.get_schema(
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
