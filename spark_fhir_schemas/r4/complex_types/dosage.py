from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Dosage:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.dosage_doseandrate import Dosage_DoseAndRate
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                    "sequence", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("text", StringType(), True),
                StructField(
                    "additionalInstruction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("patientInstruction", StringType(), True),
                StructField(
                    "timing", Timing.get_schema(recursion_depth + 1), True
                ),
                StructField("asNeededBoolean", BooleanType(), True),
                StructField(
                    "asNeededCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "site", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "route", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "doseAndRate",
                    ArrayType(
                        Dosage_DoseAndRate.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "maxDosePerPeriod", Ratio.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "maxDosePerAdministration",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "maxDosePerLifetime",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
