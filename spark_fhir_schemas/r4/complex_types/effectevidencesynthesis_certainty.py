from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_certaintysubcomponent import EffectEvidenceSynthesis_CertaintySubcomponent


# noinspection PyPep8Naming
class EffectEvidenceSynthesis_Certainty:
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
                StructField(
                    "rating", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "certaintySubcomponent",
                    ArrayType(
                        EffectEvidenceSynthesis_CertaintySubcomponent.
                        get_schema()
                    ), True
                ),
            ]
        )

        return schema
