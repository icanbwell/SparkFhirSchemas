from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.instant import instant


# noinspection PyPep8Naming
class Slot:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField(
                    "serviceCategory", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "serviceType", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "specialty", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "appointmentType", CodeableConcept.get_schema(), True
                ),
                StructField("schedule", Reference.get_schema(), True),
                StructField("status", StringType(), True),
                StructField("start", instant.get_schema(), True),
                StructField("end", instant.get_schema(), True),
                StructField("overbooked", BooleanType(), True),
                StructField("comment", StringType(), True),
            ]
        )

        return schema
