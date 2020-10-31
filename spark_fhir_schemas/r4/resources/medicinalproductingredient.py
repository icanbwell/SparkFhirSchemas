from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.medicinalproductingredient_specifiedsubstance import MedicinalProductIngredient_SpecifiedSubstance
from spark_fhir_schemas.r4.complex_types.medicinalproductingredient_substance import MedicinalProductIngredient_Substance


# noinspection PyPep8Naming
class MedicinalProductIngredient:
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
                StructField("role", CodeableConcept.get_schema(), True),
                StructField("allergenicIndicator", BooleanType(), True),
                StructField(
                    "manufacturer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "specifiedSubstance",
                    ArrayType(
                        MedicinalProductIngredient_SpecifiedSubstance.
                        get_schema()
                    ), True
                ),
                StructField(
                    "substance",
                    MedicinalProductIngredient_Substance.get_schema(), True
                ),
            ]
        )

        return schema
