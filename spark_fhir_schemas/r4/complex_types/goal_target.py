from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.duration import Duration


class Goal_Target:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("measure", CodeableConcept.get_schema(), True),
                StructField("detailQuantity", Quantity.get_schema(), True),
                StructField("detailRange", Range.get_schema(), True),
                StructField("detailCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("detailString", StringType(), True),
                StructField("detailBoolean", BooleanType(), True),
                StructField("detailInteger", IntegerType(), True),
                StructField("detailRatio", Ratio.get_schema(), True),
                StructField("dueDate", StringType(), True),
                StructField("dueDuration", Duration.get_schema(), True),
            ]
        )

        return schema
