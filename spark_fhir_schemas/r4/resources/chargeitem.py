from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.chargeitem_performer import ChargeItem_Performer
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class ChargeItem:
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
                StructField(
                    "definitionUri", ArrayType(uri.get_schema()), True
                ),
                StructField(
                    "definitionCanonical", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField("status", StringType(), True),
                StructField("partOf", ArrayType(Reference.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("context", Reference.get_schema(), True),
                StructField("occurrenceDateTime", StringType(), True),
                StructField("occurrencePeriod", Period.get_schema(), True),
                StructField("occurrenceTiming", Timing.get_schema(), True),
                StructField(
                    "performer", ArrayType(ChargeItem_Performer.get_schema()),
                    True
                ),
                StructField(
                    "performingOrganization", Reference.get_schema(), True
                ),
                StructField(
                    "requestingOrganization", Reference.get_schema(), True
                ),
                StructField("costCenter", Reference.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField(
                    "bodysite", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("factorOverride", decimal.get_schema(), True),
                StructField("priceOverride", Money.get_schema(), True),
                StructField("overrideReason", StringType(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("enteredDate", dateTime.get_schema(), True),
                StructField(
                    "reason", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "service", ArrayType(Reference.get_schema()), True
                ),
                StructField("productReference", Reference.get_schema(), True),
                StructField(
                    "productCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "account", ArrayType(Reference.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "supportingInformation", ArrayType(Reference.get_schema()),
                    True
                ),
            ]
        )

        return schema
