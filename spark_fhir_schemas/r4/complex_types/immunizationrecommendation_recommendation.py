from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImmunizationRecommendation_Recommendation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.immunizationrecommendation_datecriterion import ImmunizationRecommendation_DateCriterion
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "vaccineCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "targetDisease",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contraindicatedVaccineCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "forecastStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "forecastReason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "dateCriterion",
                    ArrayType(
                        ImmunizationRecommendation_DateCriterion.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("description", StringType(), True),
                StructField("series", StringType(), True),
                StructField("doseNumberPositiveInt", IntegerType(), True),
                StructField("doseNumberString", StringType(), True),
                StructField("seriesDosesPositiveInt", IntegerType(), True),
                StructField("seriesDosesString", StringType(), True),
                StructField(
                    "supportingImmunization",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "supportingPatientInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
