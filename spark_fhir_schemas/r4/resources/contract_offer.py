from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.contract_party import Contract_Party
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.contract_answer import Contract_Answer
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt


class Contract_Offer:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("party",ArrayType(Contract_Party.get_schema()), True),
                StructField("topic", Reference.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("decision", CodeableConcept.get_schema(), True),
                StructField("decisionMode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("answer",ArrayType(Contract_Answer.get_schema()), True),
                StructField("text", StringType(), True),
                StructField("linkId",ArrayType(string.get_schema()), True),
                StructField("securityLabelNumber",ArrayType(unsignedInt.get_schema()), True),]
        )

        return schema
