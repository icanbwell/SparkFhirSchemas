from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.supplydelivery_supplieditem import SupplyDelivery_SuppliedItem
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.timing import Timing


# noinspection PyPep8Naming
class SupplyDelivery:
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
                    "basedOn", ArrayType(Reference.get_schema()), True
                ),
                StructField("partOf", ArrayType(Reference.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField(
                    "suppliedItem", SupplyDelivery_SuppliedItem.get_schema(),
                    True
                ),
                StructField("occurrenceDateTime", StringType(), True),
                StructField("occurrencePeriod", Period.get_schema(), True),
                StructField("occurrenceTiming", Timing.get_schema(), True),
                StructField("supplier", Reference.get_schema(), True),
                StructField("destination", Reference.get_schema(), True),
                StructField(
                    "receiver", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
