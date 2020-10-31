from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationRequest_DispenseRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.medicationrequest_initialfill import MedicationRequest_InitialFill
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "initialFill",
                    MedicationRequest_InitialFill.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dispenseInterval",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "validityPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "numberOfRepeatsAllowed",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "expectedSupplyDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
