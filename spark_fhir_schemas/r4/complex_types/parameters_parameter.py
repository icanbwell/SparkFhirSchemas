from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Parameters_Parameter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.count import Count
        from spark_fhir_schemas.r4.complex_types.distance import Distance
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.humanname import HumanName
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.sampleddata import SampledData
        from spark_fhir_schemas.r4.complex_types.signature import Signature
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.contributor import Contributor
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.expression import Expression
        from spark_fhir_schemas.r4.complex_types.parameterdefinition import ParameterDefinition
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinition
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("name", StringType(), True),
                StructField("valueBase64Binary", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueCanonical", StringType(), True),
                StructField("valueCode", StringType(), True),
                StructField("valueDate", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valueDecimal", IntegerType(), True),
                StructField("valueId", StringType(), True),
                StructField("valueInstant", StringType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueMarkdown", StringType(), True),
                StructField("valueOid", StringType(), True),
                StructField("valuePositiveInt", IntegerType(), True),
                StructField("valueString", StringType(), True),
                StructField("valueTime", StringType(), True),
                StructField("valueUnsignedInt", IntegerType(), True),
                StructField("valueUri", StringType(), True),
                StructField("valueUrl", StringType(), True),
                StructField("valueUuid", StringType(), True),
                StructField(
                    "valueAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueCount", Count.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueMoney", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueMeta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource", ResourceList.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "part",
                    ArrayType(
                        Parameters_Parameter.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
