from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
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


class Extension:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("url", uri.get_schema(), True),
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
                StructField("valueMeta", Meta.get_schema(), True),
            ]
        )

        return schema
