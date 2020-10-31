from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.medicinalproductpharmaceutical_targetspecies import MedicinalProductPharmaceutical_TargetSpecies


class MedicinalProductPharmaceutical_RouteOfAdministration:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("firstDose", Quantity.get_schema(), True),
                StructField("maxSingleDose", Quantity.get_schema(), True),
                StructField("maxDosePerDay", Quantity.get_schema(), True),
                StructField("maxDosePerTreatmentPeriod", Ratio.get_schema(), True),
                StructField("maxTreatmentPeriod", Duration.get_schema(), True),
                StructField("targetSpecies",ArrayType(MedicinalProductPharmaceutical_TargetSpecies.get_schema()), True),]
        )

        return schema
