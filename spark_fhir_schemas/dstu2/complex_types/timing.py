from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class TimingSchema:
    """
    Specifies an event that may occur multiple times. Timing schedules are used to
    record when things are expected or requested to occur. The most common usage
    is in dosage instructions for medications. They are also used when planning
    care of various kinds.
    If the element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    Specifies an event that may occur multiple times. Timing schedules are used to
    record when things are expected or requested to occur. The most common usage
    is in dosage instructions for medications. They are also used when planning
    care of various kinds.
    If the element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or extensions


        id: None
        extension: May be used to represent additional information that is not part of the basic
    definition of the element. In order to make the use of extensions safe and
    manageable, there is a strict set of governance  applied to the definition and
    use of extensions. Though any implementer is allowed to define an extension,
    there is a set of requirements that SHALL be met as part of the definition of
    the extension.
        event: Identifies specific times when the event occurs.
        repeat: A set of rules that describe when the event should occur.
        code: A code for the timing pattern. Some codes such as BID are ubiquitous, but many
    institutions define their own additional codes.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # event
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema
            # repeat
        from spark_fhir_schemas.dstu2.complex_types.timingrepeat import TimingRepeatSchema
            # code
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
        if (max_recursion_limit and nesting_list.count("Timing") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["Timing"]
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
                # Identifies specific times when the event occurs.
                StructField("event", dateTimeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A set of rules that describe when the event should occur.
                StructField("repeat", TimingRepeatSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A code for the timing pattern. Some codes such as BID are ubiquitous, but many
                # institutions define their own additional codes.
                StructField("code", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema