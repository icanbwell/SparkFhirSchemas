from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NamingSystemUniqueIdSchema:
    """
    A curated namespace that issues unique symbols within that namespace for the
    identification of concepts, people, devices, etc.  Represents a "System" used
    within the Identifier and Coding data types.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    A curated namespace that issues unique symbols within that namespace for the
    identification of concepts, people, devices, etc.  Represents a "System" used
    within the Identifier and Coding data types.


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
        type: Identifies the unique identifier scheme used for this particular identifier.
        value: The string that should be sent over the wire to identify the code system or
    identifier system.
        preferred: Indicates whether this identifier is the "preferred" identifier of this type.
        period: Identifies the period of time over which this identifier is considered
    appropriate to refer to the naming system.  Outside of this window, the
    identifier might be non-deterministic.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # modifierExtension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # type
        from spark_fhir_schemas.dstu2.simple_types.namingsystemidentifiertype import NamingSystemIdentifierTypeSchema
            # value
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # preferred
        from spark_fhir_schemas.dstu2.simple_types.boolean import booleanSchema
            # period
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
        if (max_recursion_limit and nesting_list.count("NamingSystemUniqueId") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["NamingSystemUniqueId"]
        schema = StructType(
            [
                # None
                StructField("id", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField("extension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField("modifierExtension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifies the unique identifier scheme used for this particular identifier.
                StructField("type", StringType(), True),
                # The string that should be sent over the wire to identify the code system or
                # identifier system.
                StructField("value", StringType(), True),
                # Indicates whether this identifier is the "preferred" identifier of this type.
                StructField("preferred", BooleanType(), True),
                # Identifies the period of time over which this identifier is considered
                # appropriate to refer to the naming system.  Outside of this window, the
                # identifier might be non-deterministic.
                StructField("period", PeriodSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema