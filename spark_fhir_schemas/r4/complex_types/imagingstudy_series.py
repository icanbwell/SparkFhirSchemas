from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.imagingstudy_performer import ImagingStudy_Performer
from spark_fhir_schemas.r4.complex_types.imagingstudy_instance import ImagingStudy_Instance


# noinspection PyPep8Naming
class ImagingStudy_Series:
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
                StructField("uid", id.get_schema(), True),
                StructField("number", unsignedInt.get_schema(), True),
                StructField("modality", Coding.get_schema(), True),
                StructField("description", StringType(), True),
                StructField(
                    "numberOfInstances", unsignedInt.get_schema(), True
                ),
                StructField(
                    "endpoint", ArrayType(Reference.get_schema()), True
                ),
                StructField("bodySite", Coding.get_schema(), True),
                StructField("laterality", Coding.get_schema(), True),
                StructField(
                    "specimen", ArrayType(Reference.get_schema()), True
                ),
                StructField("started", dateTime.get_schema(), True),
                StructField(
                    "performer",
                    ArrayType(ImagingStudy_Performer.get_schema()), True
                ),
                StructField(
                    "instance", ArrayType(ImagingStudy_Instance.get_schema()),
                    True
                ),
            ]
        )

        return schema
