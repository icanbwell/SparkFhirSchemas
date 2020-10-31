from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ClaimResponse:
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
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.claimresponse_item import ClaimResponse_Item
        from spark_fhir_schemas.r4.complex_types.claimresponse_additem import ClaimResponse_AddItem
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_Adjudication
        from spark_fhir_schemas.r4.complex_types.claimresponse_total import ClaimResponse_Total
        from spark_fhir_schemas.r4.complex_types.claimresponse_payment import ClaimResponse_Payment
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.claimresponse_processnote import ClaimResponse_ProcessNote
        from spark_fhir_schemas.r4.complex_types.claimresponse_insurance import ClaimResponse_Insurance
        from spark_fhir_schemas.r4.complex_types.claimresponse_error import ClaimResponse_Error
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
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subType", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("use", code.get_schema(recursion_depth + 1), True),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "requestor", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "request", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "outcome", code.get_schema(recursion_depth + 1), True
                ),
                StructField("disposition", StringType(), True),
                StructField("preAuthRef", StringType(), True),
                StructField(
                    "preAuthPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "payeeType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        ClaimResponse_Item.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "addItem",
                    ArrayType(
                        ClaimResponse_AddItem.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "adjudication",
                    ArrayType(
                        ClaimResponse_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "total",
                    ArrayType(
                        ClaimResponse_Total.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "payment",
                    ClaimResponse_Payment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fundsReserve",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "formCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "form", Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "processNote",
                    ArrayType(
                        ClaimResponse_ProcessNote.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "communicationRequest",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "insurance",
                    ArrayType(
                        ClaimResponse_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "error",
                    ArrayType(
                        ClaimResponse_Error.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
