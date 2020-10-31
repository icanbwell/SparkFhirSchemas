from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.age import Age
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class FamilyMemberHistory_Condition:
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
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("outcome", CodeableConcept.get_schema(), True),
                StructField("contributedToDeath", BooleanType(), True),
                StructField("onsetAge", Age.get_schema(), True),
                StructField("onsetRange", Range.get_schema(), True),
                StructField("onsetPeriod", Period.get_schema(), True),
                StructField("onsetString", StringType(), True),
                StructField("note", ArrayType(Annotation.get_schema()), True),
            ]
        )

        return schema
