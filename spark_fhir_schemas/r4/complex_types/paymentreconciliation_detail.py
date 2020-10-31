from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PaymentReconciliation_Detail:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.money import Money
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
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "predecessor", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "request", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "submitter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "response", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("date", DateType(), True),
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "payee", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "amount", Money.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
