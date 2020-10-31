from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.composition_section import Composition_Section


class Composition_Section:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("title", StringType(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("author",ArrayType(Reference.get_schema()), True),
                StructField("focus", Reference.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("mode", code.get_schema(), True),
                StructField("orderedBy", CodeableConcept.get_schema(), True),
                StructField("entry",ArrayType(Reference.get_schema()), True),
                StructField("emptyReason", CodeableConcept.get_schema(), True),
                StructField("section",ArrayType(Composition_Section.get_schema()), True),]
        )

        return schema
