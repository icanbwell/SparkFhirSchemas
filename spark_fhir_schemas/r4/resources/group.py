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
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.group_characteristic import Group_Characteristic
from spark_fhir_schemas.r4.complex_types.group_member import Group_Member


# noinspection PyPep8Naming
class Group:
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
                StructField("active", BooleanType(), True),
                StructField("type", StringType(), True),
                StructField("actual", BooleanType(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("quantity", unsignedInt.get_schema(), True),
                StructField("managingEntity", Reference.get_schema(), True),
                StructField(
                    "characteristic",
                    ArrayType(Group_Characteristic.get_schema()), True
                ),
                StructField(
                    "member", ArrayType(Group_Member.get_schema()), True
                ),
            ]
        )

        return schema
