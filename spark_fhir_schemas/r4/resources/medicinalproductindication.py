from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.medicinalproductindication_othertherapy import MedicinalProductIndication_OtherTherapy
from spark_fhir_schemas.r4.complex_types.population import Population


# noinspection PyPep8Naming
class MedicinalProductIndication:
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
                    "subject", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "diseaseSymptomProcedure", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "diseaseStatus", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "comorbidity", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "intendedEffect", CodeableConcept.get_schema(), True
                ),
                StructField("duration", Quantity.get_schema(), True),
                StructField(
                    "otherTherapy",
                    ArrayType(
                        MedicinalProductIndication_OtherTherapy.get_schema()
                    ), True
                ),
                StructField(
                    "undesirableEffect", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "population", ArrayType(Population.get_schema()), True
                ),
            ]
        )

        return schema
