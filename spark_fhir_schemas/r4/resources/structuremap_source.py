from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.string import string
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
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string


class StructureMap_Source:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("context", id.get_schema(), True),
                StructField("min", integer.get_schema(), True),
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
                StructField("defaultValueAddress", Address.get_schema(), True),
                StructField("defaultValueAge", Age.get_schema(), True),
                StructField("defaultValueAnnotation", Annotation.get_schema(), True),
                StructField("defaultValueAttachment", Attachment.get_schema(), True),
                StructField("defaultValueCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("defaultValueCoding", Coding.get_schema(), True),
                StructField("defaultValueContactPoint", ContactPoint.get_schema(), True),
                StructField("defaultValueCount", Count.get_schema(), True),
                StructField("defaultValueDistance", Distance.get_schema(), True),
                StructField("defaultValueDuration", Duration.get_schema(), True),
                StructField("defaultValueHumanName", HumanName.get_schema(), True),
                StructField("defaultValueIdentifier", Identifier.get_schema(), True),
                StructField("defaultValueMoney", Money.get_schema(), True),
                StructField("defaultValuePeriod", Period.get_schema(), True),
                StructField("defaultValueQuantity", Quantity.get_schema(), True),
                StructField("defaultValueRange", Range.get_schema(), True),
                StructField("defaultValueRatio", Ratio.get_schema(), True),
                StructField("defaultValueReference", Reference.get_schema(), True),
                StructField("defaultValueSampledData", SampledData.get_schema(), True),
                StructField("defaultValueSignature", Signature.get_schema(), True),
                StructField("defaultValueTiming", Timing.get_schema(), True),
                StructField("defaultValueContactDetail", ContactDetail.get_schema(), True),
                StructField("defaultValueContributor", Contributor.get_schema(), True),
                StructField("defaultValueDataRequirement", DataRequirement.get_schema(), True),
                StructField("defaultValueExpression", Expression.get_schema(), True),
                StructField("defaultValueParameterDefinition", ParameterDefinition.get_schema(), True),
                StructField("defaultValueRelatedArtifact", RelatedArtifact.get_schema(), True),
                StructField("defaultValueTriggerDefinition", TriggerDefinition.get_schema(), True),
                StructField("defaultValueUsageContext", UsageContext.get_schema(), True),
                StructField("defaultValueDosage", Dosage.get_schema(), True),
                StructField("defaultValueMeta", Meta.get_schema(), True),
                StructField("element", StringType(), True),
                StructField("listMode", StringType(), True),
                StructField("variable", id.get_schema(), True),
                StructField("condition", StringType(), True),
                StructField("check", StringType(), True),
                StructField("logMessage", StringType(), True),]
        )

        return schema
