from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class SupplyDeliverySchema:
    """
    Record of delivery of what is supplied.
    If the element is present, it must have either a @value, an @id, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    Record of delivery of what is supplied.
    If the element is present, it must have either a @value, an @id, or extensions


        id: The logical id of the resource, as used in the URL for the resource. Once
    assigned, this value never changes.
        meta: The metadata about the resource. This is content that is maintained by the
    infrastructure. Changes to the content may not always be associated with
    version changes to the resource.
        implicitRules: A reference to a set of rules that were followed when the resource was
    constructed, and which must be understood when processing the content.
        language: The base language in which the resource is written.
        text: A human-readable narrative that contains a summary of the resource, and may be
    used to represent the content of the resource to a human. The narrative need
    not encode all the structured data, but is required to contain sufficient
    detail to make it "clinically safe" for a human to just read the narrative.
    Resource definitions may define what content should be represented in the
    narrative to ensure clinical safety.
        contained: These resources do not have an independent existence apart from the resource
    that contains them - they cannot be identified independently, and nor can they
    have their own independent transaction scope.
        extension: May be used to represent additional information that is not part of the basic
    definition of the resource. In order to make the use of extensions safe and
    manageable, there is a strict set of governance  applied to the definition and
    use of extensions. Though any implementer is allowed to define an extension,
    there is a set of requirements that SHALL be met as part of the definition of
    the extension.
        modifierExtension: May be used to represent additional information that is not part of the basic
    definition of the resource, and that modifies the understanding of the element
    that contains it. Usually modifier elements provide negation or qualification.
    In order to make the use of extensions safe and manageable, there is a strict
    set of governance applied to the definition and use of extensions. Though any
    implementer is allowed to define an extension, there is a set of requirements
    that SHALL be met as part of the definition of the extension. Applications
    processing a resource are required to check for modifier extensions.
        identifier: Identifier assigned by the dispensing facility when the item(s) is dispensed.
        status: A code specifying the state of the dispense event.
        patient: A link to a resource representing the person whom the delivered item is for.
        type: Indicates the type of dispensing event that is performed. Examples include:
    Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
        quantity: The amount of supply that has been dispensed. Includes unit of measure.
        suppliedItem: Identifies the medication, substance or device being dispensed. This is either
    a link to a resource representing the details of the item or a simple
    attribute carrying a code that identifies the item from a known list.
        supplier: The individual responsible for dispensing the medication, supplier or device.
        whenPrepared: The time the dispense event occurred.
        time: The time the dispensed item was sent or handed to the patient (or agent).
        destination: Identification of the facility/location where the Supply was shipped to, as
    part of the dispense event.
        receiver: Identifies the person who picked up the Supply.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # meta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema
            # implicitRules
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema
            # language
        from spark_fhir_schemas.dstu2.simple_types.code import codeSchema
            # text
        from spark_fhir_schemas.dstu2.complex_types.narrative import NarrativeSchema
            # contained
        Not mapped: ResourceContainer
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # modifierExtension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # identifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # status
        from spark_fhir_schemas.dstu2.simple_types.supplydeliverystatus import SupplyDeliveryStatusSchema
            # patient
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # type
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
            # quantity
        Not mapped: SimpleQuantity
            # suppliedItem
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # supplier
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # whenPrepared
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
            # time
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema
            # destination
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # receiver
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        if (max_recursion_limit and nesting_list.count("SupplyDelivery") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["SupplyDelivery"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField("meta", MetaSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", codeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField("text", NarrativeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField("contained", ResourceContainerSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField("extension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField("modifierExtension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifier assigned by the dispensing facility when the item(s) is dispensed.
                StructField("identifier", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A code specifying the state of the dispense event.
                StructField("status", StringType(), True),
                # A link to a resource representing the person whom the delivered item is for.
                StructField("patient", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Indicates the type of dispensing event that is performed. Examples include:
                # Trial Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
                StructField("type", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The amount of supply that has been dispensed. Includes unit of measure.
                StructField("quantity", SimpleQuantitySchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifies the medication, substance or device being dispensed. This is either
                # a link to a resource representing the details of the item or a simple
                # attribute carrying a code that identifies the item from a known list.
                StructField("suppliedItem", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The individual responsible for dispensing the medication, supplier or device.
                StructField("supplier", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The time the dispense event occurred.
                StructField("whenPrepared", PeriodSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The time the dispensed item was sent or handed to the patient (or agent).
                StructField("time", dateTimeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identification of the facility/location where the Supply was shipped to, as
                # part of the dispense event.
                StructField("destination", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifies the person who picked up the Supply.
                StructField("receiver", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema