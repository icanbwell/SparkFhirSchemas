from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class StructureMap_Source:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.integer import integer
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
                StructField(
                    "context", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "min", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("max", StringType(), True),
                StructField("type", StringType(), True),
                StructField("defaultValueBase64Binary", StringType(), True),
                StructField("defaultValueBoolean", BooleanType(), True),
                StructField("defaultValueCanonical", StringType(), True),
                StructField("defaultValueCode", StringType(), True),
                StructField("defaultValueDate", StringType(), True),
                StructField("defaultValueDateTime", StringType(), True),
                StructField("defaultValueDecimal", IntegerType(), True),
                StructField("defaultValueId", StringType(), True),
                StructField("defaultValueInstant", StringType(), True),
                StructField("defaultValueInteger", IntegerType(), True),
                StructField("defaultValueMarkdown", StringType(), True),
                StructField("defaultValueOid", StringType(), True),
                StructField("defaultValuePositiveInt", IntegerType(), True),
                StructField("defaultValueString", StringType(), True),
                StructField("defaultValueTime", StringType(), True),
                StructField("defaultValueUnsignedInt", IntegerType(), True),
                StructField("defaultValueUri", StringType(), True),
                StructField("defaultValueUrl", StringType(), True),
                StructField("defaultValueUuid", StringType(), True),
                StructField(
                    "defaultValueAddress",
                    Address.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueAge", Age.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "defaultValueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueCoding",
                    Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueCount", Count.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "defaultValueDistance",
                    Distance.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueMoney", Money.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "defaultValuePeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "defaultValueRatio", Ratio.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "defaultValueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueTiming",
                    Timing.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueDosage",
                    Dosage.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "defaultValueMeta", Meta.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("element", StringType(), True),
                StructField("listMode", StringType(), True),
                StructField(
                    "variable", id.get_schema(recursion_depth + 1), True
                ),
                StructField("condition", StringType(), True),
                StructField("check", StringType(), True),
                StructField("logMessage", StringType(), True),
            ]
        )

        return schema
