from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImagingStudy_Series:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.imagingstudy_performer import ImagingStudy_Performer
        from spark_fhir_schemas.r4.complex_types.imagingstudy_instance import ImagingStudy_Instance
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
                StructField("uid", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "number", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "modality", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "numberOfInstances",
                    unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "bodySite", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "laterality", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "specimen",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "started", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer",
                    ArrayType(
                        ImagingStudy_Performer.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "instance",
                    ArrayType(
                        ImagingStudy_Instance.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
