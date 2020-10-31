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
from spark_fhir_schemas.r4.complex_types.medicinalproductpharmaceutical_characteristics import MedicinalProductPharmaceutical_Characteristics
from spark_fhir_schemas.r4.complex_types.medicinalproductpharmaceutical_routeofadministration import MedicinalProductPharmaceutical_RouteOfAdministration


# noinspection PyPep8Naming
class MedicinalProductPharmaceutical:
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
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField(
                    "administrableDoseForm", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "unitOfPresentation", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "ingredient", ArrayType(Reference.get_schema()), True
                ),
                StructField("device", ArrayType(Reference.get_schema()), True),
                StructField(
                    "characteristics",
                    ArrayType(
                        MedicinalProductPharmaceutical_Characteristics.
                        get_schema()
                    ), True
                ),
                StructField(
                    "routeOfAdministration",
                    ArrayType(
                        MedicinalProductPharmaceutical_RouteOfAdministration.
                        get_schema()
                    ), True
                ),
            ]
        )

        return schema