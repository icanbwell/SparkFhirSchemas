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
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.contract_contentdefinition import Contract_ContentDefinition
from spark_fhir_schemas.r4.resources.contract_term import Contract_Term
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.contract_signer import Contract_Signer
from spark_fhir_schemas.r4.resources.contract_friendly import Contract_Friendly
from spark_fhir_schemas.r4.resources.contract_legal import Contract_Legal
from spark_fhir_schemas.r4.resources.contract_rule import Contract_Rule
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.reference import Reference


class Contract:
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
                StructField("url", uri.get_schema(), True),
                StructField("version", StringType(), True),
                StructField("status", code.get_schema(), True),
                StructField("legalState", CodeableConcept.get_schema(), True),
                StructField("instantiatesCanonical", Reference.get_schema(), True),
                StructField("instantiatesUri", uri.get_schema(), True),
                StructField("contentDerivative", CodeableConcept.get_schema(), True),
                StructField("issued", dateTime.get_schema(), True),
                StructField("applies", Period.get_schema(), True),
                StructField("expirationType", CodeableConcept.get_schema(), True),
                StructField("subject",ArrayType(Reference.get_schema()), True),
                StructField("authority",ArrayType(Reference.get_schema()), True),
                StructField("domain",ArrayType(Reference.get_schema()), True),
                StructField("site",ArrayType(Reference.get_schema()), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("subtitle", StringType(), True),
                StructField("alias",ArrayType(string.get_schema()), True),
                StructField("author", Reference.get_schema(), True),
                StructField("scope", CodeableConcept.get_schema(), True),
                StructField("topicCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("topicReference", Reference.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("contentDefinition", Contract_ContentDefinition.get_schema(), True),
                StructField("term",ArrayType(Contract_Term.get_schema()), True),
                StructField("supportingInfo",ArrayType(Reference.get_schema()), True),
                StructField("relevantHistory",ArrayType(Reference.get_schema()), True),
                StructField("signer",ArrayType(Contract_Signer.get_schema()), True),
                StructField("friendly",ArrayType(Contract_Friendly.get_schema()), True),
                StructField("legal",ArrayType(Contract_Legal.get_schema()), True),
                StructField("rule",ArrayType(Contract_Rule.get_schema()), True),
                StructField("legallyBindingAttachment", Attachment.get_schema(), True),
                StructField("legallyBindingReference", Reference.get_schema(), True),]
        )

        return schema
