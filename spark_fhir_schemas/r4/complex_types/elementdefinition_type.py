from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.canonical import canonical


class ElementDefinition_Type:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", uri.get_schema(), True),
                StructField("profile",ArrayType(canonical.get_schema()), True),
                StructField("targetProfile",ArrayType(canonical.get_schema()), True),
                StructField("aggregation",ArrayType(None.get_schema()), True),
                StructField("versioning", StringType(), True),
            ]
        )

        return schema
