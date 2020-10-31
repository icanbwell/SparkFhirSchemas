from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Identifier:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("use", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("system", uri.get_schema(), True),
                StructField("value", StringType(), True),
                StructField("period", Period.get_schema(), True),
                StructField("assigner", Reference.get_schema(), True),
            ]
        )

        return schema
