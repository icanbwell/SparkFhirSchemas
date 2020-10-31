from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.id import id


class ImplementationGuide_Resource:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("reference", Reference.get_schema(), True),
                StructField("fhirVersion",ArrayType(None.get_schema()), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("exampleBoolean", BooleanType(), True),
                StructField("exampleCanonical", StringType(), True),
                StructField("groupingId", id.get_schema(), True),
            ]
        )

        return schema
