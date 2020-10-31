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
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.insuranceplan_contact import InsurancePlan_Contact
from spark_fhir_schemas.r4.complex_types.insuranceplan_coverage import InsurancePlan_Coverage
from spark_fhir_schemas.r4.complex_types.insuranceplan_plan import InsurancePlan_Plan


# noinspection PyPep8Naming
class InsurancePlan:
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
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("name", StringType(), True),
                StructField("alias", ArrayType(StringType()), True),
                StructField("period", Period.get_schema(), True),
                StructField("ownedBy", Reference.get_schema(), True),
                StructField("administeredBy", Reference.get_schema(), True),
                StructField(
                    "coverageArea", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "contact", ArrayType(InsurancePlan_Contact.get_schema()),
                    True
                ),
                StructField(
                    "endpoint", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "network", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "coverage", ArrayType(InsurancePlan_Coverage.get_schema()),
                    True
                ),
                StructField(
                    "plan", ArrayType(InsurancePlan_Plan.get_schema()), True
                ),
            ]
        )

        return schema
