from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class QuestionnaireResponse_Answer:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.questionnaireresponse_item import QuestionnaireResponse_Item
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
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueDecimal", IntegerType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueDate", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valueTime", StringType(), True),
                StructField("valueString", StringType(), True),
                StructField("valueUri", StringType(), True),
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        QuestionnaireResponse_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
