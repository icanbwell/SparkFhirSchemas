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
class AutoMapperElasticSearchParameters_Parameter(AutoMapperDataTypeComplexBase):
    """
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there is
    no RESTful endpoint associated with it.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        name: Optional[Any] = None,
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
        resource: Optional[Any] = None,
        part: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
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
            resource=resource,
            part=part,
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
        This resource is a non-persisted resource used to pass information into and
        back from an [operation](operations.html). It has no other use, and there is
        no RESTful endpoint associated with it.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        name: The name of the parameter (reference to the operation definition).

        valueBase64Binary: If the parameter is a data type.

        valueBoolean: If the parameter is a data type.

        valueCanonical: If the parameter is a data type.

        valueCode: If the parameter is a data type.

        valueDate: If the parameter is a data type.

        valueDateTime: If the parameter is a data type.

        valueDecimal: If the parameter is a data type.

        valueId: If the parameter is a data type.

        valueInstant: If the parameter is a data type.

        valueInteger: If the parameter is a data type.

        valueMarkdown: If the parameter is a data type.

        valueOid: If the parameter is a data type.

        valuePositiveInt: If the parameter is a data type.

        valueString: If the parameter is a data type.

        valueTime: If the parameter is a data type.

        valueUnsignedInt: If the parameter is a data type.

        valueUri: If the parameter is a data type.

        valueUrl: If the parameter is a data type.

        valueUuid: If the parameter is a data type.

        valueAddress: If the parameter is a data type.

        valueAge: If the parameter is a data type.

        valueAnnotation: If the parameter is a data type.

        valueAttachment: If the parameter is a data type.

        valueCodeableConcept: If the parameter is a data type.

        valueCoding: If the parameter is a data type.

        valueContactPoint: If the parameter is a data type.

        valueCount: If the parameter is a data type.

        valueDistance: If the parameter is a data type.

        valueDuration: If the parameter is a data type.

        valueHumanName: If the parameter is a data type.

        valueIdentifier: If the parameter is a data type.

        valueMoney: If the parameter is a data type.

        valuePeriod: If the parameter is a data type.

        valueQuantity: If the parameter is a data type.

        valueRange: If the parameter is a data type.

        valueRatio: If the parameter is a data type.

        valueReference: If the parameter is a data type.

        valueSampledData: If the parameter is a data type.

        valueSignature: If the parameter is a data type.

        valueTiming: If the parameter is a data type.

        valueContactDetail: If the parameter is a data type.

        valueContributor: If the parameter is a data type.

        valueDataRequirement: If the parameter is a data type.

        valueExpression: If the parameter is a data type.

        valueParameterDefinition: If the parameter is a data type.

        valueRelatedArtifact: If the parameter is a data type.

        valueTriggerDefinition: If the parameter is a data type.

        valueUsageContext: If the parameter is a data type.

        valueDosage: If the parameter is a data type.

        valueMeta: If the parameter is a data type.

        resource: If the parameter is a whole resource.

        part: A named part of a multi-part parameter.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
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
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Parameters_Parameter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Parameters_Parameter"]
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
                # The name of the parameter (reference to the operation definition).
                StructField("name", StringType(), True),
                # If the parameter is a data type.
                StructField("valueBase64Binary", StringType(), True),
                # If the parameter is a data type.
                StructField("valueBoolean", BooleanType(), True),
                # If the parameter is a data type.
                StructField("valueCanonical", StringType(), True),
                # If the parameter is a data type.
                StructField("valueCode", StringType(), True),
                # If the parameter is a data type.
                StructField("valueDate", DateType(), True),
                # If the parameter is a data type.
                StructField("valueDateTime", TimestampType(), True),
                # If the parameter is a data type.
                StructField("valueDecimal", FloatType(), True),
                # If the parameter is a data type.
                StructField("valueId", StringType(), True),
                # If the parameter is a data type.
                StructField("valueInstant", StringType(), True),
                # If the parameter is a data type.
                StructField("valueInteger", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueMarkdown", StringType(), True),
                # If the parameter is a data type.
                StructField("valueOid", StringType(), True),
                # If the parameter is a data type.
                StructField("valuePositiveInt", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueString", StringType(), True),
                # If the parameter is a data type.
                StructField("valueTime", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUnsignedInt", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueUri", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUrl", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUuid", StringType(), True),
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a data type.
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
                # If the parameter is a whole resource.
                StructField(
                    "resource",
                    ResourceListSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A named part of a multi-part parameter.
                StructField(
                    "part",
                    ArrayType(
                        Parameters_ParameterSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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
