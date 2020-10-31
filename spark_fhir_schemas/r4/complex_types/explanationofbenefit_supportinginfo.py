from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExplanationOfBenefit_SupportingInfo:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource provides: the claim details; adjudication details from the
        processing of a Claim; and optionally account balance information, for
        informing the subscriber of the benefits provided.


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

        sequence: A number to uniquely identify supporting information entries.

        category: The general class of the information supplied: information; exception;
            accident, employment; onset, etc.

        code: System and code pertaining to the specific information regarding special
            conditions relating to the setting, treatment or patient  for which care is
            sought.

        timingDate: The date when or period to which this information refers.

        timingPeriod: The date when or period to which this information refers.

        valueBoolean: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueString: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueQuantity: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueAttachment: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        valueReference: Additional data or information such as resources, documents, images etc.
            including references to the data or the actual inclusion of the data.

        reason: Provides the reason in the situation where a reason code is required in
            addition to the content.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coding import Coding
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
                # A number to uniquely identify supporting information entries.
                StructField(
                    "sequence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                # The general class of the information supplied: information; exception;
                # accident, employment; onset, etc.
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # System and code pertaining to the specific information regarding special
                # conditions relating to the setting, treatment or patient  for which care is
                # sought.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The date when or period to which this information refers.
                StructField("timingDate", StringType(), True),
                # The date when or period to which this information refers.
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField("valueBoolean", BooleanType(), True),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField("valueString", StringType(), True),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # Additional data or information such as resources, documents, images etc.
                # including references to the data or the actual inclusion of the data.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Provides the reason in the situation where a reason code is required in
                # addition to the content.
                StructField(
                    "reason", Coding.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
