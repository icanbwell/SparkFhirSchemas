from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_item import CoverageEligibilityResponse_Item


# noinspection PyPep8Naming
class CoverageEligibilityResponse_Insurance:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("coverage", Reference.get_schema(), True),
                StructField("inforce", BooleanType(), True),
                StructField("benefitPeriod", Period.get_schema(), True),
                StructField(
                    "item",
                    ArrayType(CoverageEligibilityResponse_Item.get_schema()),
                    True
                ),
            ]
        )

        return schema
