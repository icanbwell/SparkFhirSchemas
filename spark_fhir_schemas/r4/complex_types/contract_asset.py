from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.contract_context import Contract_Context
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_Answer
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.contract_valueditem import Contract_ValuedItem


# noinspection PyPep8Naming
class Contract_Asset:
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
                StructField("scope", CodeableConcept.get_schema(), True),
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "typeReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "subtype", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("relationship", Coding.get_schema(), True),
                StructField(
                    "context", ArrayType(Contract_Context.get_schema()), True
                ),
                StructField("condition", StringType(), True),
                StructField(
                    "periodType", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("period", ArrayType(Period.get_schema()), True),
                StructField("usePeriod", ArrayType(Period.get_schema()), True),
                StructField("text", StringType(), True),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "answer", ArrayType(Contract_Answer.get_schema()), True
                ),
                StructField(
                    "securityLabelNumber", ArrayType(unsignedInt.get_schema()),
                    True
                ),
                StructField(
                    "valuedItem", ArrayType(Contract_ValuedItem.get_schema()),
                    True
                ),
            ]
        )

        return schema
