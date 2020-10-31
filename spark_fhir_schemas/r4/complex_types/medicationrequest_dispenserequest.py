from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.medicationrequest_initialfill import MedicationRequest_InitialFill
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class MedicationRequest_DispenseRequest:
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
                    "initialFill", MedicationRequest_InitialFill.get_schema(),
                    True
                ),
                StructField("dispenseInterval", Duration.get_schema(), True),
                StructField("validityPeriod", Period.get_schema(), True),
                StructField(
                    "numberOfRepeatsAllowed", unsignedInt.get_schema(), True
                ),
                StructField("quantity", Quantity.get_schema(), True),
                StructField(
                    "expectedSupplyDuration", Duration.get_schema(), True
                ),
                StructField("performer", Reference.get_schema(), True),
            ]
        )

        return schema
