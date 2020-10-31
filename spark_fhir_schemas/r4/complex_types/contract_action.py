from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_Action:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contract_subject import Contract_Subject
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
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
                StructField("doNotPerform", BooleanType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subject",
                    ArrayType(
                        Contract_Subject.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "intent", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("contextLinkId", ArrayType(StringType()), True),
                StructField("occurrenceDateTime", StringType(), True),
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "requester",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("requesterLinkId", ArrayType(StringType()), True),
                StructField(
                    "performerType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "performerRole",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("performerLinkId", ArrayType(StringType()), True),
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("reason", ArrayType(StringType()), True),
                StructField("reasonLinkId", ArrayType(StringType()), True),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
