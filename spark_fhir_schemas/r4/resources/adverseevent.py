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
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.adverseevent_suspectentity import AdverseEvent_SuspectEntity


# noinspection PyPep8Naming
class AdverseEvent:
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
                StructField("identifier", Identifier.get_schema(), True),
                StructField("actuality", StringType(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("event", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("detected", dateTime.get_schema(), True),
                StructField("recordedDate", dateTime.get_schema(), True),
                StructField(
                    "resultingCondition", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField("location", Reference.get_schema(), True),
                StructField("seriousness", CodeableConcept.get_schema(), True),
                StructField("severity", CodeableConcept.get_schema(), True),
                StructField("outcome", CodeableConcept.get_schema(), True),
                StructField("recorder", Reference.get_schema(), True),
                StructField(
                    "contributor", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "suspectEntity",
                    ArrayType(AdverseEvent_SuspectEntity.get_schema()), True
                ),
                StructField(
                    "subjectMedicalHistory", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "referenceDocument", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField("study", ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
