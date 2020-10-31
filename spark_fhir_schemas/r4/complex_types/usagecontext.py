from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class UsageContext:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Specifies clinical/business/etc. metadata that can be used to retrieve, index
        and/or categorize an artifact. This metadata can either be specific to the
        applicable population (e.g., age category, DRG) or the specific context of
        care (e.g., venue, care setting, provider of care).


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: A code that identifies the type of context being specified by this usage
            context.

        valueCodeableConcept: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        valueQuantity: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        valueRange: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        valueReference: A value that defines the context specified in this context of use. The
            interpretation of the value is defined by the code.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
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
                # A code that identifies the type of context being specified by this usage
                # context.
                StructField(
                    "code", Coding.get_schema(recursion_depth + 1), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # A value that defines the context specified in this context of use. The
                # interpretation of the value is defined by the code.
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
