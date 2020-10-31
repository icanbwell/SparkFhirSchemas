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
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.coverage_class import Coverage_Class
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.coverage_costtobeneficiary import Coverage_CostToBeneficiary
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.reference import Reference


class Coverage:
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
                StructField("policyHolder", Reference.get_schema(), True),
                StructField("subscriber", Reference.get_schema(), True),
                StructField("subscriberId", StringType(), True),
                StructField("beneficiary", Reference.get_schema(), True),
                StructField("dependent", StringType(), True),
                StructField("relationship", CodeableConcept.get_schema(), True),
                StructField("period", Period.get_schema(), True),
                StructField("payor",ArrayType(Reference.get_schema()), True),
                StructField("class",ArrayType(Coverage_Class.get_schema()), True),
                StructField("order", positiveInt.get_schema(), True),
                StructField("network", StringType(), True),
                StructField("costToBeneficiary",ArrayType(Coverage_CostToBeneficiary.get_schema()), True),
                StructField("subrogation", BooleanType(), True),
                StructField("contract",ArrayType(Reference.get_schema()), True),]
        )

        return schema
