from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.identifier import Identifier


class SubstanceProtein_Subunit:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("subunit", integer.get_schema(), True),
                StructField("sequence", StringType(), True),
                StructField("length", integer.get_schema(), True),
                StructField("sequenceAttachment", Attachment.get_schema(), True),
                StructField("nTerminalModificationId", Identifier.get_schema(), True),
                StructField("nTerminalModification", StringType(), True),
                StructField("cTerminalModificationId", Identifier.get_schema(), True),
                StructField("cTerminalModification", StringType(), True),
            ]
        )

        return schema
