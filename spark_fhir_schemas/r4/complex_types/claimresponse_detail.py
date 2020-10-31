from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_Adjudication
from spark_fhir_schemas.r4.complex_types.claimresponse_subdetail import ClaimResponse_SubDetail


class ClaimResponse_Detail:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("detailSequence", positiveInt.get_schema(), True),
                StructField("noteNumber",ArrayType(positiveInt.get_schema()), True),
                StructField("adjudication",ArrayType(ClaimResponse_Adjudication.get_schema()), True),
                StructField("subDetail",ArrayType(ClaimResponse_SubDetail.get_schema()), True),
            ]
        )

        return schema
