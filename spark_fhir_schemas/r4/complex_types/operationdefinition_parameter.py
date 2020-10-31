from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.operationdefinition_binding import OperationDefinition_Binding
from spark_fhir_schemas.r4.complex_types.operationdefinition_referencedfrom import OperationDefinition_ReferencedFrom
from spark_fhir_schemas.r4.complex_types.operationdefinition_parameter import OperationDefinition_Parameter


class OperationDefinition_Parameter:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("name", code.get_schema(), True),
                StructField("use", StringType(), True),
                StructField("min", integer.get_schema(), True),
                StructField("max", StringType(), True),
                StructField("documentation", StringType(), True),
                StructField("type", code.get_schema(), True),
                StructField("targetProfile",ArrayType(canonical.get_schema()), True),
                StructField("searchType", StringType(), True),
                StructField("binding", OperationDefinition_Binding.get_schema(), True),
                StructField("referencedFrom",ArrayType(OperationDefinition_ReferencedFrom.get_schema()), True),
                StructField("part",ArrayType(OperationDefinition_Parameter.get_schema()), True),
            ]
        )

        return schema
