from pyspark.sql.types import ArrayType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.immunizationrecommendation_datecriterion import ImmunizationRecommendation_DateCriterion
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class ImmunizationRecommendation_Recommendation:
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
                    "vaccineCode", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "targetDisease", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "contraindicatedVaccineCode",
                    ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "forecastStatus", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "forecastReason", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "dateCriterion",
                    ArrayType(
                        ImmunizationRecommendation_DateCriterion.get_schema()
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
                    ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "supportingPatientInformation",
                    ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
