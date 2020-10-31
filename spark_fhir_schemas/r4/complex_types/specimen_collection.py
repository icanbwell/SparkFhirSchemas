from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class Specimen_Collection:
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
                StructField("collector", Reference.get_schema(), True),
                StructField("collectedDateTime", StringType(), True),
                StructField("collectedPeriod", Period.get_schema(), True),
                StructField("duration", Duration.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("bodySite", CodeableConcept.get_schema(), True),
                StructField(
                    "fastingStatusCodeableConcept",
                    CodeableConcept.get_schema(), True
                ),
                StructField(
                    "fastingStatusDuration", Duration.get_schema(), True
                ),
            ]
        )

        return schema
