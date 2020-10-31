from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.annotation import Annotation


class FamilyMemberHistory_Condition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("outcome", CodeableConcept.get_schema(), True),
                StructField("contributedToDeath", BooleanType(), True),
                StructField("onsetAge", Age.get_schema(), True),
                StructField("onsetRange", Range.get_schema(), True),
                StructField("onsetPeriod", Period.get_schema(), True),
                StructField("onsetString", StringType(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
