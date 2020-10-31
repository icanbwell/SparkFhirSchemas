from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.datarequirement_codefilter import DataRequirement_CodeFilter
from spark_fhir_schemas.r4.resources.datarequirement_datefilter import DataRequirement_DateFilter
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.datarequirement_sort import DataRequirement_Sort


class DataRequirement:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("type", code.get_schema(), True),
                StructField("profile",ArrayType(canonical.get_schema()), True),
                StructField("subjectCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("subjectReference", Reference.get_schema(), True),
                StructField("mustSupport",ArrayType(string.get_schema()), True),
                StructField("codeFilter",ArrayType(DataRequirement_CodeFilter.get_schema()), True),
                StructField("dateFilter",ArrayType(DataRequirement_DateFilter.get_schema()), True),
                StructField("limit", positiveInt.get_schema(), True),
                StructField("sort",ArrayType(DataRequirement_Sort.get_schema()), True),]
        )

        return schema
