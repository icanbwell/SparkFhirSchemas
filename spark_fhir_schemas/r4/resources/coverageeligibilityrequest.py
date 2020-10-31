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
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_supportinginfo import CoverageEligibilityRequest_SupportingInfo
from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_insurance import CoverageEligibilityRequest_Insurance
from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_item import CoverageEligibilityRequest_Item


# noinspection PyPep8Naming
class CoverageEligibilityRequest:
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
                StructField("priority", CodeableConcept.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("servicedDate", StringType(), True),
                StructField("servicedPeriod", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("provider", Reference.get_schema(), True),
                StructField("insurer", Reference.get_schema(), True),
                StructField("facility", Reference.get_schema(), True),
                StructField(
                    "supportingInfo",
                    ArrayType(
                        CoverageEligibilityRequest_SupportingInfo.get_schema()
                    ), True
                ),
                StructField(
                    "insurance",
                    ArrayType(
                        CoverageEligibilityRequest_Insurance.get_schema()
                    ), True
                ),
                StructField(
                    "item",
                    ArrayType(CoverageEligibilityRequest_Item.get_schema()),
                    True
                ),
            ]
        )

        return schema
