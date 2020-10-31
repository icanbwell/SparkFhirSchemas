from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class OperationOutcome_Issue:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("severity", StringType(), True),
                StructField("code", StringType(), True),
                StructField("details", CodeableConcept.get_schema(), True),
                StructField("diagnostics", StringType(), True),
                StructField("location", ArrayType(StringType()), True),
                StructField("expression", ArrayType(StringType()), True),
            ]
        )

        return schema
