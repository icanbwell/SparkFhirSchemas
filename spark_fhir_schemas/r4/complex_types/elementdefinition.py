from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ElementDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.elementdefinition_slicing import ElementDefinition_Slicing
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.elementdefinition_base import ElementDefinition_Base
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.elementdefinition_type import ElementDefinition_Type
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
        from spark_fhir_schemas.r4.complex_types.elementdefinition_example import ElementDefinition_Example
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.elementdefinition_constraint import ElementDefinition_Constraint
        from spark_fhir_schemas.r4.complex_types.elementdefinition_binding import ElementDefinition_Binding
        from spark_fhir_schemas.r4.complex_types.elementdefinition_mapping import ElementDefinition_Mapping
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("path", StringType(), True),
                StructField("sliceName", StringType(), True),
                StructField("sliceIsConstraining", BooleanType(), True),
                StructField("label", StringType(), True),
                StructField(
                    "code", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "slicing",
                    ElementDefinition_Slicing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("short", StringType(), True),
                StructField(
                    "definition", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "comment", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "requirements", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("alias", ArrayType(StringType()), True),
                StructField(
                    "min", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField("max", StringType(), True),
                StructField(
                    "base",
                    ElementDefinition_Base.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "contentReference", uri.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "type",
                    ArrayType(
                        ElementDefinition_Type.get_schema(recursion_depth + 1)
                    ), True
                ),
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
                StructField(
                    "meaningWhenMissing",
                    markdown.get_schema(recursion_depth + 1), True
                ),
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
                StructField(
                    "fixedAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "fixedAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedCount", Count.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "fixedDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "fixedHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedMoney", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "fixedRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixedMeta", Meta.get_schema(recursion_depth + 1), True
                ),
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
                StructField(
                    "patternAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "patternAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternCoding", Coding.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "patternContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternCount", Count.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternDistance",
                    Distance.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternMoney", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "patternQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "patternContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patternDosage", Dosage.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "patternMeta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "example",
                    ArrayType(
                        ElementDefinition_Example.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("minValueDate", StringType(), True),
                StructField("minValueDateTime", StringType(), True),
                StructField("minValueInstant", StringType(), True),
                StructField("minValueTime", StringType(), True),
                StructField("minValueDecimal", IntegerType(), True),
                StructField("minValueInteger", IntegerType(), True),
                StructField("minValuePositiveInt", IntegerType(), True),
                StructField("minValueUnsignedInt", IntegerType(), True),
                StructField(
                    "minValueQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("maxValueDate", StringType(), True),
                StructField("maxValueDateTime", StringType(), True),
                StructField("maxValueInstant", StringType(), True),
                StructField("maxValueTime", StringType(), True),
                StructField("maxValueDecimal", IntegerType(), True),
                StructField("maxValueInteger", IntegerType(), True),
                StructField("maxValuePositiveInt", IntegerType(), True),
                StructField("maxValueUnsignedInt", IntegerType(), True),
                StructField(
                    "maxValueQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "maxLength", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "condition", ArrayType(id.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "constraint",
                    ArrayType(
                        ElementDefinition_Constraint.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("mustSupport", BooleanType(), True),
                StructField("isModifier", BooleanType(), True),
                StructField("isModifierReason", StringType(), True),
                StructField("isSummary", BooleanType(), True),
                StructField(
                    "binding",
                    ElementDefinition_Binding.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "mapping",
                    ArrayType(
                        ElementDefinition_Mapping.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
