from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.ratio import Ratio


# noinspection PyPep8Naming
class MedicationAdministration_Dosage:
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
                StructField("text", StringType(), True),
                StructField("site", CodeableConcept.get_schema(), True),
                StructField("route", CodeableConcept.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("dose", Quantity.get_schema(), True),
                StructField("rateRatio", Ratio.get_schema(), True),
                StructField("rateQuantity", Quantity.get_schema(), True),
            ]
        )

        return schema
