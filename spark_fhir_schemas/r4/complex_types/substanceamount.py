from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substanceamount_referencerange import SubstanceAmount_ReferenceRange


class SubstanceAmount:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountRange", Range.get_schema(), True),
                StructField("amountString", StringType(), True),
                StructField("amountType", CodeableConcept.get_schema(), True),
                StructField("amountText", StringType(), True),
                StructField("referenceRange", SubstanceAmount_ReferenceRange.get_schema(), True),
            ]
        )

        return schema
