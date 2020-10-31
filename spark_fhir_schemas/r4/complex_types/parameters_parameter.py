from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Parameters_Parameter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource is a non-persisted resource used to pass information into and
        back from an [operation](operations.html). It has no other use, and there is
        no RESTful endpoint associated with it.


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

        name: The name of the parameter (reference to the operation definition).

        valueBase64Binary: If the parameter is a data type.

        valueBoolean: If the parameter is a data type.

        valueCanonical: If the parameter is a data type.

        valueCode: If the parameter is a data type.

        valueDate: If the parameter is a data type.

        valueDateTime: If the parameter is a data type.

        valueDecimal: If the parameter is a data type.

        valueId: If the parameter is a data type.

        valueInstant: If the parameter is a data type.

        valueInteger: If the parameter is a data type.

        valueMarkdown: If the parameter is a data type.

        valueOid: If the parameter is a data type.

        valuePositiveInt: If the parameter is a data type.

        valueString: If the parameter is a data type.

        valueTime: If the parameter is a data type.

        valueUnsignedInt: If the parameter is a data type.

        valueUri: If the parameter is a data type.

        valueUrl: If the parameter is a data type.

        valueUuid: If the parameter is a data type.

        valueAddress: If the parameter is a data type.

        valueAge: If the parameter is a data type.

        valueAnnotation: If the parameter is a data type.

        valueAttachment: If the parameter is a data type.

        valueCodeableConcept: If the parameter is a data type.

        valueCoding: If the parameter is a data type.

        valueContactPoint: If the parameter is a data type.

        valueCount: If the parameter is a data type.

        valueDistance: If the parameter is a data type.

        valueDuration: If the parameter is a data type.

        valueHumanName: If the parameter is a data type.

        valueIdentifier: If the parameter is a data type.

        valueMoney: If the parameter is a data type.

        valuePeriod: If the parameter is a data type.

        valueQuantity: If the parameter is a data type.

        valueRange: If the parameter is a data type.

        valueRatio: If the parameter is a data type.

        valueReference: If the parameter is a data type.

        valueSampledData: If the parameter is a data type.

        valueSignature: If the parameter is a data type.

        valueTiming: If the parameter is a data type.

        valueContactDetail: If the parameter is a data type.

        valueContributor: If the parameter is a data type.

        valueDataRequirement: If the parameter is a data type.

        valueExpression: If the parameter is a data type.

        valueParameterDefinition: If the parameter is a data type.

        valueRelatedArtifact: If the parameter is a data type.

        valueTriggerDefinition: If the parameter is a data type.

        valueUsageContext: If the parameter is a data type.

        valueDosage: If the parameter is a data type.

        valueMeta: If the parameter is a data type.

        resource: If the parameter is a whole resource.

        part: A named part of a multi-part parameter.

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
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
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
                # The name of the parameter (reference to the operation definition).
                StructField("name", StringType(), True),
                # If the parameter is a data type.
                StructField("valueBase64Binary", StringType(), True),
                # If the parameter is a data type.
                StructField("valueBoolean", BooleanType(), True),
                # If the parameter is a data type.
                StructField("valueCanonical", StringType(), True),
                # If the parameter is a data type.
                StructField("valueCode", StringType(), True),
                # If the parameter is a data type.
                StructField("valueDate", StringType(), True),
                # If the parameter is a data type.
                StructField("valueDateTime", StringType(), True),
                # If the parameter is a data type.
                StructField("valueDecimal", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueId", StringType(), True),
                # If the parameter is a data type.
                StructField("valueInstant", StringType(), True),
                # If the parameter is a data type.
                StructField("valueInteger", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueMarkdown", StringType(), True),
                # If the parameter is a data type.
                StructField("valueOid", StringType(), True),
                # If the parameter is a data type.
                StructField("valuePositiveInt", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueString", StringType(), True),
                # If the parameter is a data type.
                StructField("valueTime", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUnsignedInt", IntegerType(), True),
                # If the parameter is a data type.
                StructField("valueUri", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUrl", StringType(), True),
                # If the parameter is a data type.
                StructField("valueUuid", StringType(), True),
                # If the parameter is a data type.
                StructField(
                    "valueAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueAge", Age.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueAnnotation",
                    Annotation.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueContactPoint",
                    ContactPoint.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueCount", Count.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueDistance", Distance.get_schema(recursion_depth + 1),
                    True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueHumanName",
                    HumanName.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueMoney", Money.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueTiming", Timing.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueContactDetail",
                    ContactDetail.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueContributor",
                    Contributor.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueParameterDefinition",
                    ParameterDefinition.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueRelatedArtifact",
                    RelatedArtifact.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueUsageContext",
                    UsageContext.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueDosage", Dosage.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a data type.
                StructField(
                    "valueMeta", Meta.get_schema(recursion_depth + 1), True
                ),
                # If the parameter is a whole resource.
                StructField(
                    "resource", ResourceList.get_schema(recursion_depth + 1),
                    True
                ),
                # A named part of a multi-part parameter.
                StructField(
                    "part",
                    ArrayType(
                        Parameters_Parameter.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
