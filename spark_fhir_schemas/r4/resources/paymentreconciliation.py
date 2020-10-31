from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PaymentReconciliation:
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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.complex_types.paymentreconciliation_detail import PaymentReconciliation_Detail
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.paymentreconciliation_processnote import PaymentReconciliation_ProcessNote
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
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "paymentIssuer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "request", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "requestor", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("outcome", StringType(), True),
                StructField("disposition", StringType(), True),
                StructField("paymentDate", DateType(), True),
                StructField(
                    "paymentAmount", Money.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "paymentIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "detail",
                    ArrayType(
                        PaymentReconciliation_Detail.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "formCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "processNote",
                    ArrayType(
                        PaymentReconciliation_ProcessNote.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
