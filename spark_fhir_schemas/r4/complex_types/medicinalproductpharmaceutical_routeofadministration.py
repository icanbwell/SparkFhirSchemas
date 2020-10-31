from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.medicinalproductpharmaceutical_targetspecies import MedicinalProductPharmaceutical_TargetSpecies


# noinspection PyPep8Naming
class MedicinalProductPharmaceutical_RouteOfAdministration:
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
                StructField("firstDose", Quantity.get_schema(), True),
                StructField("maxSingleDose", Quantity.get_schema(), True),
                StructField("maxDosePerDay", Quantity.get_schema(), True),
                StructField(
                    "maxDosePerTreatmentPeriod", Ratio.get_schema(), True
                ),
                StructField("maxTreatmentPeriod", Duration.get_schema(), True),
                StructField(
                    "targetSpecies",
                    ArrayType(
                        MedicinalProductPharmaceutical_TargetSpecies.
                        get_schema()
                    ), True
                ),
            ]
        )

        return schema
