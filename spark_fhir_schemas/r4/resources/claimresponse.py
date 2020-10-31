from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.claimresponse_item import ClaimResponse_Item
from spark_fhir_schemas.r4.resources.claimresponse_additem import ClaimResponse_AddItem
from spark_fhir_schemas.r4.resources.claimresponse_adjudication import ClaimResponse_Adjudication
from spark_fhir_schemas.r4.resources.claimresponse_total import ClaimResponse_Total
from spark_fhir_schemas.r4.resources.claimresponse_payment import ClaimResponse_Payment
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.claimresponse_processnote import ClaimResponse_ProcessNote
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.claimresponse_insurance import ClaimResponse_Insurance
from spark_fhir_schemas.r4.resources.claimresponse_error import ClaimResponse_Error


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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
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
                StructField("item",ArrayType(ClaimResponse_Item.get_schema()), True),
                StructField("addItem",ArrayType(ClaimResponse_AddItem.get_schema()), True),
                StructField("adjudication",ArrayType(ClaimResponse_Adjudication.get_schema()), True),
                StructField("total",ArrayType(ClaimResponse_Total.get_schema()), True),
                StructField("payment", ClaimResponse_Payment.get_schema(), True),
                StructField("fundsReserve", CodeableConcept.get_schema(), True),
                StructField("formCode", CodeableConcept.get_schema(), True),
                StructField("form", Attachment.get_schema(), True),
                StructField("processNote",ArrayType(ClaimResponse_ProcessNote.get_schema()), True),
                StructField("communicationRequest",ArrayType(Reference.get_schema()), True),
                StructField("insurance",ArrayType(ClaimResponse_Insurance.get_schema()), True),
                StructField("error",ArrayType(ClaimResponse_Error.get_schema()), True),]
        )

        return schema
