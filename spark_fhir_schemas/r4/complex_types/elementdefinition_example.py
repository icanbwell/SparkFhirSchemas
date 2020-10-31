from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ElementDefinition_Example:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Captures constraints on each element within the resource, profile, or
        extension.


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

        label: Describes the purpose of this example amoung the set of examples.

        valueBase64Binary: The actual value for the element, which must be one of the types allowed for
            this element.

        valueBoolean: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCanonical: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCode: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDate: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDateTime: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDecimal: The actual value for the element, which must be one of the types allowed for
            this element.

        valueId: The actual value for the element, which must be one of the types allowed for
            this element.

        valueInstant: The actual value for the element, which must be one of the types allowed for
            this element.

        valueInteger: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMarkdown: The actual value for the element, which must be one of the types allowed for
            this element.

        valueOid: The actual value for the element, which must be one of the types allowed for
            this element.

        valuePositiveInt: The actual value for the element, which must be one of the types allowed for
            this element.

        valueString: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTime: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUnsignedInt: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUri: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUrl: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUuid: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAddress: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAge: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAnnotation: The actual value for the element, which must be one of the types allowed for
            this element.

        valueAttachment: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCodeableConcept: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCoding: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContactPoint: The actual value for the element, which must be one of the types allowed for
            this element.

        valueCount: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDistance: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDuration: The actual value for the element, which must be one of the types allowed for
            this element.

        valueHumanName: The actual value for the element, which must be one of the types allowed for
            this element.

        valueIdentifier: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMoney: The actual value for the element, which must be one of the types allowed for
            this element.

        valuePeriod: The actual value for the element, which must be one of the types allowed for
            this element.

        valueQuantity: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRange: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRatio: The actual value for the element, which must be one of the types allowed for
            this element.

        valueReference: The actual value for the element, which must be one of the types allowed for
            this element.

        valueSampledData: The actual value for the element, which must be one of the types allowed for
            this element.

        valueSignature: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTiming: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContactDetail: The actual value for the element, which must be one of the types allowed for
            this element.

        valueContributor: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDataRequirement: The actual value for the element, which must be one of the types allowed for
            this element.

        valueExpression: The actual value for the element, which must be one of the types allowed for
            this element.

        valueParameterDefinition: The actual value for the element, which must be one of the types allowed for
            this element.

        valueRelatedArtifact: The actual value for the element, which must be one of the types allowed for
            this element.

        valueTriggerDefinition: The actual value for the element, which must be one of the types allowed for
            this element.

        valueUsageContext: The actual value for the element, which must be one of the types allowed for
            this element.

        valueDosage: The actual value for the element, which must be one of the types allowed for
            this element.

        valueMeta: The actual value for the element, which must be one of the types allowed for
            this element.

        """
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
                # Describes the purpose of this example amoung the set of examples.
                StructField("label", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueBase64Binary", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueBoolean", BooleanType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueCanonical", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueCode", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDate", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDateTime", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueDecimal", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueId", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueInstant", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueInteger", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueMarkdown", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueOid", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valuePositiveInt", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueString", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueTime", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUnsignedInt", IntegerType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUri", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUrl", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField("valueUuid", StringType(), True),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAge", Age.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueCount", Count.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueMoney", Money.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                # The actual value for the element, which must be one of the types allowed for
                # this element.
                StructField(
                    "valueMeta", Meta.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
