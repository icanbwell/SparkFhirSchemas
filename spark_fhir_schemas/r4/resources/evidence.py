from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.usagecontext import UsageContext
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference


class Evidence:
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
                StructField("url", uri.get_schema(), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("shortTitle", StringType(), True),
                StructField("subtitle", StringType(), True),
                StructField("status", StringType(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("publisher", StringType(), True),
                StructField("contact",ArrayType(ContactDetail.get_schema()), True),
                StructField("description", markdown.get_schema(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("useContext",ArrayType(UsageContext.get_schema()), True),
                StructField("jurisdiction",ArrayType(CodeableConcept.get_schema()), True),
                StructField("copyright", markdown.get_schema(), True),
                StructField("approvalDate", DateType(), True),
                StructField("lastReviewDate", DateType(), True),
                StructField("effectivePeriod", Period.get_schema(), True),
                StructField("topic",ArrayType(CodeableConcept.get_schema()), True),
                StructField("author",ArrayType(ContactDetail.get_schema()), True),
                StructField("editor",ArrayType(ContactDetail.get_schema()), True),
                StructField("reviewer",ArrayType(ContactDetail.get_schema()), True),
                StructField("endorser",ArrayType(ContactDetail.get_schema()), True),
                StructField("relatedArtifact",ArrayType(RelatedArtifact.get_schema()), True),
                StructField("exposureBackground", Reference.get_schema(), True),
                StructField("exposureVariant",ArrayType(Reference.get_schema()), True),
                StructField("outcome",ArrayType(Reference.get_schema()), True),]
        )

        return schema
