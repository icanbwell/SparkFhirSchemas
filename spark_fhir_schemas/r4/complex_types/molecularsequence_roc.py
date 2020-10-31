from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.decimal import decimal


class MolecularSequence_Roc:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("score",ArrayType(integer.get_schema()), True),
                StructField("numTP",ArrayType(integer.get_schema()), True),
                StructField("numFP",ArrayType(integer.get_schema()), True),
                StructField("numFN",ArrayType(integer.get_schema()), True),
                StructField("precision",ArrayType(decimal.get_schema()), True),
                StructField("sensitivity",ArrayType(decimal.get_schema()), True),
                StructField("fMeasure",ArrayType(decimal.get_schema()), True),
            ]
        )

        return schema
