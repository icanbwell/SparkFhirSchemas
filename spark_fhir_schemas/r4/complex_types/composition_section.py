from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.code import code


# noinspection PyPep8Naming
class Composition_Section:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("title", StringType(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("author", ArrayType(Reference.get_schema()), True),
                StructField("focus", Reference.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("mode", code.get_schema(), True),
                StructField("orderedBy", CodeableConcept.get_schema(), True),
                StructField("entry", ArrayType(Reference.get_schema()), True),
                StructField("emptyReason", CodeableConcept.get_schema(), True),
                StructField(
                    "section", ArrayType(Composition_Section.get_schema()),
                    True
                ),
            ]
        )

        return schema
