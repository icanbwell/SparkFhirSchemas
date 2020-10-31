from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.annotation import Annotation


class AllergyIntolerance_Reaction:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("substance", CodeableConcept.get_schema(), True),
                StructField("manifestation",ArrayType(CodeableConcept.get_schema()), True),
                StructField("description", StringType(), True),
                StructField("onset", dateTime.get_schema(), True),
                StructField("severity", StringType(), True),
                StructField("exposureRoute", CodeableConcept.get_schema(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
