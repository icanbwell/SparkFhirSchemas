from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.elementdefinition_slicing import ElementDefinition_Slicing
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.elementdefinition_base import ElementDefinition_Base
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.elementdefinition_type import ElementDefinition_Type
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
from spark_fhir_schemas.r4.resources.markdown import markdown
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
from spark_fhir_schemas.r4.resources.elementdefinition_example import ElementDefinition_Example
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.elementdefinition_constraint import ElementDefinition_Constraint
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.elementdefinition_binding import ElementDefinition_Binding
from spark_fhir_schemas.r4.resources.elementdefinition_mapping import ElementDefinition_Mapping


class ElementDefinition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("path", StringType(), True),
                StructField("representation",ArrayType(None.get_schema()), True),
                StructField("sliceName", StringType(), True),
                StructField("sliceIsConstraining", BooleanType(), True),
                StructField("label", StringType(), True),
                StructField("code",ArrayType(Coding.get_schema()), True),
                StructField("slicing", ElementDefinition_Slicing.get_schema(), True),
                StructField("short", StringType(), True),
                StructField("definition", markdown.get_schema(), True),
                StructField("comment", markdown.get_schema(), True),
                StructField("requirements", markdown.get_schema(), True),
                StructField("alias",ArrayType(string.get_schema()), True),
                StructField("min", unsignedInt.get_schema(), True),
                StructField("max", StringType(), True),
                StructField("base", ElementDefinition_Base.get_schema(), True),
                StructField("contentReference", uri.get_schema(), True),
                StructField("type",ArrayType(ElementDefinition_Type.get_schema()), True),
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
                StructField("meaningWhenMissing", markdown.get_schema(), True),
                StructField("orderMeaning", StringType(), True),
                StructField("fixedBase64Binary", StringType(), True),
                StructField("fixedBoolean", BooleanType(), True),
                StructField("fixedCanonical", StringType(), True),
                StructField("fixedCode", StringType(), True),
                StructField("fixedDate", StringType(), True),
                StructField("fixedDateTime", StringType(), True),
                StructField("fixedDecimal", IntegerType(), True),
                StructField("fixedId", StringType(), True),
                StructField("fixedInstant", StringType(), True),
                StructField("fixedInteger", IntegerType(), True),
                StructField("fixedMarkdown", StringType(), True),
                StructField("fixedOid", StringType(), True),
                StructField("fixedPositiveInt", IntegerType(), True),
                StructField("fixedString", StringType(), True),
                StructField("fixedTime", StringType(), True),
                StructField("fixedUnsignedInt", IntegerType(), True),
                StructField("fixedUri", StringType(), True),
                StructField("fixedUrl", StringType(), True),
                StructField("fixedUuid", StringType(), True),
                StructField("fixedAddress", Address.get_schema(), True),
                StructField("fixedAge", Age.get_schema(), True),
                StructField("fixedAnnotation", Annotation.get_schema(), True),
                StructField("fixedAttachment", Attachment.get_schema(), True),
                StructField("fixedCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("fixedCoding", Coding.get_schema(), True),
                StructField("fixedContactPoint", ContactPoint.get_schema(), True),
                StructField("fixedCount", Count.get_schema(), True),
                StructField("fixedDistance", Distance.get_schema(), True),
                StructField("fixedDuration", Duration.get_schema(), True),
                StructField("fixedHumanName", HumanName.get_schema(), True),
                StructField("fixedIdentifier", Identifier.get_schema(), True),
                StructField("fixedMoney", Money.get_schema(), True),
                StructField("fixedPeriod", Period.get_schema(), True),
                StructField("fixedQuantity", Quantity.get_schema(), True),
                StructField("fixedRange", Range.get_schema(), True),
                StructField("fixedRatio", Ratio.get_schema(), True),
                StructField("fixedReference", Reference.get_schema(), True),
                StructField("fixedSampledData", SampledData.get_schema(), True),
                StructField("fixedSignature", Signature.get_schema(), True),
                StructField("fixedTiming", Timing.get_schema(), True),
                StructField("fixedContactDetail", ContactDetail.get_schema(), True),
                StructField("fixedContributor", Contributor.get_schema(), True),
                StructField("fixedDataRequirement", DataRequirement.get_schema(), True),
                StructField("fixedExpression", Expression.get_schema(), True),
                StructField("fixedParameterDefinition", ParameterDefinition.get_schema(), True),
                StructField("fixedRelatedArtifact", RelatedArtifact.get_schema(), True),
                StructField("fixedTriggerDefinition", TriggerDefinition.get_schema(), True),
                StructField("fixedUsageContext", UsageContext.get_schema(), True),
                StructField("fixedDosage", Dosage.get_schema(), True),
                StructField("fixedMeta", Meta.get_schema(), True),
                StructField("patternBase64Binary", StringType(), True),
                StructField("patternBoolean", BooleanType(), True),
                StructField("patternCanonical", StringType(), True),
                StructField("patternCode", StringType(), True),
                StructField("patternDate", StringType(), True),
                StructField("patternDateTime", StringType(), True),
                StructField("patternDecimal", IntegerType(), True),
                StructField("patternId", StringType(), True),
                StructField("patternInstant", StringType(), True),
                StructField("patternInteger", IntegerType(), True),
                StructField("patternMarkdown", StringType(), True),
                StructField("patternOid", StringType(), True),
                StructField("patternPositiveInt", IntegerType(), True),
                StructField("patternString", StringType(), True),
                StructField("patternTime", StringType(), True),
                StructField("patternUnsignedInt", IntegerType(), True),
                StructField("patternUri", StringType(), True),
                StructField("patternUrl", StringType(), True),
                StructField("patternUuid", StringType(), True),
                StructField("patternAddress", Address.get_schema(), True),
                StructField("patternAge", Age.get_schema(), True),
                StructField("patternAnnotation", Annotation.get_schema(), True),
                StructField("patternAttachment", Attachment.get_schema(), True),
                StructField("patternCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("patternCoding", Coding.get_schema(), True),
                StructField("patternContactPoint", ContactPoint.get_schema(), True),
                StructField("patternCount", Count.get_schema(), True),
                StructField("patternDistance", Distance.get_schema(), True),
                StructField("patternDuration", Duration.get_schema(), True),
                StructField("patternHumanName", HumanName.get_schema(), True),
                StructField("patternIdentifier", Identifier.get_schema(), True),
                StructField("patternMoney", Money.get_schema(), True),
                StructField("patternPeriod", Period.get_schema(), True),
                StructField("patternQuantity", Quantity.get_schema(), True),
                StructField("patternRange", Range.get_schema(), True),
                StructField("patternRatio", Ratio.get_schema(), True),
                StructField("patternReference", Reference.get_schema(), True),
                StructField("patternSampledData", SampledData.get_schema(), True),
                StructField("patternSignature", Signature.get_schema(), True),
                StructField("patternTiming", Timing.get_schema(), True),
                StructField("patternContactDetail", ContactDetail.get_schema(), True),
                StructField("patternContributor", Contributor.get_schema(), True),
                StructField("patternDataRequirement", DataRequirement.get_schema(), True),
                StructField("patternExpression", Expression.get_schema(), True),
                StructField("patternParameterDefinition", ParameterDefinition.get_schema(), True),
                StructField("patternRelatedArtifact", RelatedArtifact.get_schema(), True),
                StructField("patternTriggerDefinition", TriggerDefinition.get_schema(), True),
                StructField("patternUsageContext", UsageContext.get_schema(), True),
                StructField("patternDosage", Dosage.get_schema(), True),
                StructField("patternMeta", Meta.get_schema(), True),
                StructField("example",ArrayType(ElementDefinition_Example.get_schema()), True),
                StructField("minValueDate", StringType(), True),
                StructField("minValueDateTime", StringType(), True),
                StructField("minValueInstant", StringType(), True),
                StructField("minValueTime", StringType(), True),
                StructField("minValueDecimal", IntegerType(), True),
                StructField("minValueInteger", IntegerType(), True),
                StructField("minValuePositiveInt", IntegerType(), True),
                StructField("minValueUnsignedInt", IntegerType(), True),
                StructField("minValueQuantity", Quantity.get_schema(), True),
                StructField("maxValueDate", StringType(), True),
                StructField("maxValueDateTime", StringType(), True),
                StructField("maxValueInstant", StringType(), True),
                StructField("maxValueTime", StringType(), True),
                StructField("maxValueDecimal", IntegerType(), True),
                StructField("maxValueInteger", IntegerType(), True),
                StructField("maxValuePositiveInt", IntegerType(), True),
                StructField("maxValueUnsignedInt", IntegerType(), True),
                StructField("maxValueQuantity", Quantity.get_schema(), True),
                StructField("maxLength", integer.get_schema(), True),
                StructField("condition",ArrayType(id.get_schema()), True),
                StructField("constraint",ArrayType(ElementDefinition_Constraint.get_schema()), True),
                StructField("mustSupport", BooleanType(), True),
                StructField("isModifier", BooleanType(), True),
                StructField("isModifierReason", StringType(), True),
                StructField("isSummary", BooleanType(), True),
                StructField("binding", ElementDefinition_Binding.get_schema(), True),
                StructField("mapping",ArrayType(ElementDefinition_Mapping.get_schema()), True),]
        )

        return schema
