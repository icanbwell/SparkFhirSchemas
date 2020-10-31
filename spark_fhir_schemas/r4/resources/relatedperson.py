from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RelatedPerson:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.humanname import HumanName
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedperson_communication import RelatedPerson_Communication
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("active", BooleanType(), True),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "relationship",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "name",
                    ArrayType(HumanName.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("gender", StringType(), True),
                StructField("birthDate", DateType(), True),
                StructField(
                    "address",
                    ArrayType(Address.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "photo",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "communication",
                    ArrayType(
                        RelatedPerson_Communication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
