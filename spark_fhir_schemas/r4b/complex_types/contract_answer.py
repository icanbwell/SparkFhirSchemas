from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    IntegerType,
    DataType,
    FloatType,
    TimestampType,
)


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class Contract_AnswerSchema:
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
    ) -> Union[StructType, DataType]:
        """
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        valueBoolean: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDecimal: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueInteger: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDate: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueDateTime: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueTime: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueString: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueUri: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueAttachment: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueCoding: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueQuantity: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        valueReference: Response to an offer clause or question text,  which enables selection of
            values to be agreed to, e.g., the period of participation, the date of
            occupancy of a rental, warrently duration, or whether biospecimen may be used
            for further research.

        """
        if extension_fields is None:
            extension_fields = [
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
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4b.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4b.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.r4b.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4b.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.r4b.complex_types.reference import ReferenceSchema

        if (
            max_recursion_limit
            and nesting_list.count("Contract_Answer") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract_Answer"]
        my_parent_path = (
            parent_path + ".contract_answer" if parent_path else "contract_answer"
        )
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
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
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
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
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueBoolean", BooleanType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDecimal", FloatType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueInteger", IntegerType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDate", DateType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueDateTime", TimestampType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueTime", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueString", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField("valueUri", StringType(), True),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueCoding",
                    CodingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Response to an offer clause or question text,  which enables selection of
                # values to be agreed to, e.g., the period of participation, the date of
                # occupancy of a rental, warrently duration, or whether biospecimen may be used
                # for further research.
                StructField(
                    "valueReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema