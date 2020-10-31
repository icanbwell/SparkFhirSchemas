from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.quantity import Quantity


# noinspection PyPep8Naming
class CarePlan_Detail:
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
                StructField("kind", code.get_schema(), True),
                StructField(
                    "instantiatesCanonical", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField(
                    "instantiatesUri", ArrayType(uri.get_schema()), True
                ),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField("goal", ArrayType(Reference.get_schema()), True),
                StructField("status", StringType(), True),
                StructField(
                    "statusReason", CodeableConcept.get_schema(), True
                ),
                StructField("doNotPerform", BooleanType(), True),
                StructField("scheduledTiming", Timing.get_schema(), True),
                StructField("scheduledPeriod", Period.get_schema(), True),
                StructField("scheduledString", StringType(), True),
                StructField("location", Reference.get_schema(), True),
                StructField(
                    "performer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "productCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("productReference", Reference.get_schema(), True),
                StructField("dailyAmount", Quantity.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("description", StringType(), True),
            ]
        )

        return schema
