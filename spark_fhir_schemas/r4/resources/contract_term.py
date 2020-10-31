from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.contract_securitylabel import Contract_SecurityLabel
from spark_fhir_schemas.r4.resources.contract_offer import Contract_Offer
from spark_fhir_schemas.r4.resources.contract_asset import Contract_Asset
from spark_fhir_schemas.r4.resources.contract_action import Contract_Action
from spark_fhir_schemas.r4.resources.contract_term import Contract_Term


class Contract_Term:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("issued", dateTime.get_schema(), True),
                StructField("applies", Period.get_schema(), True),
                StructField("topicCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("topicReference", Reference.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType", CodeableConcept.get_schema(), True),
                StructField("text", StringType(), True),
                StructField("securityLabel",ArrayType(Contract_SecurityLabel.get_schema()), True),
                StructField("offer", Contract_Offer.get_schema(), True),
                StructField("asset",ArrayType(Contract_Asset.get_schema()), True),
                StructField("action",ArrayType(Contract_Action.get_schema()), True),
                StructField("group",ArrayType(Contract_Term.get_schema()), True),]
        )

        return schema
