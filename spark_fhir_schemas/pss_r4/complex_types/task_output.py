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
class AutoMapperElasticSearchTask_Output(AutoMapperDataTypeComplexBase):
    """
    A task to be performed.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        valueBase64Binary: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueCanonical: Optional[Any] = None,
        valueCode: Optional[Any] = None,
        valueDate: Optional[Any] = None,
        valueDateTime: Optional[Any] = None,
        valueDecimal: Optional[Any] = None,
        valueId: Optional[Any] = None,
        valueInstant: Optional[Any] = None,
        valueInteger: Optional[Any] = None,
        valueMarkdown: Optional[Any] = None,
        valueOid: Optional[Any] = None,
        valuePositiveInt: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueTime: Optional[Any] = None,
        valueUnsignedInt: Optional[Any] = None,
        valueUri: Optional[Any] = None,
        valueUrl: Optional[Any] = None,
        valueUuid: Optional[Any] = None,
        valueAddress: Optional[Any] = None,
        valueAge: Optional[Any] = None,
        valueAnnotation: Optional[Any] = None,
        valueAttachment: Optional[Any] = None,
        valueCodeableConcept: Optional[Any] = None,
        valueCoding: Optional[Any] = None,
        valueContactPoint: Optional[Any] = None,
        valueCount: Optional[Any] = None,
        valueDistance: Optional[Any] = None,
        valueDuration: Optional[Any] = None,
        valueHumanName: Optional[Any] = None,
        valueIdentifier: Optional[Any] = None,
        valueMoney: Optional[Any] = None,
        valuePeriod: Optional[Any] = None,
        valueQuantity: Optional[Any] = None,
        valueRange: Optional[Any] = None,
        valueRatio: Optional[Any] = None,
        valueReference: Optional[Any] = None,
        valueSampledData: Optional[Any] = None,
        valueSignature: Optional[Any] = None,
        valueTiming: Optional[Any] = None,
        valueContactDetail: Optional[Any] = None,
        valueContributor: Optional[Any] = None,
        valueDataRequirement: Optional[Any] = None,
        valueExpression: Optional[Any] = None,
        valueParameterDefinition: Optional[Any] = None,
        valueRelatedArtifact: Optional[Any] = None,
        valueTriggerDefinition: Optional[Any] = None,
        valueUsageContext: Optional[Any] = None,
        valueDosage: Optional[Any] = None,
        valueMeta: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            valueBase64Binary=valueBase64Binary,
            valueBoolean=valueBoolean,
            valueCanonical=valueCanonical,
            valueCode=valueCode,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueDecimal=valueDecimal,
            valueId=valueId,
            valueInstant=valueInstant,
            valueInteger=valueInteger,
            valueMarkdown=valueMarkdown,
            valueOid=valueOid,
            valuePositiveInt=valuePositiveInt,
            valueString=valueString,
            valueTime=valueTime,
            valueUnsignedInt=valueUnsignedInt,
            valueUri=valueUri,
            valueUrl=valueUrl,
            valueUuid=valueUuid,
            valueAddress=valueAddress,
            valueAge=valueAge,
            valueAnnotation=valueAnnotation,
            valueAttachment=valueAttachment,
            valueCodeableConcept=valueCodeableConcept,
            valueCoding=valueCoding,
            valueContactPoint=valueContactPoint,
            valueCount=valueCount,
            valueDistance=valueDistance,
            valueDuration=valueDuration,
            valueHumanName=valueHumanName,
            valueIdentifier=valueIdentifier,
            valueMoney=valueMoney,
            valuePeriod=valuePeriod,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueRatio=valueRatio,
            valueReference=valueReference,
            valueSampledData=valueSampledData,
            valueSignature=valueSignature,
            valueTiming=valueTiming,
            valueContactDetail=valueContactDetail,
            valueContributor=valueContributor,
            valueDataRequirement=valueDataRequirement,
            valueExpression=valueExpression,
            valueParameterDefinition=valueParameterDefinition,
            valueRelatedArtifact=valueRelatedArtifact,
            valueTriggerDefinition=valueTriggerDefinition,
            valueUsageContext=valueUsageContext,
            valueDosage=valueDosage,
            valueMeta=valueMeta,
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
        A task to be performed.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The name of the Output parameter.

        valueBase64Binary: The value of the Output parameter as a basic type.

        valueBoolean: The value of the Output parameter as a basic type.

        valueCanonical: The value of the Output parameter as a basic type.

        valueCode: The value of the Output parameter as a basic type.

        valueDate: The value of the Output parameter as a basic type.

        valueDateTime: The value of the Output parameter as a basic type.

        valueDecimal: The value of the Output parameter as a basic type.

        valueId: The value of the Output parameter as a basic type.

        valueInstant: The value of the Output parameter as a basic type.

        valueInteger: The value of the Output parameter as a basic type.

        valueMarkdown: The value of the Output parameter as a basic type.

        valueOid: The value of the Output parameter as a basic type.

        valuePositiveInt: The value of the Output parameter as a basic type.

        valueString: The value of the Output parameter as a basic type.

        valueTime: The value of the Output parameter as a basic type.

        valueUnsignedInt: The value of the Output parameter as a basic type.

        valueUri: The value of the Output parameter as a basic type.

        valueUrl: The value of the Output parameter as a basic type.

        valueUuid: The value of the Output parameter as a basic type.

        valueAddress: The value of the Output parameter as a basic type.

        valueAge: The value of the Output parameter as a basic type.

        valueAnnotation: The value of the Output parameter as a basic type.

        valueAttachment: The value of the Output parameter as a basic type.

        valueCodeableConcept: The value of the Output parameter as a basic type.

        valueCoding: The value of the Output parameter as a basic type.

        valueContactPoint: The value of the Output parameter as a basic type.

        valueCount: The value of the Output parameter as a basic type.

        valueDistance: The value of the Output parameter as a basic type.

        valueDuration: The value of the Output parameter as a basic type.

        valueHumanName: The value of the Output parameter as a basic type.

        valueIdentifier: The value of the Output parameter as a basic type.

        valueMoney: The value of the Output parameter as a basic type.

        valuePeriod: The value of the Output parameter as a basic type.

        valueQuantity: The value of the Output parameter as a basic type.

        valueRange: The value of the Output parameter as a basic type.

        valueRatio: The value of the Output parameter as a basic type.

        valueReference: The value of the Output parameter as a basic type.

        valueSampledData: The value of the Output parameter as a basic type.

        valueSignature: The value of the Output parameter as a basic type.

        valueTiming: The value of the Output parameter as a basic type.

        valueContactDetail: The value of the Output parameter as a basic type.

        valueContributor: The value of the Output parameter as a basic type.

        valueDataRequirement: The value of the Output parameter as a basic type.

        valueExpression: The value of the Output parameter as a basic type.

        valueParameterDefinition: The value of the Output parameter as a basic type.

        valueRelatedArtifact: The value of the Output parameter as a basic type.

        valueTriggerDefinition: The value of the Output parameter as a basic type.

        valueUsageContext: The value of the Output parameter as a basic type.

        valueDosage: The value of the Output parameter as a basic type.

        valueMeta: The value of the Output parameter as a basic type.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
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
            and nesting_list.count("Task_Output") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Task_Output"]
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
                # The name of the Output parameter.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField("valueBase64Binary", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueBoolean", BooleanType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueCanonical", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueCode", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueDate", DateType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueDateTime", TimestampType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueDecimal", FloatType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueId", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueInstant", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueInteger", IntegerType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueMarkdown", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueOid", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valuePositiveInt", IntegerType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueString", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueTime", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueUnsignedInt", IntegerType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueUri", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueUrl", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField("valueUuid", StringType(), True),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueAddress",
                    AddressSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueAnnotation",
                    AnnotationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueContactPoint",
                    ContactPointSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueCount",
                    CountSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueDistance",
                    DistanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueHumanName",
                    HumanNameSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueMoney",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valuePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueSignature",
                    SignatureSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueContactDetail",
                    ContactDetailSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueContributor",
                    ContributorSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifactSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueUsageContext",
                    UsageContextSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueDosage",
                    DosageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The value of the Output parameter as a basic type.
                StructField(
                    "valueMeta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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
        return schema
