from pyspark.sql.types import ArrayType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
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


# noinspection PyPep8Naming
class ClaimResponse:
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
                StructField("status", code.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType", CodeableConcept.get_schema(), True),
                StructField("use", code.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("insurer", Reference.get_schema(), True),
                StructField("requestor", Reference.get_schema(), True),
                StructField("request", Reference.get_schema(), True),
                StructField("outcome", code.get_schema(), True),
                StructField("disposition", StringType(), True),
                StructField("preAuthRef", StringType(), True),
                StructField("preAuthPeriod", Period.get_schema(), True),
                StructField("payeeType", CodeableConcept.get_schema(), True),
                StructField(
                    "item", ArrayType(ClaimResponse_Item.get_schema()), True
                ),
                StructField(
                    "addItem", ArrayType(ClaimResponse_AddItem.get_schema()),
                    True
                ),
                StructField(
                    "adjudication",
                    ArrayType(ClaimResponse_Adjudication.get_schema()), True
                ),
                StructField(
                    "total", ArrayType(ClaimResponse_Total.get_schema()), True
                ),
                StructField(
                    "payment", ClaimResponse_Payment.get_schema(), True
                ),
                StructField(
                    "fundsReserve", CodeableConcept.get_schema(), True
                ),
                StructField("formCode", CodeableConcept.get_schema(), True),
                StructField("form", Attachment.get_schema(), True),
                StructField(
                    "processNote",
                    ArrayType(ClaimResponse_ProcessNote.get_schema()), True
                ),
                StructField(
                    "communicationRequest", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "insurance",
                    ArrayType(ClaimResponse_Insurance.get_schema()), True
                ),
                StructField(
                    "error", ArrayType(ClaimResponse_Error.get_schema()), True
                ),
            ]
        )

        return schema
