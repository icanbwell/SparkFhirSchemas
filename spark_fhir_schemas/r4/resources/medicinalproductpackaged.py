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
from spark_fhir_schemas.r4.complex_types.marketingstatus import MarketingStatus
from spark_fhir_schemas.r4.complex_types.medicinalproductpackaged_batchidentifier import MedicinalProductPackaged_BatchIdentifier
from spark_fhir_schemas.r4.complex_types.medicinalproductpackaged_packageitem import MedicinalProductPackaged_PackageItem


# noinspection PyPep8Naming
class MedicinalProductPackaged:
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
                    "subject", ArrayType(Reference.get_schema()), True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "legalStatusOfSupply", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "marketingStatus", ArrayType(MarketingStatus.get_schema()),
                    True
                ),
                StructField(
                    "marketingAuthorization", Reference.get_schema(), True
                ),
                StructField(
                    "manufacturer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "batchIdentifier",
                    ArrayType(
                        MedicinalProductPackaged_BatchIdentifier.get_schema()
                    ), True
                ),
                StructField(
                    "packageItem",
                    ArrayType(
                        MedicinalProductPackaged_PackageItem.get_schema()
                    ), True
                ),
            ]
        )

        return schema
