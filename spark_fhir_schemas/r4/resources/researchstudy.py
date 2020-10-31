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
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.contactdetail import ContactDetail
from spark_fhir_schemas.r4.resources.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.researchstudy_arm import ResearchStudy_Arm
from spark_fhir_schemas.r4.resources.researchstudy_objective import ResearchStudy_Objective


class ResearchStudy:
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
                StructField("title", StringType(), True),
                StructField("protocol",ArrayType(Reference.get_schema()), True),
                StructField("partOf",ArrayType(Reference.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("primaryPurposeType", CodeableConcept.get_schema(), True),
                StructField("phase", CodeableConcept.get_schema(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("focus",ArrayType(CodeableConcept.get_schema()), True),
                StructField("condition",ArrayType(CodeableConcept.get_schema()), True),
                StructField("contact",ArrayType(ContactDetail.get_schema()), True),
                StructField("relatedArtifact",ArrayType(RelatedArtifact.get_schema()), True),
                StructField("keyword",ArrayType(CodeableConcept.get_schema()), True),
                StructField("location",ArrayType(CodeableConcept.get_schema()), True),
                StructField("description", markdown.get_schema(), True),
                StructField("enrollment",ArrayType(Reference.get_schema()), True),
                StructField("period", Period.get_schema(), True),
                StructField("sponsor", Reference.get_schema(), True),
                StructField("principalInvestigator", Reference.get_schema(), True),
                StructField("site",ArrayType(Reference.get_schema()), True),
                StructField("reasonStopped", CodeableConcept.get_schema(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("arm",ArrayType(ResearchStudy_Arm.get_schema()), True),
                StructField("objective",ArrayType(ResearchStudy_Objective.get_schema()), True),]
        )

        return schema
