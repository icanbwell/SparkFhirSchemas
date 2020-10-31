from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.molecularsequence_roc import MolecularSequence_Roc


class MolecularSequence_Quality:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", StringType(), True),
                StructField("standardSequence", CodeableConcept.get_schema(), True),
                StructField("start", integer.get_schema(), True),
                StructField("end", integer.get_schema(), True),
                StructField("score", Quantity.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("truthTP", decimal.get_schema(), True),
                StructField("queryTP", decimal.get_schema(), True),
                StructField("truthFN", decimal.get_schema(), True),
                StructField("queryFP", decimal.get_schema(), True),
                StructField("gtFP", decimal.get_schema(), True),
                StructField("precision", decimal.get_schema(), True),
                StructField("recall", decimal.get_schema(), True),
                StructField("fScore", decimal.get_schema(), True),
                StructField("roc", MolecularSequence_Roc.get_schema(), True),]
        )

        return schema
