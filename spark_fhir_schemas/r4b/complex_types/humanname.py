from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class HumanNameSchema:
    """
    A human's name with the ability to identify parts and usage.
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
        A human's name with the ability to identify parts and usage.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        use: Identifies the purpose for this name.

        text: Specifies the entire name as it should be displayed e.g. on an application UI.
            This may be provided instead of or as well as the specific parts.

        family: The part of a name that links to the genealogy. In some cultures (e.g.
            Eritrea) the family name of a son is the first name of his father.

        given: Given name.

        prefix: Part of the name that is acquired as a title due to academic, legal,
            employment or nobility status, etc. and that appears at the start of the name.

        suffix: Part of the name that is acquired as a title due to academic, legal,
            employment or nobility status, etc. and that appears at the end of the name.

        period: Indicates the period of time when this name was valid for the named person.

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
        from spark_fhir_schemas.r4b.complex_types.period import PeriodSchema

        if (
            max_recursion_limit
            and nesting_list.count("HumanName") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["HumanName"]
        my_parent_path = parent_path + ".humanname" if parent_path else "humanname"
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
                # Identifies the purpose for this name.
                StructField("use", StringType(), True),
                # Specifies the entire name as it should be displayed e.g. on an application UI.
                # This may be provided instead of or as well as the specific parts.
                StructField("text", StringType(), True),
                # The part of a name that links to the genealogy. In some cultures (e.g.
                # Eritrea) the family name of a son is the first name of his father.
                StructField("family", StringType(), True),
                # Given name.
                StructField("given", ArrayType(StringType()), True),
                # Part of the name that is acquired as a title due to academic, legal,
                # employment or nobility status, etc. and that appears at the start of the name.
                StructField("prefix", ArrayType(StringType()), True),
                # Part of the name that is acquired as a title due to academic, legal,
                # employment or nobility status, etc. and that appears at the end of the name.
                StructField("suffix", ArrayType(StringType()), True),
                # Indicates the period of time when this name was valid for the named person.
                StructField(
                    "period",
                    PeriodSchema.get_schema(
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