from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DiagnosticOrderSchema:
    """
    A record of a request for a diagnostic investigation service to be performed.
    If the element is present, it must have either a @value, an @id, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    A record of a request for a diagnostic investigation service to be performed.
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
        subject: Who or what the investigation is to be performed on. This is usually a human
    patient, but diagnostic tests can also be requested on animals, groups of
    humans or animals, devices such as dialysis machines, or even locations
    (typically for environmental scans).
        orderer: The practitioner that holds legal responsibility for ordering the
    investigation.
        identifier: Identifiers assigned to this order instance by the orderer and/or  the
    receiver and/or order fulfiller.
        encounter: An encounter that provides additional information about the healthcare context
    in which this request is made.
        reason: An explanation or justification for why this diagnostic investigation is being
    requested.   This is often for billing purposes.  May relate to the resources
    referred to in supportingInformation.
        supportingInformation: Additional clinical information about the patient or specimen that may
    influence test interpretations.  This includes observations explicitly
    requested by the producer(filler) to provide context or supporting information
    needed to complete the order.
        specimen: One or more specimens that the diagnostic investigation is about.
        status: The status of the order.
        priority: The clinical priority associated with this order.
        event: A summary of the events of interest that have occurred as the request is
    processed; e.g. when the order was made, various processing steps (specimens
    received), when it was completed.
        item: The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
        note: Any other notes associated with this patient, specimen or order (e.g. "patient
    hates needles").
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
            # subject
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # orderer
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # identifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # encounter
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # reason
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
            # supportingInformation
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # specimen
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # status
        from spark_fhir_schemas.dstu2.simple_types.diagnosticorderstatus import DiagnosticOrderStatusSchema
            # priority
        from spark_fhir_schemas.dstu2.simple_types.diagnosticorderpriority import DiagnosticOrderPrioritySchema
            # event
        Not mapped: DiagnosticOrderEvent
            # item
        Not mapped: DiagnosticOrderItem
            # note
        from spark_fhir_schemas.dstu2.complex_types.annotation import AnnotationSchema
        if (max_recursion_limit and nesting_list.count("DiagnosticOrder") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["DiagnosticOrder"]
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
                # Who or what the investigation is to be performed on. This is usually a human
                # patient, but diagnostic tests can also be requested on animals, groups of
                # humans or animals, devices such as dialysis machines, or even locations
                # (typically for environmental scans).
                StructField("subject", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The practitioner that holds legal responsibility for ordering the
                # investigation.
                StructField("orderer", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifiers assigned to this order instance by the orderer and/or  the
                # receiver and/or order fulfiller.
                StructField("identifier", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # An encounter that provides additional information about the healthcare context
                # in which this request is made.
                StructField("encounter", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # An explanation or justification for why this diagnostic investigation is being
                # requested.   This is often for billing purposes.  May relate to the resources
                # referred to in supportingInformation.
                StructField("reason", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Additional clinical information about the patient or specimen that may
                # influence test interpretations.  This includes observations explicitly
                # requested by the producer(filler) to provide context or supporting information
                # needed to complete the order.
                StructField("supportingInformation", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # One or more specimens that the diagnostic investigation is about.
                StructField("specimen", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The status of the order.
                StructField("status", StringType(), True),
                # The clinical priority associated with this order.
                StructField("priority", StringType(), True),
                # A summary of the events of interest that have occurred as the request is
                # processed; e.g. when the order was made, various processing steps (specimens
                # received), when it was completed.
                StructField("event", DiagnosticOrderEventSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The specific diagnostic investigations that are requested as part of this
                # request. Sometimes, there can only be one item per request, but in most
                # contexts, more than one investigation can be requested.
                StructField("item", DiagnosticOrderItemSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Any other notes associated with this patient, specimen or order (e.g. "patient
                # hates needles").
                StructField("note", AnnotationSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema