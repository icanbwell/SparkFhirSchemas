from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Claim_Procedure:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("date", dateTime.get_schema(), True),
                StructField(
                    "procedureCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "procedureReference", Reference.get_schema(), True
                ),
                StructField("udi", ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
