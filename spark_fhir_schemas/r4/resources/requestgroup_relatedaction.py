from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.range import Range


class RequestGroup_RelatedAction:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("actionId", id.get_schema(), True),
                StructField("relationship", code.get_schema(), True),
                StructField("offsetDuration", Duration.get_schema(), True),
                StructField("offsetRange", Range.get_schema(), True),]
        )

        return schema
