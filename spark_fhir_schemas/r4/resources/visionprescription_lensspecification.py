from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.visionprescription_prism import VisionPrescription_Prism
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.annotation import Annotation


class VisionPrescription_LensSpecification:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("product", CodeableConcept.get_schema(), True),
                StructField("eye", StringType(), True),
                StructField("sphere", decimal.get_schema(), True),
                StructField("cylinder", decimal.get_schema(), True),
                StructField("axis", integer.get_schema(), True),
                StructField("prism",ArrayType(VisionPrescription_Prism.get_schema()), True),
                StructField("add", decimal.get_schema(), True),
                StructField("power", decimal.get_schema(), True),
                StructField("backCurve", decimal.get_schema(), True),
                StructField("diameter", decimal.get_schema(), True),
                StructField("duration", Quantity.get_schema(), True),
                StructField("color", StringType(), True),
                StructField("brand", StringType(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
