from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.insuranceplan_generalcost import InsurancePlan_GeneralCost
from spark_fhir_schemas.r4.resources.insuranceplan_specificcost import InsurancePlan_SpecificCost


class InsurancePlan_Plan:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("coverageArea",ArrayType(Reference.get_schema()), True),
                StructField("network",ArrayType(Reference.get_schema()), True),
                StructField("generalCost",ArrayType(InsurancePlan_GeneralCost.get_schema()), True),
                StructField("specificCost",ArrayType(InsurancePlan_SpecificCost.get_schema()), True),]
        )

        return schema
