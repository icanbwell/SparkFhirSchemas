from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CompositionEventSchema:
    """
    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of meaning,
    establishes its own context and that has clinical attestation with regard to
    who is making the statement. While a Composition defines the structure, it
    does not actually contain the content: rather the full content of a document
    is contained in a Bundle, of which the Composition is the first resource
    contained.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of meaning,
    establishes its own context and that has clinical attestation with regard to
    who is making the statement. While a Composition defines the structure, it
    does not actually contain the content: rather the full content of a document
    is contained in a Bundle, of which the Composition is the first resource
    contained.


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
        code: This list of codes represents the main clinical acts, such as a colonoscopy or
    an appendectomy, being documented. In some cases, the event is inherent in the
    typeCode, such as a "History and Physical Report" in which the procedure being
    documented is necessarily a "History and Physical" act.
        period: The period of time covered by the documentation. There is no assertion that
    the documentation is a complete representation for this period, only that it
    documents events during this time.
        detail: The description and/or reference of the event(s) being documented. For
    example, this could be used to document such a colonoscopy or an appendectomy.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # modifierExtension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # code
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
            # period
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
            # detail
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        if (max_recursion_limit and nesting_list.count("CompositionEvent") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["CompositionEvent"]
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
                # This list of codes represents the main clinical acts, such as a colonoscopy or
                # an appendectomy, being documented. In some cases, the event is inherent in the
                # typeCode, such as a "History and Physical Report" in which the procedure being
                # documented is necessarily a "History and Physical" act.
                StructField("code", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The period of time covered by the documentation. There is no assertion that
                # the documentation is a complete representation for this period, only that it
                # documents events during this time.
                StructField("period", PeriodSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The description and/or reference of the event(s) being documented. For
                # example, this could be used to document such a colonoscopy or an appendectomy.
                StructField("detail", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema