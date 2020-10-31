from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Questionnaire_Initial:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


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

        valueBoolean: The actual value to for an initial answer.

        valueDecimal: The actual value to for an initial answer.

        valueInteger: The actual value to for an initial answer.

        valueDate: The actual value to for an initial answer.

        valueDateTime: The actual value to for an initial answer.

        valueTime: The actual value to for an initial answer.

        valueString: The actual value to for an initial answer.

        valueUri: The actual value to for an initial answer.

        valueAttachment: The actual value to for an initial answer.

        valueCoding: The actual value to for an initial answer.

        valueQuantity: The actual value to for an initial answer.

        valueReference: The actual value to for an initial answer.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # The actual value to for an initial answer.
                StructField("valueBoolean", BooleanType(), True),
                # The actual value to for an initial answer.
                StructField("valueDecimal", IntegerType(), True),
                # The actual value to for an initial answer.
                StructField("valueInteger", IntegerType(), True),
                # The actual value to for an initial answer.
                StructField("valueDate", StringType(), True),
                # The actual value to for an initial answer.
                StructField("valueDateTime", StringType(), True),
                # The actual value to for an initial answer.
                StructField("valueTime", StringType(), True),
                # The actual value to for an initial answer.
                StructField("valueString", StringType(), True),
                # The actual value to for an initial answer.
                StructField("valueUri", StringType(), True),
                # The actual value to for an initial answer.
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The actual value to for an initial answer.
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                # The actual value to for an initial answer.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The actual value to for an initial answer.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
