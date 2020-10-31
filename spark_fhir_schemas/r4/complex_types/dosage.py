from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.dosage_doseandrate import Dosage_DoseAndRate
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity


class Dosage:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("sequence", integer.get_schema(), True),
                StructField("text", StringType(), True),
                StructField("additionalInstruction",ArrayType(CodeableConcept.get_schema()), True),
                StructField("patientInstruction", StringType(), True),
                StructField("timing", Timing.get_schema(), True),
                StructField("asNeededBoolean", BooleanType(), True),
                StructField("asNeededCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("site", CodeableConcept.get_schema(), True),
                StructField("route", CodeableConcept.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("doseAndRate",ArrayType(Dosage_DoseAndRate.get_schema()), True),
                StructField("maxDosePerPeriod", Ratio.get_schema(), True),
                StructField("maxDosePerAdministration", Quantity.get_schema(), True),
                StructField("maxDosePerLifetime", Quantity.get_schema(), True),
            ]
        )

        return schema
