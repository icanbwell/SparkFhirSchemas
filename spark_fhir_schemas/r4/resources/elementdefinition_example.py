from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.address import Address
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.contactpoint import ContactPoint
from spark_fhir_schemas.r4.resources.count import Count
from spark_fhir_schemas.r4.resources.distance import Distance
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.humanname import HumanName
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.sampleddata import SampledData
from spark_fhir_schemas.r4.resources.signature import Signature
from spark_fhir_schemas.r4.resources.timing import Timing
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.contributor import Contributor
from spark_fhir_schemas.r4.resources.datarequirement import DataRequirement
from spark_fhir_schemas.r4.resources.expression import Expression
from spark_fhir_schemas.r4.resources.parameterdefinition import ParameterDefinition
from spark_fhir_schemas.r4.resources.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.resources.triggerdefinition import TriggerDefinition
from spark_fhir_schemas.r4.resources.usagecontext import UsageContext
from spark_fhir_schemas.r4.resources.dosage import Dosage
from spark_fhir_schemas.r4.resources.meta import Meta


class ElementDefinition_Example:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("label", StringType(), True),
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
                StructField("valueAddress", Address.get_schema(), True),
                StructField("valueAge", Age.get_schema(), True),
                StructField("valueAnnotation", Annotation.get_schema(), True),
                StructField("valueAttachment", Attachment.get_schema(), True),
                StructField("valueCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("valueCoding", Coding.get_schema(), True),
                StructField("valueContactPoint", ContactPoint.get_schema(), True),
                StructField("valueCount", Count.get_schema(), True),
                StructField("valueDistance", Distance.get_schema(), True),
                StructField("valueDuration", Duration.get_schema(), True),
                StructField("valueHumanName", HumanName.get_schema(), True),
                StructField("valueIdentifier", Identifier.get_schema(), True),
                StructField("valueMoney", Money.get_schema(), True),
                StructField("valuePeriod", Period.get_schema(), True),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueRange", Range.get_schema(), True),
                StructField("valueRatio", Ratio.get_schema(), True),
                StructField("valueReference", Reference.get_schema(), True),
                StructField("valueSampledData", SampledData.get_schema(), True),
                StructField("valueSignature", Signature.get_schema(), True),
                StructField("valueTiming", Timing.get_schema(), True),
                StructField("valueContactDetail", ContactDetail.get_schema(), True),
                StructField("valueContributor", Contributor.get_schema(), True),
                StructField("valueDataRequirement", DataRequirement.get_schema(), True),
                StructField("valueExpression", Expression.get_schema(), True),
                StructField("valueParameterDefinition", ParameterDefinition.get_schema(), True),
                StructField("valueRelatedArtifact", RelatedArtifact.get_schema(), True),
                StructField("valueTriggerDefinition", TriggerDefinition.get_schema(), True),
                StructField("valueUsageContext", UsageContext.get_schema(), True),
                StructField("valueDosage", Dosage.get_schema(), True),
                StructField("valueMeta", Meta.get_schema(), True),]
        )

        return schema
