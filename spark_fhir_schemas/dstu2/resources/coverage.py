from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CoverageSchema:
    """
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    If the element is present, it must have either a @value, an @id, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
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
        issuer: The program or plan underwriter or payor.
        bin: Business Identification Number (BIN number) used to identify the routing  of
    eclaims if the insurer themselves don't have a BIN number for all of their
    business.
        period: Time period during which the coverage is in force. A missing start date
    indicates the start date isn't known, a missing end date means the coverage is
    continuing to be in force.
        type: The type of coverage: social program, medical plan, accident coverage (workers
    compensation, auto), group health.
        subscriberId: The id issued to the subscriber.
        identifier: The main (and possibly only) identifier for the coverage - often referred to
    as a Member Id, Subscriber Id, Certificate number or Personal Health Number or
    Case ID.
        group: Identifies a style or collective of coverage issues by the underwriter, for
    example may be used to identify a class of coverage or employer group. May
    also be referred to as a Policy or Group ID.
        plan: Identifies a style or collective of coverage issues by the underwriter, for
    example may be used to identify a class of coverage or employer group. May
    also be referred to as a Policy or Group ID.
        subPlan: Identifies a sub-style or sub-collective of coverage issues by the
    underwriter, for example may be used to identify a specific employer group
    within a class of employers. May be referred to as a Section or Division ID.
        dependent: A unique identifier for a dependent under the coverage.
        sequence: An optional counter for a particular instance of the identified coverage which
    increments upon each renewal.
        subscriber: The party who 'owns' the insurance contractual relationship to the policy or
    to whom the benefit of the policy is due.
        network: The identifier for a community of providers.
        contract: The policy(s) which constitute this insurance coverage.
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
            # issuer
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # bin
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # period
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
            # type
        from spark_fhir_schemas.dstu2.complex_types.coding import CodingSchema
            # subscriberId
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # identifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # group
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # plan
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # subPlan
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # dependent
        from spark_fhir_schemas.dstu2.simple_types.positiveint import positiveIntSchema
            # sequence
        from spark_fhir_schemas.dstu2.simple_types.positiveint import positiveIntSchema
            # subscriber
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # network
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # contract
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        if (max_recursion_limit and nesting_list.count("Coverage") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["Coverage"]
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
                # The program or plan underwriter or payor.
                StructField("issuer", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Business Identification Number (BIN number) used to identify the routing  of
                # eclaims if the insurer themselves don't have a BIN number for all of their
                # business.
                StructField("bin", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Time period during which the coverage is in force. A missing start date
                # indicates the start date isn't known, a missing end date means the coverage is
                # continuing to be in force.
                StructField("period", PeriodSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The type of coverage: social program, medical plan, accident coverage (workers
                # compensation, auto), group health.
                StructField("type", CodingSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The id issued to the subscriber.
                StructField("subscriberId", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The main (and possibly only) identifier for the coverage - often referred to
                # as a Member Id, Subscriber Id, Certificate number or Personal Health Number or
                # Case ID.
                StructField("identifier", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifies a style or collective of coverage issues by the underwriter, for
                # example may be used to identify a class of coverage or employer group. May
                # also be referred to as a Policy or Group ID.
                StructField("group", StringType(), True),
                # Identifies a style or collective of coverage issues by the underwriter, for
                # example may be used to identify a class of coverage or employer group. May
                # also be referred to as a Policy or Group ID.
                StructField("plan", StringType(), True),
                # Identifies a sub-style or sub-collective of coverage issues by the
                # underwriter, for example may be used to identify a specific employer group
                # within a class of employers. May be referred to as a Section or Division ID.
                StructField("subPlan", StringType(), True),
                # A unique identifier for a dependent under the coverage.
                StructField("dependent", positiveIntSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # An optional counter for a particular instance of the identified coverage which
                # increments upon each renewal.
                StructField("sequence", positiveIntSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The party who 'owns' the insurance contractual relationship to the policy or
                # to whom the benefit of the policy is due.
                StructField("subscriber", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The identifier for a community of providers.
                StructField("network", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The policy(s) which constitute this insurance coverage.
                StructField("contract", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema