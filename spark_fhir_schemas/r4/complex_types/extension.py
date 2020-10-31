from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Extension:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Optional Extension Element - found in all resources.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        url: Source of the definition for the extension code - a logical name or a URL.

        valueBase64Binary: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueBoolean: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCanonical: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCode: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDate: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDateTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDecimal: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueId: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueInstant: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueInteger: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueMarkdown: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueOid: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePositiveInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueString: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueTime: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUnsignedInt: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUri: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUrl: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUuid: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueAddress: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueAge: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueAnnotation: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueAttachment: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCodeableConcept: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCoding: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueContactPoint: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueCount: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDistance: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDuration: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueHumanName: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueIdentifier: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueMoney: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valuePeriod: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueQuantity: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueRange: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueRatio: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueReference: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueSampledData: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueSignature: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueTiming: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueContactDetail: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueContributor: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDataRequirement: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueExpression: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueParameterDefinition: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueRelatedArtifact: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueTriggerDefinition: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueUsageContext: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueDosage: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        valueMeta: Value of extension - must be one of a constrained set of the data types (see
            [Extensibility](extensibility.html) for a list).

        """
        from spark_fhir_schemas.r4.simple_types.uri import uri
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
                # Source of the definition for the extension code - a logical name or a URL.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueBase64Binary", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueBoolean", BooleanType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueCanonical", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueCode", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDate", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDateTime", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueDecimal", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueId", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueInstant", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueInteger", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueMarkdown", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueOid", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valuePositiveInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueString", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueTime", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUnsignedInt", IntegerType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUri", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUrl", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField("valueUuid", StringType(), True),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueAge", Age.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueCount", Count.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueMoney", Money.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                # Value of extension - must be one of a constrained set of the data types (see
                # [Extensibility](extensibility.html) for a list).
                StructField(
                    "valueMeta", Meta.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
