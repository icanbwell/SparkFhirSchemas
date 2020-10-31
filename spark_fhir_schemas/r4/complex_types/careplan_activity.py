from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.careplan_detail import CarePlan_Detail


# noinspection PyPep8Naming
class CarePlan_Activity:
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
                    "outcomeCodeableConcept",
                    ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "outcomeReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "progress", ArrayType(Annotation.get_schema()), True
                ),
                StructField("reference", Reference.get_schema(), True),
                StructField("detail", CarePlan_Detail.get_schema(), True),
            ]
        )

        return schema
