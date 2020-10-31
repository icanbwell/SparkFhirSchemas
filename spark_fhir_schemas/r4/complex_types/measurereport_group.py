from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.measurereport_population import MeasureReport_Population
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.measurereport_stratifier import MeasureReport_Stratifier


# noinspection PyPep8Naming
class MeasureReport_Group:
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
                StructField(
                    "population",
                    ArrayType(MeasureReport_Population.get_schema()), True
                ),
                StructField("measureScore", Quantity.get_schema(), True),
                StructField(
                    "stratifier",
                    ArrayType(MeasureReport_Stratifier.get_schema()), True
                ),
            ]
        )

        return schema
