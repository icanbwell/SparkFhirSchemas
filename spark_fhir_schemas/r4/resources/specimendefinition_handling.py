from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.string import string


class SpecimenDefinition_Handling:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("temperatureQualifier", CodeableConcept.get_schema(), True),
                StructField("temperatureRange", Range.get_schema(), True),
                StructField("maxDuration", Duration.get_schema(), True),
                StructField("instruction", StringType(), True),]
        )

        return schema
