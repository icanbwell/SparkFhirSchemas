from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.canonical import canonical


class ElementDefinition_Constraint:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("key", id.get_schema(), True),
                StructField("requirements", StringType(), True),
                StructField("severity", StringType(), True),
                StructField("human", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("xpath", StringType(), True),
                StructField("source", canonical.get_schema(), True),
            ]
        )

        return schema
