from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

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

# noinspection PyPep8Naming
class AutoMapperElasticSearchStructureMap_Source(AutoMapperDataTypeComplexBase):
    """
    A Map of relationships between 2 structures that can be used to transform
    data.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        context: Optional[Any] = None,
        min_: Optional[Any] = None,
        max_: Optional[Any] = None,
        type_: Optional[Any] = None,
        defaultValueBase64Binary: Optional[Any] = None,
        defaultValueBoolean: Optional[Any] = None,
        defaultValueCanonical: Optional[Any] = None,
        defaultValueCode: Optional[Any] = None,
        defaultValueDate: Optional[Any] = None,
        defaultValueDateTime: Optional[Any] = None,
        defaultValueDecimal: Optional[Any] = None,
        defaultValueId: Optional[Any] = None,
        defaultValueInstant: Optional[Any] = None,
        defaultValueInteger: Optional[Any] = None,
        defaultValueMarkdown: Optional[Any] = None,
        defaultValueOid: Optional[Any] = None,
        defaultValuePositiveInt: Optional[Any] = None,
        defaultValueString: Optional[Any] = None,
        defaultValueTime: Optional[Any] = None,
        defaultValueUnsignedInt: Optional[Any] = None,
        defaultValueUri: Optional[Any] = None,
        defaultValueUrl: Optional[Any] = None,
        defaultValueUuid: Optional[Any] = None,
        defaultValueAddress: Optional[Any] = None,
        defaultValueAge: Optional[Any] = None,
        defaultValueAnnotation: Optional[Any] = None,
        defaultValueAttachment: Optional[Any] = None,
        defaultValueCodeableConcept: Optional[Any] = None,
        defaultValueCoding: Optional[Any] = None,
        defaultValueContactPoint: Optional[Any] = None,
        defaultValueCount: Optional[Any] = None,
        defaultValueDistance: Optional[Any] = None,
        defaultValueDuration: Optional[Any] = None,
        defaultValueHumanName: Optional[Any] = None,
        defaultValueIdentifier: Optional[Any] = None,
        defaultValueMoney: Optional[Any] = None,
        defaultValuePeriod: Optional[Any] = None,
        defaultValueQuantity: Optional[Any] = None,
        defaultValueRange: Optional[Any] = None,
        defaultValueRatio: Optional[Any] = None,
        defaultValueReference: Optional[Any] = None,
        defaultValueSampledData: Optional[Any] = None,
        defaultValueSignature: Optional[Any] = None,
        defaultValueTiming: Optional[Any] = None,
        defaultValueContactDetail: Optional[Any] = None,
        defaultValueContributor: Optional[Any] = None,
        defaultValueDataRequirement: Optional[Any] = None,
        defaultValueExpression: Optional[Any] = None,
        defaultValueParameterDefinition: Optional[Any] = None,
        defaultValueRelatedArtifact: Optional[Any] = None,
        defaultValueTriggerDefinition: Optional[Any] = None,
        defaultValueUsageContext: Optional[Any] = None,
        defaultValueDosage: Optional[Any] = None,
        defaultValueMeta: Optional[Any] = None,
        element: Optional[Any] = None,
        listMode: Optional[Any] = None,
        variable: Optional[Any] = None,
        condition: Optional[Any] = None,
        check: Optional[Any] = None,
        logMessage: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            context=context,
            min_=min_,
            max_=max_,
            type_=type_,
            defaultValueBase64Binary=defaultValueBase64Binary,
            defaultValueBoolean=defaultValueBoolean,
            defaultValueCanonical=defaultValueCanonical,
            defaultValueCode=defaultValueCode,
            defaultValueDate=defaultValueDate,
            defaultValueDateTime=defaultValueDateTime,
            defaultValueDecimal=defaultValueDecimal,
            defaultValueId=defaultValueId,
            defaultValueInstant=defaultValueInstant,
            defaultValueInteger=defaultValueInteger,
            defaultValueMarkdown=defaultValueMarkdown,
            defaultValueOid=defaultValueOid,
            defaultValuePositiveInt=defaultValuePositiveInt,
            defaultValueString=defaultValueString,
            defaultValueTime=defaultValueTime,
            defaultValueUnsignedInt=defaultValueUnsignedInt,
            defaultValueUri=defaultValueUri,
            defaultValueUrl=defaultValueUrl,
            defaultValueUuid=defaultValueUuid,
            defaultValueAddress=defaultValueAddress,
            defaultValueAge=defaultValueAge,
            defaultValueAnnotation=defaultValueAnnotation,
            defaultValueAttachment=defaultValueAttachment,
            defaultValueCodeableConcept=defaultValueCodeableConcept,
            defaultValueCoding=defaultValueCoding,
            defaultValueContactPoint=defaultValueContactPoint,
            defaultValueCount=defaultValueCount,
            defaultValueDistance=defaultValueDistance,
            defaultValueDuration=defaultValueDuration,
            defaultValueHumanName=defaultValueHumanName,
            defaultValueIdentifier=defaultValueIdentifier,
            defaultValueMoney=defaultValueMoney,
            defaultValuePeriod=defaultValuePeriod,
            defaultValueQuantity=defaultValueQuantity,
            defaultValueRange=defaultValueRange,
            defaultValueRatio=defaultValueRatio,
            defaultValueReference=defaultValueReference,
            defaultValueSampledData=defaultValueSampledData,
            defaultValueSignature=defaultValueSignature,
            defaultValueTiming=defaultValueTiming,
            defaultValueContactDetail=defaultValueContactDetail,
            defaultValueContributor=defaultValueContributor,
            defaultValueDataRequirement=defaultValueDataRequirement,
            defaultValueExpression=defaultValueExpression,
            defaultValueParameterDefinition=defaultValueParameterDefinition,
            defaultValueRelatedArtifact=defaultValueRelatedArtifact,
            defaultValueTriggerDefinition=defaultValueTriggerDefinition,
            defaultValueUsageContext=defaultValueUsageContext,
            defaultValueDosage=defaultValueDosage,
            defaultValueMeta=defaultValueMeta,
            element=element,
            listMode=listMode,
            variable=variable,
            condition=condition,
            check=check,
            logMessage=logMessage,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        A Map of relationships between 2 structures that can be used to transform
        data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        context: Type or variable this rule applies to.

        min: Specified minimum cardinality for the element. This is optional; if present,
            it acts an implicit check on the input content.

        max: Specified maximum cardinality for the element - a number or a "*". This is
            optional; if present, it acts an implicit check on the input content (* just
            serves as documentation; it's the default value).

        type: Specified type for the element. This works as a condition on the mapping - use
            for polymorphic elements.

        defaultValueBase64Binary: A value to use if there is no existing value in the source object.

        defaultValueBoolean: A value to use if there is no existing value in the source object.

        defaultValueCanonical: A value to use if there is no existing value in the source object.

        defaultValueCode: A value to use if there is no existing value in the source object.

        defaultValueDate: A value to use if there is no existing value in the source object.

        defaultValueDateTime: A value to use if there is no existing value in the source object.

        defaultValueDecimal: A value to use if there is no existing value in the source object.

        defaultValueId: A value to use if there is no existing value in the source object.

        defaultValueInstant: A value to use if there is no existing value in the source object.

        defaultValueInteger: A value to use if there is no existing value in the source object.

        defaultValueMarkdown: A value to use if there is no existing value in the source object.

        defaultValueOid: A value to use if there is no existing value in the source object.

        defaultValuePositiveInt: A value to use if there is no existing value in the source object.

        defaultValueString: A value to use if there is no existing value in the source object.

        defaultValueTime: A value to use if there is no existing value in the source object.

        defaultValueUnsignedInt: A value to use if there is no existing value in the source object.

        defaultValueUri: A value to use if there is no existing value in the source object.

        defaultValueUrl: A value to use if there is no existing value in the source object.

        defaultValueUuid: A value to use if there is no existing value in the source object.

        defaultValueAddress: A value to use if there is no existing value in the source object.

        defaultValueAge: A value to use if there is no existing value in the source object.

        defaultValueAnnotation: A value to use if there is no existing value in the source object.

        defaultValueAttachment: A value to use if there is no existing value in the source object.

        defaultValueCodeableConcept: A value to use if there is no existing value in the source object.

        defaultValueCoding: A value to use if there is no existing value in the source object.

        defaultValueContactPoint: A value to use if there is no existing value in the source object.

        defaultValueCount: A value to use if there is no existing value in the source object.

        defaultValueDistance: A value to use if there is no existing value in the source object.

        defaultValueDuration: A value to use if there is no existing value in the source object.

        defaultValueHumanName: A value to use if there is no existing value in the source object.

        defaultValueIdentifier: A value to use if there is no existing value in the source object.

        defaultValueMoney: A value to use if there is no existing value in the source object.

        defaultValuePeriod: A value to use if there is no existing value in the source object.

        defaultValueQuantity: A value to use if there is no existing value in the source object.

        defaultValueRange: A value to use if there is no existing value in the source object.

        defaultValueRatio: A value to use if there is no existing value in the source object.

        defaultValueReference: A value to use if there is no existing value in the source object.

        defaultValueSampledData: A value to use if there is no existing value in the source object.

        defaultValueSignature: A value to use if there is no existing value in the source object.

        defaultValueTiming: A value to use if there is no existing value in the source object.

        defaultValueContactDetail: A value to use if there is no existing value in the source object.

        defaultValueContributor: A value to use if there is no existing value in the source object.

        defaultValueDataRequirement: A value to use if there is no existing value in the source object.

        defaultValueExpression: A value to use if there is no existing value in the source object.

        defaultValueParameterDefinition: A value to use if there is no existing value in the source object.

        defaultValueRelatedArtifact: A value to use if there is no existing value in the source object.

        defaultValueTriggerDefinition: A value to use if there is no existing value in the source object.

        defaultValueUsageContext: A value to use if there is no existing value in the source object.

        defaultValueDosage: A value to use if there is no existing value in the source object.

        defaultValueMeta: A value to use if there is no existing value in the source object.

        element: Optional field for this source.

        listMode: How to handle the list mode for this element.

        variable: Named context for field, if a field is specified.

        condition: FHIRPath expression  - must be true or the rule does not apply.

        check: FHIRPath expression  - must be true or the mapping engine throws an error
            instead of completing.

        logMessage: A FHIRPath expression which specifies a message to put in the transform log
            when content matching the source rule is found.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.address import (
            AutoMapperElasticSearchAddress as AddressSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactpoint import (
            AutoMapperElasticSearchContactPoint as ContactPointSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.count import (
            AutoMapperElasticSearchCount as CountSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.distance import (
            AutoMapperElasticSearchDistance as DistanceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.humanname import (
            AutoMapperElasticSearchHumanName as HumanNameSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.money import (
            AutoMapperElasticSearchMoney as MoneySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.sampleddata import (
            AutoMapperElasticSearchSampledData as SampledDataSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.signature import (
            AutoMapperElasticSearchSignature as SignatureSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactdetail import (
            AutoMapperElasticSearchContactDetail as ContactDetailSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contributor import (
            AutoMapperElasticSearchContributor as ContributorSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.expression import (
            AutoMapperElasticSearchExpression as ExpressionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.parameterdefinition import (
            AutoMapperElasticSearchParameterDefinition as ParameterDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.triggerdefinition import (
            AutoMapperElasticSearchTriggerDefinition as TriggerDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.usagecontext import (
            AutoMapperElasticSearchUsageContext as UsageContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage import (
            AutoMapperElasticSearchDosage as DosageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("StructureMap_Source") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureMap_Source"]
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
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Type or variable this rule applies to.
                StructField(
                    "context",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specified minimum cardinality for the element. This is optional; if present,
                # it acts an implicit check on the input content.
                StructField(
                    "min",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specified maximum cardinality for the element - a number or a "*". This is
                # optional; if present, it acts an implicit check on the input content (* just
                # serves as documentation; it's the default value).
                StructField("max", StringType(), True),
                # Specified type for the element. This works as a condition on the mapping - use
                # for polymorphic elements.
                StructField("type", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueBase64Binary", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueBoolean", BooleanType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueCanonical", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueCode", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDate", DateType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDateTime", TimestampType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDecimal", FloatType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueId", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueInstant", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueInteger", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueMarkdown", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueOid", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValuePositiveInt", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueString", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueTime", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUnsignedInt", IntegerType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUri", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUrl", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueUuid", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAddress",
                    AddressSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAnnotation",
                    AnnotationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactPoint",
                    ContactPointSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDistance",
                    DistanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueHumanName",
                    HumanNameSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValuePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSignature",
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactDetail",
                    ContactDetailSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContributor",
                    ContributorSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueParameterDefinition",
                    ParameterDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRelatedArtifact",
                    RelatedArtifactSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTriggerDefinition",
                    TriggerDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueUsageContext",
                    UsageContextSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDosage",
                    DosageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMeta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Optional field for this source.
                StructField("element", StringType(), True),
                # How to handle the list mode for this element.
                StructField("listMode", StringType(), True),
                # Named context for field, if a field is specified.
                StructField(
                    "variable",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # FHIRPath expression  - must be true or the rule does not apply.
                StructField("condition", StringType(), True),
                # FHIRPath expression  - must be true or the mapping engine throws an error
                # instead of completing.
                StructField("check", StringType(), True),
                # A FHIRPath expression which specifies a message to put in the transform log
                # when content matching the source rule is found.
                StructField("logMessage", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
