from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSourceMaterial:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_fractiondescription import SubstanceSourceMaterial_FractionDescription
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_organism import SubstanceSourceMaterial_Organism
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_partdescription import SubstanceSourceMaterial_PartDescription
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "sourceMaterialClass",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sourceMaterialType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sourceMaterialState",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "organismId", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("organismName", StringType(), True),
                StructField(
                    "parentSubstanceId",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "parentSubstanceName", ArrayType(StringType()), True
                ),
                StructField(
                    "countryOfOrigin",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "geographicalLocation", ArrayType(StringType()), True
                ),
                StructField(
                    "developmentStage",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fractionDescription",
                    ArrayType(
                        SubstanceSourceMaterial_FractionDescription.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "organism",
                    SubstanceSourceMaterial_Organism.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "partDescription",
                    ArrayType(
                        SubstanceSourceMaterial_PartDescription.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
