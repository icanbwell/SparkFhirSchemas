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
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.paymentreconciliation_detail import PaymentReconciliation_Detail
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.paymentreconciliation_processnote import PaymentReconciliation_ProcessNote


class PaymentReconciliation:
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
                StructField("period", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("paymentIssuer", Reference.get_schema(), True),
                StructField("request", Reference.get_schema(), True),
                StructField("requestor", Reference.get_schema(), True),
                StructField("outcome", StringType(), True),
                StructField("disposition", StringType(), True),
                StructField("paymentDate", DateType(), True),
                StructField("paymentAmount", Money.get_schema(), True),
                StructField("paymentIdentifier", Identifier.get_schema(), True),
                StructField("detail",ArrayType(PaymentReconciliation_Detail.get_schema()), True),
                StructField("formCode", CodeableConcept.get_schema(), True),
                StructField("processNote",ArrayType(PaymentReconciliation_ProcessNote.get_schema()), True),]
        )

        return schema
