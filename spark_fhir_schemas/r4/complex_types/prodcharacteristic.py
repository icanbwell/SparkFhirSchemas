from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


class ProdCharacteristic:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("height", Quantity.get_schema(), True),
                StructField("width", Quantity.get_schema(), True),
                StructField("depth", Quantity.get_schema(), True),
                StructField("weight", Quantity.get_schema(), True),
                StructField("nominalVolume", Quantity.get_schema(), True),
                StructField("externalDiameter", Quantity.get_schema(), True),
                StructField("shape", StringType(), True),
                StructField("color",ArrayType(string.get_schema()), True),
                StructField("imprint",ArrayType(string.get_schema()), True),
                StructField("image",ArrayType(Attachment.get_schema()), True),
                StructField("scoring", CodeableConcept.get_schema(), True),
            ]
        )

        return schema
