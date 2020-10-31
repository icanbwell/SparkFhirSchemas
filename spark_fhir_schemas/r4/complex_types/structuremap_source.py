from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class StructureMap_Source:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.integer import integer
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
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Type or variable this rule applies to.
                StructField(
                    "context", id.get_schema(recursion_depth + 1), True
                ),
                # Specified minimum cardinality for the element. This is optional; if present,
                # it acts an implicit check on the input content.
                StructField(
                    "min", integer.get_schema(recursion_depth + 1), True
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
                StructField("defaultValueDate", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDateTime", StringType(), True),
                # A value to use if there is no existing value in the source object.
                StructField("defaultValueDecimal", IntegerType(), True),
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
                    Address.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAge", Age.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCoding",
                    Coding.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueCount", Count.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDistance",
                    Distance.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMoney", Money.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValuePeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRatio", Ratio.get_schema(recursion_depth + 1),
                    True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTiming",
                    Timing.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueDosage",
                    Dosage.get_schema(recursion_depth + 1), True
                ),
                # A value to use if there is no existing value in the source object.
                StructField(
                    "defaultValueMeta", Meta.get_schema(recursion_depth + 1),
                    True
                ),
                # Optional field for this source.
                StructField("element", StringType(), True),
                # How to handle the list mode for this element.
                StructField("listMode", StringType(), True),
                # Named context for field, if a field is specified.
                StructField(
                    "variable", id.get_schema(recursion_depth + 1), True
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
        return schema
