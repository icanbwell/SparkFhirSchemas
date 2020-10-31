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
from spark_fhir_schemas.r4.complex_types.invoice_participant import Invoice_Participant
from spark_fhir_schemas.r4.complex_types.invoice_lineitem import Invoice_LineItem
from spark_fhir_schemas.r4.complex_types.invoice_pricecomponent import Invoice_PriceComponent
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class Invoice:
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
                StructField("status", StringType(), True),
                StructField("cancelledReason", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("recipient", Reference.get_schema(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField(
                    "participant", ArrayType(Invoice_Participant.get_schema()),
                    True
                ),
                StructField("issuer", Reference.get_schema(), True),
                StructField("account", Reference.get_schema(), True),
                StructField(
                    "lineItem", ArrayType(Invoice_LineItem.get_schema()), True
                ),
                StructField(
                    "totalPriceComponent",
                    ArrayType(Invoice_PriceComponent.get_schema()), True
                ),
                StructField("totalNet", Money.get_schema(), True),
                StructField("totalGross", Money.get_schema(), True),
                StructField("paymentTerms", markdown.get_schema(), True),
                StructField("note", ArrayType(Annotation.get_schema()), True),
            ]
        )

        return schema
