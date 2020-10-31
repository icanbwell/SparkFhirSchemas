from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_ValuedItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
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
                StructField(
                    "entityCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "entityReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "effectiveTime", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "points", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                StructField("payment", StringType(), True),
                StructField(
                    "paymentDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "recipient", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
