from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Task_Input:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A task to be performed.


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

        type: A code or description indicating how the input is intended to be used as part
            of the task execution.

        valueBase64Binary: The value of the input parameter as a basic type.

        valueBoolean: The value of the input parameter as a basic type.

        valueCanonical: The value of the input parameter as a basic type.

        valueCode: The value of the input parameter as a basic type.

        valueDate: The value of the input parameter as a basic type.

        valueDateTime: The value of the input parameter as a basic type.

        valueDecimal: The value of the input parameter as a basic type.

        valueId: The value of the input parameter as a basic type.

        valueInstant: The value of the input parameter as a basic type.

        valueInteger: The value of the input parameter as a basic type.

        valueMarkdown: The value of the input parameter as a basic type.

        valueOid: The value of the input parameter as a basic type.

        valuePositiveInt: The value of the input parameter as a basic type.

        valueString: The value of the input parameter as a basic type.

        valueTime: The value of the input parameter as a basic type.

        valueUnsignedInt: The value of the input parameter as a basic type.

        valueUri: The value of the input parameter as a basic type.

        valueUrl: The value of the input parameter as a basic type.

        valueUuid: The value of the input parameter as a basic type.

        valueAddress: The value of the input parameter as a basic type.

        valueAge: The value of the input parameter as a basic type.

        valueAnnotation: The value of the input parameter as a basic type.

        valueAttachment: The value of the input parameter as a basic type.

        valueCodeableConcept: The value of the input parameter as a basic type.

        valueCoding: The value of the input parameter as a basic type.

        valueContactPoint: The value of the input parameter as a basic type.

        valueCount: The value of the input parameter as a basic type.

        valueDistance: The value of the input parameter as a basic type.

        valueDuration: The value of the input parameter as a basic type.

        valueHumanName: The value of the input parameter as a basic type.

        valueIdentifier: The value of the input parameter as a basic type.

        valueMoney: The value of the input parameter as a basic type.

        valuePeriod: The value of the input parameter as a basic type.

        valueQuantity: The value of the input parameter as a basic type.

        valueRange: The value of the input parameter as a basic type.

        valueRatio: The value of the input parameter as a basic type.

        valueReference: The value of the input parameter as a basic type.

        valueSampledData: The value of the input parameter as a basic type.

        valueSignature: The value of the input parameter as a basic type.

        valueTiming: The value of the input parameter as a basic type.

        valueContactDetail: The value of the input parameter as a basic type.

        valueContributor: The value of the input parameter as a basic type.

        valueDataRequirement: The value of the input parameter as a basic type.

        valueExpression: The value of the input parameter as a basic type.

        valueParameterDefinition: The value of the input parameter as a basic type.

        valueRelatedArtifact: The value of the input parameter as a basic type.

        valueTriggerDefinition: The value of the input parameter as a basic type.

        valueUsageContext: The value of the input parameter as a basic type.

        valueDosage: The value of the input parameter as a basic type.

        valueMeta: The value of the input parameter as a basic type.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
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
                # A code or description indicating how the input is intended to be used as part
                # of the task execution.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the input parameter as a basic type.
                StructField("valueBase64Binary", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueBoolean", BooleanType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueCanonical", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueCode", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueDate", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueDateTime", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueDecimal", IntegerType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueId", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueInstant", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueInteger", IntegerType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueMarkdown", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueOid", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valuePositiveInt", IntegerType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueString", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueTime", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueUnsignedInt", IntegerType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueUri", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueUrl", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField("valueUuid", StringType(), True),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueAge", Age.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueCount", Count.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueMoney", Money.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                # The value of the input parameter as a basic type.
                StructField(
                    "valueMeta", Meta.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
