from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.observationdefinition_quantitativedetails import ObservationDefinition_QuantitativeDetails
from spark_fhir_schemas.r4.complex_types.observationdefinition_qualifiedinterval import ObservationDefinition_QualifiedInterval
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class ObservationDefinition:
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
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("multipleResultsAllowed", BooleanType(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("preferredReportName", StringType(), True),
                StructField(
                    "quantitativeDetails",
                    ObservationDefinition_QuantitativeDetails.get_schema(),
                    True
                ),
                StructField(
                    "qualifiedInterval",
                    ArrayType(
                        ObservationDefinition_QualifiedInterval.get_schema()
                    ), True
                ),
                StructField(
                    "validCodedValueSet", Reference.get_schema(), True
                ),
                StructField(
                    "normalCodedValueSet", Reference.get_schema(), True
                ),
                StructField(
                    "abnormalCodedValueSet", Reference.get_schema(), True
                ),
                StructField(
                    "criticalCodedValueSet", Reference.get_schema(), True
                ),
            ]
        )

        return schema
