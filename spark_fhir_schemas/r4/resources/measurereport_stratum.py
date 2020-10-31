from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.measurereport_component import MeasureReport_Component
from spark_fhir_schemas.r4.resources.measurereport_population1 import MeasureReport_Population1
from spark_fhir_schemas.r4.resources.quantity import Quantity


class MeasureReport_Stratum:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("value", CodeableConcept.get_schema(), True),
                StructField("component",ArrayType(MeasureReport_Component.get_schema()), True),
                StructField("population",ArrayType(MeasureReport_Population1.get_schema()), True),
                StructField("measureScore", Quantity.get_schema(), True),]
        )

        return schema
