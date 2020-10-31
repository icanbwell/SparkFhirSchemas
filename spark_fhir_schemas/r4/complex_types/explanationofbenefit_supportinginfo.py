from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.coding import Coding


# noinspection PyPep8Naming
class ExplanationOfBenefit_SupportingInfo:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("timingDate", StringType(), True),
                StructField("timingPeriod", Period.get_schema(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueString", StringType(), True),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueAttachment", Attachment.get_schema(), True),
                StructField("valueReference", Reference.get_schema(), True),
                StructField("reason", Coding.get_schema(), True),
            ]
        )

        return schema
