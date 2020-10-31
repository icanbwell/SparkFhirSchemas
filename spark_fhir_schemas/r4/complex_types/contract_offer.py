from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.contract_party import Contract_Party
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_Answer
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt


# noinspection PyPep8Naming
class Contract_Offer:
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
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField(
                    "party", ArrayType(Contract_Party.get_schema()), True
                ),
                StructField("topic", Reference.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("decision", CodeableConcept.get_schema(), True),
                StructField(
                    "decisionMode", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "answer", ArrayType(Contract_Answer.get_schema()), True
                ),
                StructField("text", StringType(), True),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "securityLabelNumber", ArrayType(unsignedInt.get_schema()),
                    True
                ),
            ]
        )

        return schema
