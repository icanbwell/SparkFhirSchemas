from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OrganizationContactSchema:
    """
    A formally or informally recognized grouping of people or organizations formed
    for the purpose of achieving some form of collective action.  Includes
    companies, institutions, corporations, departments, community groups,
    healthcare practice groups, etc.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    A formally or informally recognized grouping of people or organizations formed
    for the purpose of achieving some form of collective action.  Includes
    companies, institutions, corporations, departments, community groups,
    healthcare practice groups, etc.


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
        purpose: Indicates a purpose for which the contact can be reached.
        name: A name associated with the contact.
        telecom: A contact detail (e.g. a telephone number or an email address) by which the
    party may be contacted.
        address: Visiting or postal addresses for the contact.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # modifierExtension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # purpose
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
            # name
        from spark_fhir_schemas.dstu2.complex_types.humanname import HumanNameSchema
            # telecom
        from spark_fhir_schemas.dstu2.complex_types.contactpoint import ContactPointSchema
            # address
        from spark_fhir_schemas.dstu2.complex_types.address import AddressSchema
        if (max_recursion_limit and nesting_list.count("OrganizationContact") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["OrganizationContact"]
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
                # Indicates a purpose for which the contact can be reached.
                StructField("purpose", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A name associated with the contact.
                StructField("name", HumanNameSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A contact detail (e.g. a telephone number or an email address) by which the
                # party may be contacted.
                StructField("telecom", ContactPointSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Visiting or postal addresses for the contact.
                StructField("address", AddressSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema