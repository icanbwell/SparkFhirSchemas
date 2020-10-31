from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.coding import Coding


class ExplanationOfBenefit_SupportingInfo:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
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
                StructField("reason", Coding.get_schema(), True),]
        )

        return schema
